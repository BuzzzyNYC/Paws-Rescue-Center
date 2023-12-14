from flask import Flask, render_template, abort
from forms import SignUpForm, LogInForm
from flask import session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fyatrangtranghawuy6273283dbyxgydu'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///paws.db'
#db = SQLAlchemy(app)


# """Model for pets"""
# class Pet(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, unique=True)
#     age = db.Column(db.String)
#     bio = db.Column(db.String)

# """Model for Users"""
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     full_name = db.Column(db.String)
#     email = db.Column(db.String, unique=True)
#     password = db.Column(db.String)

# db.create_all()






"""Information about the pets in the database"""
pets = [
    {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten"},
    {"id": 2, "name": "Kelly", "age": "53 weeks", "bio": "I am a tiny doggie"},
    {"id": 3, "name": "Kello", "age": "53 weeks", "bio": "I am a tiny doggie"},
    {"id": 4, "name": "Kelly", "age": "53 weeks", "bio": "I am a tiny doggie"},
]


"""Information about the Users in the database"""
users = [
    {"id":1, "full_name":"Trang Nguyen", "email": "trangtpu92@yahoo.com", "password": "12345"},
]

@app.route("/")
def home():
    """View for the Home page of the website"""
    return render_template("home.html", pets=pets)
    
@app.route("/about")
def about():
    """View About page"""
    return render_template("about.html")

@app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    """View function to show pet details for each pet."""
    pet = next((pet for pet in pets if pet["id"] == pet_id), None)
    if pet is None:
        abort(404, description="No Pet was found with the given ID")
    return render_template("details.html", pet = pet)

@app.route("/signup", methods=["POST", "GET"])
def signup():
    """Sign up form"""
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = {"id": len(users)+1, "full_name": form.full_name.data, "email": form.email.data, "password": form.password.data}
        users.append(new_user)
        return render_template("signup.html", message="Successfully signed up")
    return render_template("signup.html", form = form)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        user = next((user for user in users if user["email"] == form.email.data and user["password"] == form.password.data), None)
        if user is None:
            return render_template("login.html", form = form, message = "Wrong Credentials. Please Try Again.")
        else:
            session['user'] = user
            return render_template("login.html", message = "Successfully Logged In!")
    return render_template("login.html", form = form)

@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('home', _scheme='https', _external=True))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
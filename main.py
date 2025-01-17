import pyrebase
import click
import pwinput 

firebaseConfig = {

            apiKey: "AIzaSyB0Vp3l7qBCzgBLzoXhCOLtAr-nEh8-1mo",

            authDomain: "skillsync-project.firebaseapp.com",

            projectId: "skillsync-project",

            storageBucket: "skillsync-project.firebasestorage.app",

            messagingSenderId: "281111673415",

            appId: "1:281111673415:web:4c27bd29ee5423b8544f62",

            measurementId: "G-8P3QE6ZG0G"
  }


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@click.group():
def cli():
    pass

@cli.command()
click.echo("Login to your account")
def login():
    email = click.prompt("enter email: ",type = str)
    password = click.prompt("enter password: ",mask ="*")
    try:
        login = auth.sign_in_with_email_and_password(email,password)
        click.echo("Login successful!!")
    except:
        click.echo("Invalid email or password")
    return

@cli.command()
click.echo("Create an Account")
def SignUp():
    email = click.prompt("enter password: ",type = str)
    password = click.prompt("enter password: ",mask ="*")
    confirm_password = pwinput(prompt = "confirm password: ",mask ="*")
    if password != confirm_password:
        click.echo("passwords do not match!")
        return
    click.echo("Below state if you're a Mentor or Mentee")
    role = click.prompt("Enter your role: ",type =str)
    if role not in "mentor,mentee":
        click.echo("Invalid input,please enter the correct input")
        return
    try:
        user = auth.create_user_with_email_and_password(email,password)
        click.echo("Account created successfully")
    except:
        click.echo("Email already exists!")
    return

if __name__=="__main__":
       cli()

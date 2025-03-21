import pyrebase
import click
import pwinput
import requests
from firebase_admin import credentials, firestore


 

firebaseConfig = {

            "apiKey": "AIzaSyB0Vp3l7qBCzgBLzoXhCOLtAr-nEh8-1mo",

            "authDomain": "skillsync-project.firebaseapp.com",

            "projectId": "skillsync-project",

            "databaseURL": "https://console.firebase.google.com/project/skillsync-project/database/skillsync-project-default-rtdb/data/~2F",

            "storageBucket": "skillsync-project.firebasestorage.app",

            "messagingSenderId": "281111673415",

            "appId": "1:281111673415:web:4c27bd29ee5423b8544f62",

            "measurementId": "G-8P3QE6ZG0G"
  }


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
# Initialize Firebase Admin SDK


@click.group()
def cli():
    pass

@cli.command()

def get_db():
    return db

def get_auth():
    return auth

def login():
    click.echo("Login to your account")
    email = click.prompt("enter email: ",type=str)
    password = click.prompt("enter password: ",mask ="*")
    try:
        login = auth.sign_in_with_email_and_password(email,password)
        click.echo("Login successful!!")
    except:
        click.echo("Invalid email or password")
    return


def signup():
    click.echo("Create an Account")
    email = click.prompt("Enter email", type=str)
    password = click.prompt("Enter password", hide_input=True)
    confirm_password = click.prompt("Confirm password", hide_input=True)

    if password != confirm_password:
        click.echo("Passwords do not match!")
        return

    role = click.prompt("Are you a mentor or mentee?", type=str).lower()
    if role not in ["mentor", "mentee"]:
        click.echo("Invalid role! Choose 'mentor' or 'mentee'.")
        return

    try:
        user = auth.create_user_with_email_and_password(email, password)
        user_id = user["localId"]

    
        db.collection("users").document(user_id).set({
            "email": email,
            "role": role
        })

        click.echo("Account created successfully!")

    except:
        click.echo("Error: Email already exists!")


@click.option("--expertise", "-e", type=str, help="Filter by expertise (e.g., Python, Java)")
@click.option("--availability", "-a", type=str, help="Filter by availability (e.g., Monday 10:00-12:00)")
def search_users(expertise, availability):
    #Search for mentors/peers by expertise or availability
    users = db.child("users").get().val()
    
    if not users:
        click.echo("No users found in the database.")
        return

    filtered_users = []
    
    for user_id, user_data in users.items():
        if expertise and expertise not in user_data.get("expertise", []):
            continue  # Skip users who don’t match expertise
        
        if availability and availability not in user_data.get("availability", []):
            continue  # Skip users who don’t match availability
        
        filtered_users.append(user_data)

    if filtered_users:
        click.echo("Available mentors/peers:")
        for user in filtered_users:
            click.echo(f"- {user['name']} ({user['role']}) | Expertise: {', '.join(user.get('expertise', []))}")
    else:
        click.echo("No users found matching the filters.")

if __name__ == "__main__":
    search_users()











    
if __name__=="__main__":
       cli()
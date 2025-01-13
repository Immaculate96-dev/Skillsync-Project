import pyrebase
import click

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

def login():
    email = input("enter email: ")
    password = input("enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email,password)
    except:
        print("Invalid email or password")
    return


def SignUp():
    email = input("enter password: ")
    password = input("enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email,password)
    except:
        print("email already exists!")
    return


ans = input("Do you have an account? [y/n]")

if ans == "n":
    login()
else:
    SignUp()
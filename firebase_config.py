import pyrebase

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



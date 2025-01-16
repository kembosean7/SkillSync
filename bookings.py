from firebase_config import firebase_client, intialize_firebase
from datetime import datetime
intialize_firebase()


#Fetch and display a list of available mentors
def get_mentors():
    try:
        user_ref = firebase_client().collection('users')
        users = user_ref.get()

        if users:
            for user in users:
                user_data = user.to_dict()
                if  user_data['role'] == 'peer':
                    print(f"Name: {user_data['name']}, Email: {user_data['email']}, Role: {user_data['role']}")
        else:
            print(f"No users found. ")


    
    except Exception as e:
        print(f"Error occured: {e}")




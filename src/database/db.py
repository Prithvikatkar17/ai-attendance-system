from src.database.config import supabase
import bcrypt


def hash_pass(pwd):
    #hashes the password using bcrypt and returns the hashed password
    return bcrypt.hashpw(pwd.encode(),bcrypt.gensalt()).decode()
    # encode() is used to convert the password string to bytes, which is required by bcrypt. 
    #  The hashed password is then decoded back to a string for storage in the database.
    # gensalt() generates a random salt for each password, enhancing security by ensuring 
    # that even identical passwords will have different hashes.



def check_pass(pwd,hashed):    #checks if the password matches the hashed password
    return bcrypt.checkpw(pwd.encode(),hashed.encode()) #checkpw() takes the plain password and the hashed password, 
                                                        #encodes them to bytes, and returns True if they match, otherwise False.

def check_teacher_exists(username):
    #checks for unique username and returns false if username already exists
    response = supabase.table('teachers').select('username').eq('username', username).execute()
    return len(response.data) > 0

def create_teacher(username, password,name):
    
    data = {
        'username': username,
        'password': hash_pass(password),
        'name': name
    }
    response = supabase.table('teachers').insert(data).execute()
    return response.data

def teacher_login(username,password):
    response = supabase.table('teachers').select('*').eq('username', username).execute()
    # The select('*') method retrieves all columns for the matching record, 
    # and eq('username', username) filters the records to find the one with the specified username.   
    if response.data:   # If a record is found, response.data will contain a list of matching records (in this case,
                        # it should be a list with one record since usernames are unique).
        teacher = response.data[0]  # We take the first record from the list (response.data[0]) to get the teacher's information, 
                        # which includes the hashed password stored in the database.
        if check_pass(password, teacher['password']): # We then use the check_pass function to compare the
                                                    # provided password with the hashed password from the database.
            return teacher
    return None
    # If no matching record is found or if the password does not match, the function returns None, indicating a failed login attempt.


def get_all_students():
    response = supabase.table('students').select('*').execute()
    return response.data  
# This function retrieves all records from the 'students' table in the database and returns them as a list of dictionaries. Each dictionary represents a student record with its corresponding fields and values.


def create_student(new_name , face_embedding = None , voice_embedding = None):
    data = {'name':new_name ,'face_embedding':face_embedding , 'voice_embedding': voice_embedding}
    response = supabase.table('students').insert(data).execute()
    return response.data



def create_subject(sublect_code ,name ,section,teacher_id):
    data = {"subject_code":sublect_code,"name":name,"section":section,"teacher_id":teacher_id}
    response = supabase.table("subjects").insert(data).execute()
    return response.data
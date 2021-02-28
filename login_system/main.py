import pymongo

f = open('login_system/\secretfile.txt')

client = pymongo.MongoClient(f.readline())
mydb = client["learning_projects"]
mycol = mydb["accounts"]

def username_check(db_user, user_user):
    if db_user == user_user:
        return True

def password_check(db_pw, user_pw):
    if db_pw == user_pw:
        return True

print("Press '1' to login. Press '2' to Create new account.")
option = int(input())

username = input("Enter your username: ")

if option == 1:
    for x in mycol.find({},{"_id": 0, "username": 1, "password": 1}):
        user_exist = username_check(x['username'], username)
        if user_exist:
            i=0
            password_match = password_check(x['password'], input("Enter a password: "))
            while password_match == None and i < 3:
                print("Attempt #", i+1, "of 3")
                password_retry = password_check(x['password'], input("Password does not match our records, try again: "))
                i += 1
                if password_retry:
                    print("Success")
                    break

else:
    for x in mycol.find({},{"_id": 0, "username": 1}):
        if x['username'] == username:
            print("Username already exists, try again: ")
            break
        password = input("Enter a password: ")
        mydict = {"username":username, "password":password }
        db_insert = mycol.insert_one(mydict)
        break
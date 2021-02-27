import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:jTyveGk8wwGKL8H@cluster0.nkldq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = client["learning_projects"]
mycol = mydb["accounts"]

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False


mydict = {}

print("Press '1' to login. Press '2' to Create new account.")
option = int(input())

if option == 1:
    username = input("Enter your username: ")

    for x in mycol.find({},{"_id": 0, "username": 1, "password": 1}):
        
        if x['username'] == username:
            password = input("Enter your password: ")

            if x['password'] == password:
                print("Login Success!")
                break
            else:
                i = 0
                while i < 3:
                    #retry_password = "Invalid Password. Try again, retry number", i+1, "of 3: "
                    retry_password = "Invalid password. Try again: "
                    pass_retry = input(retry_password)
                    success = pass_retry == x['password']
                    i += 1 
                    if success:
                        print("Login Success!")
                        break
                else:
                    print("Login failure, reached maximum allowed password attempts.")
                    break

    #print("Username does not exist in our records. Create a new one.")

else:
    username = input("Enter a username: ")

    for x in mycol.find({},{"_id": 0, "username": 1, "password": 1}):
        if x['username'] == username:
            print("Username already exists, try again: ")
            break
        password = input("Enter a password: ")
        mydict.update({"username":username, "password":password })
        db_insert = mycol.insert_one(mydict)
        break
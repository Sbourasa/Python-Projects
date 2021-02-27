import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:jTyveGk8wwGKL8H@cluster0.nkldq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = client["learning_projects"]
mycol = mydb["accounts"]

mydict = {}

option = int(input("Press '1' to login. Press '2' to Create new account.:  "))

if option == 1:
    username = input("Enter your username: ")

    for x in mycol.find({},{"_id": 0, "username": 1, "password": 1}):
        
        if x['username'] == username:
            password = input("Enter your password: ")

            if x['password'] == password:
                print("Login Success!")
                break
            else:
                print("Invalid Password, try again : ") #TODO make this a loop 3x
        
        pass

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
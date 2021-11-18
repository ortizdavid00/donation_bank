# Login function returning username to compare with database list
def login(database, username, password):
    if username.lower() in database and database[username] == password:
        print("Welcome", username.lower() + "!")
        return username
    elif username.lower() in database and database[username] != password:
        print("Please enter the correct password for", username.lower())
        return ""
    else:
        print("Failed to login!")
        return ""

# Registration function returning username to add to database list
def register(database, username, password):
    if username.lower() in database:
        print("Username already registered!")
        return ""
    else:
        print(username.lower(), "has been registered!")
        return username

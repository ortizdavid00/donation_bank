# PWInput hides password characters for users
import pwinput
# Importing modules from donations_pkg
import donations_pkg
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

# Global (Application) variable definitions
database = {"admin": "password123"}
donations = []
authorized_user = ""

# Main application loop
while True:
    donations_pkg.homepage.show_homepage(authorized_user)
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)

    # If/elif statements for each main menu options
    option = input("Choose an option: ").lower()
    if option == "1" or option == "login":
        username = input("Please enter a username: ").lower()
        password = pwinput.pwinput("Please enter a password: ")
        authorized_user = donations_pkg.user.login(database, username, password)
    elif option == "2" or option == "register":
        username = input("Please register a username: ").lower()
        password = pwinput.pwinput("Please register a password: ")
        authorized_user = donations_pkg.user.register(database, username, password)
        if authorized_user != "":
            database[username] = password
    elif option == "3" or option == "donate":
        if authorized_user == "":
            print("You are not logged in! Please log in to donate.")
        else:
            donation = donations_pkg.homepage.donate(username)
            donations.append(donation)
    elif option == "4" or option == "show donations":
        donations_pkg.homepage.show_donations(donations)
    elif option == "5" or option == "exit":
        print("Goodbye!")
        exit()
    else:
        print("Option not recognized. Please enter a valid option!")

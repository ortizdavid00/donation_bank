# Main menu display
def show_homepage(authorized_user):
    print("")
    print("         === DonateMe Homepage ==            ")
    print("---------------------------------------------")
    print("| 1. Login           | 2. Register          |")
    print("---------------------------------------------")
    print("| 3. Donate          | 4. Show Donations    |")
    print("---------------------------------------------")
    print("|                 5.   Exit                 |")
    print("---------------------------------------------")

# Donation function. Try/except to catch any inputs besides numbers
def donate(username):
    while True:
        try:
            donation_atm = float(input("Enter an amount to donate: "))
            donation = username + " donated " + str(donation_atm)
            print("Thank you for your donation!")
            return donation
        except:
            print("Enter a valid amount!")
            continue

# Show donations functionality. Will display string if no donations available
def show_donations(donations):
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        # total = 0
        for donation in donations:
            print(donation)
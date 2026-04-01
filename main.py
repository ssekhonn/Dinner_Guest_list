# Guest List Manager
# This program helps manage guests for a reception dinner.

guests = []

"""
PSEUDOCODE

1. Create empty guest list

2. Each guest will store:
   - name
   - RSVP status (Attending, Not Attending, Maybe)

3. Create functions:
   - add_guest
   - modify_guest
   - remove_guest
   - sort_guests
   - show_guest_list
   - search_guest
   - show_invitations
   - count_attending_guests
   - show_seating_plan

4. Validate input
   - no empty names
   - remove spaces
   - format names
   - reject duplicate guests

5. Menu loop
   - display options
   - user selects feature
   - call correct function

6. Seating plan
   - assign guests to tables
   - display tables
"""


def format_name(name):
    return name.strip().title()


def add_guest(name, rsvp):  # adds a 2 parameter function for name and rsvp status

    name = format_name(name)

    if not name:
        print("Invalid name.")
        return

    # Name validation: letters and spaces only
    # (" ", "").isalpha means it will remove spaces and check if the remaining characters are letters
    if not name.replace(" ", "").isalpha():
        print("Invalid name. Please enter letters only.")
        return

    for guest in guests:  # guest is a variable that represents each guest in the guests list. It checks if the name of the guest matches the name being added. If it does, it prints a message and returns without adding the guest.
        if guest["name"] == name:
            print("Guest already exists.")
            return

    guests.append({  # adds a new guest to the guests list. It creates a dictionary with the keys "name" and "rsvp" and assigns the values of the name and rsvp parameters passed to the function.
        # this is a key-value pair in the dictionary. The key is "name" and the value is the formatted name of the guest.
        "name": name,
        "rsvp": rsvp
    })

    print(f"{name} added successfully.")


def modify_guest(old_name, new_name, new_rsvp):

    old_name = format_name(old_name)
    new_name = format_name(new_name)

    for guest in guests:
        if guest["name"] == old_name:
            guest["name"] = new_name
            guest["rsvp"] = new_rsvp
            print("Guest updated.")
            return

    print("Guest not found.")


def remove_guest(name):

    name = format_name(name)

    for guest in guests:
        if guest["name"] == name:
            guests.remove(guest)
            print("Guest removed.")
            return

    print("Guest not found.")


def sort_guests():
    # key=lambda g: g this means that the sorting will be based on the "name" key of each guest dictionary. The lambda function takes a guest dictionary as input and returns the value of the "name" key, which is used for sorting.
    guests.sort(key=lambda g: g["name"])
    print("Guests sorted alphabetically.")


def show_guest_list():

    print("\nGuest List")

    if not guests:
        print("No guests yet.")
        return

    # len means length, it counts the number of guests in the guests list and prints it.
    print(f"Total Guests: {len(guests)}")

    # i is index, guest is the guest dictionary, enumerate is a built-in function that adds a counter to an iterable and returns it as an enumerate object. start=1 means that the counter will start from 1 instead of 0. This allows us to display the guest list with numbers starting from 1.
    for i, guest in enumerate(guests, start=1):
        # in short- this line prints the index (i), the name of the guest (guest['name']), and their RSVP status (guest['rsvp']) in a formatted string. The output will look like "1. John Doe - Attending" for each guest in the list.
        print(f"{i}. {guest['name']} - {guest['rsvp']}")


def search_guest(name):

    name = format_name(name)

    for guest in guests:
        if guest["name"] == name:
            print(f"Found: {guest['name']} - {guest['rsvp']}")
            return

    print("Guest not found.")


def show_invitations():

    for guest in guests:
        print(f"Dear {guest['name']}, you are invited to dinner!")


def count_attending_guests():

    attending = 0

    for guest in guests:
        if guest["rsvp"] == "Attending":
            attending += 1

    total = len(guests)

    if total == 0:
        print("No guests yet.")
        return

    percentage = (attending / total) * 100

    print(f"Guests attending: {attending}")
    print(f"Attendance rate: {percentage:.2f}%")


def show_seating_plan():

    table_size = 3
    table = 1

    for i in range(0, len(guests), table_size):  # in short - this line creates a loop that iterates through the guests list in steps of table_size (which is 3). The range function generates a sequence of numbers starting from 0 up to the length of the guests list, with a step of table_size. This allows us to group guests into tables of 3. For example, if there are 10 guests, the loop will run with i values of 0, 3, 6, and 9, effectively creating groups of guests for each table.

        print(f"\nTable {table}")

        # this line creates a slice of the guests list from index i to i+table_size. This means it will take a group of guests for the current table. For example, if i is 0 and table_size is 3, it will take guests[0:3], which includes the first three guests. If i is 3, it will take guests[3:6], which includes the next three guests, and so on.
        table_guests = guests[i:i+table_size]

        for guest in table_guests:
            print(guest["name"])

        table += 1


def choose_rsvp():

    while True:

        print("\nRSVP Status:")
        print("1 Attending")
        print("2 Not Attending")
        print("3 Maybe")

        choice = input("Choose RSVP option: ").strip()

        if choice == "1":
            return "Attending"
        elif choice == "2":
            return "Not Attending"
        elif choice == "3":
            return "Maybe"
        else:
            print("Invalid option. Please enter 1, 2, or 3.")


def main():

    print("Welcome to the Guest Manager!")
    show_guest_list()  # NEW FEATURE: show list on startup

    while True:

        print("\nGuest Manager")
        print("1 Add Guest")
        print("2 Modify Guest")
        print("3 Remove Guest")
        print("4 Sort Guests")
        print("5 Show Guest List")
        print("6 Search Guest")
        print("7 Show Invitations")
        print("8 Count Attending Guests")
        print("9 Show Seating Plan")
        print("10 Exit")

        choice = input("Choose option: ").strip()

        if not choice.isdigit():
            print("Invalid input. Please enter a number from the menu.")
            continue

        if choice == "1":
            name = input("Enter name: ")
            rsvp = choose_rsvp()
            add_guest(name, rsvp)

        elif choice == "2":

            old_name = input("Enter the guest's current name: ")
            old_name = format_name(old_name)

            found = False

            for guest in guests:
                if guest["name"] == old_name:
                    found = True

            if not found:
                print("Guest not found.")
            else:
                new_name = input("Enter the new name: ")
                rsvp = choose_rsvp()
                modify_guest(old_name, new_name, rsvp)

        elif choice == "3":
            name = input("Enter name to remove: ")
            remove_guest(name)

        elif choice == "4":
            sort_guests()

        elif choice == "5":
            show_guest_list()

        elif choice == "6":
            name = input("Search guest: ")
            search_guest(name)

        elif choice == "7":
            show_invitations()

        elif choice == "8":
            count_attending_guests()

        elif choice == "9":
            show_seating_plan()

        elif choice == "10":
            break


# this line checks if the script is being run directly (as the main program) rather than imported as a module in another script. If this condition is true, it calls the main() function to start the program.
if __name__ == "__main__":
    main()

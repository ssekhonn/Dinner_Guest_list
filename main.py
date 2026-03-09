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


def add_guest(name, rsvp):

    name = format_name(name)

    if not name:
        print("Invalid name.")
        return

    for guest in guests:
        if guest["name"] == name:
            print("Guest already exists.")
            return

    guests.append({
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
    guests.sort(key=lambda g: g["name"])
    print("Guests sorted alphabetically.")


def show_guest_list():

    if not guests:
        print("No guests yet.")
        return

    for i, guest in enumerate(guests, start=1):
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

    count = 0

    for guest in guests:
        if guest["rsvp"] == "Attending":
            count += 1

    print(f"Guests attending: {count}")


def show_seating_plan():

    table_size = 3
    table = 1

    for i in range(0, len(guests), table_size):

        print(f"\nTable {table}")

        table_guests = guests[i:i+table_size]

        for guest in table_guests:
            print(guest["name"])

        table += 1


def choose_rsvp():

    print("1 Attending")
    print("2 Not Attending")
    print("3 Maybe")

    choice = input("Choose RSVP: ")

    if choice == "1":
        return "Attending"
    elif choice == "2":
        return "Not Attending"
    else:
        return "Maybe"


def main():

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

        choice = input("Choose option: ")

        if choice == "1":
            name = input("Enter name: ")
            rsvp = choose_rsvp()
            add_guest(name, rsvp)

        elif choice == "2":
            old_name = input("Current name: ")
            new_name = input("New name: ")
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


if __name__ == "__main__":
    main()

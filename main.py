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

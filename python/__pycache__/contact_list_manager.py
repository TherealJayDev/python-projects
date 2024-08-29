import os

CONTACTS_FILE = 'contacts.txt'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        for contact in contacts:
            file.write(contact + '\n')

def add_contact(contacts):
    name = input("Enter contact name: ")
    numbers = int(input("Enter contact phone number: "))
    contacts.append(f'{name} - {numbers}')
    save_contacts(contacts)
    print('Contact successfully added!')

def view_contact(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact}")

def delete_contact(contacts):
    view_contact(contacts)
    try:
    # Specify the line number to delete (0-indexed)  
        line_to_delete = int(input("select contact to delete by index number")) - 1  # for example, to delete the second line  
        if 0 <= line_to_delete < len(contacts):
            contacts.pop(line_to_delete)
            save_contacts(contacts)
            print('Contact successfully deleted')
        else:
            print("invalid index")
    except ValueError:
        print("invalid input. Please enter a valid number!")

def main():
    # load contacts
    contacts = load_contacts()
    while True:
        # load the prompts
        print("\nContact List Manager")
        print("1. Add contact")
        print("2. View contact")
        print("3. Delete Contact")
        print("4. Exit")

        user_input = input('Select an action from 1 - 4:')

        if user_input == '1':
            add_contact(contacts)
        elif user_input == '2':
            view_contact(contacts)
        elif user_input == '3':
            delete_contact(contacts)
        elif user_input == '4':
            print('You are exiting the Contact List Manager!')
            break 
        else:
            print('Select one of the available options')

if __name__ == "__main__":
    main()
        

        





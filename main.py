from utils.parser import parse_input
from commands.add import add_contact
from commands.change import change_contact
from commands.phone import show_phone
from commands.show_all import show_all
from commands.delete import delete_contact
from utils.storage import save_contacts, load_contacts
from models.address_book import AddressBook
from models.record import Record
from models.field import Name, Phone

def main():
    contacts = load_contacts(AddressBook())
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_contacts(contacts)
            print("Good bye! Contacts have been saved.")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "delete":
            print(delete_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

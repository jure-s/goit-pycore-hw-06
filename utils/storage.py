import json
import os
from models.record import Record
from models.field import Name, Phone

CONTACTS_FILE = "contacts/contacts.json"

def ensure_storage_directory():

    os.makedirs(os.path.dirname(CONTACTS_FILE), exist_ok=True)

def load_contacts(address_book):

    ensure_storage_directory()
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            try:
                data = json.load(file)
                for name, phones in data.items():
                    record = Record(Name(name))
                    for phone in phones:
                        try:
                            record.add_phone(Phone(phone))
                        except ValueError as e:
                            print(f"Skipping invalid phone for {name}: {phone} ({e})")
                    address_book.add_record(record)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from {CONTACTS_FILE}: {e}")
    return address_book

def save_contacts(address_book):

    ensure_storage_directory()
    with open(CONTACTS_FILE, "w") as file:
        json.dump(
            {name: [phone.value for phone in record.phones]
             for name, record in address_book.data.items()},
            file,
            indent=4
        )

from models.field import Name, Phone

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone_value):
        for phone in self.phones:
            if phone.value == phone_value:
                self.phones.remove(phone)
                return f"Phone {phone_value} removed."
        return f"Phone {phone_value} not found."

    def edit_phone(self, old_value, new_value):
        for phone in self.phones:
            if phone.value == old_value:
                phone.value = new_value
                return f"Phone {old_value} updated to {new_value}."
        return f"Phone {old_value} not found."

    def __str__(self):
        phones = "; ".join([phone.value for phone in self.phones])
        return f"Contact name: {self.name.value}, phones: {phones}"

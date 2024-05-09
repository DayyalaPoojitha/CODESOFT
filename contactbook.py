class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)
            print("")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                self.contacts[i] = new_contact
                return True
        return False

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[i]
                return True
        return False

def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    contact_book = ContactBook()
    while True:
        choice = display_menu()
        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully!\n")
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                for contact in found_contacts:
                    print(contact)
                    print("")
            else:
                print("No contacts found\n")
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            found_contacts = contact_book.search_contact(name)
            if found_contacts:
                new_name = input("Enter new name (leave blank to keep the same): ")
                new_phone_number = input("Enter new phone number (leave blank to keep the same): ")
                new_email = input("Enter new email (leave blank to keep the same): ")
                new_address = input("Enter new address (leave blank to keep the same): ")
                new_contact = Contact(new_name or found_contacts[0].name,
                                       new_phone_number or found_contacts[0].phone_number,
                                       new_email or found_contacts[0].email,
                                       new_address or found_contacts[0].address)
                if contact_book.update_contact(name, new_contact):
                    print("Contact updated successfully!\n")
                else:
                    print("Contact not found\n")
            else:
                print("Contact not found\n")
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            if contact_book.delete_contact(name):
                print("Contact deleted successfully!\n")
            else:
                print("Contact not found\n")
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

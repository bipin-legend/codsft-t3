class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

def print_menu():
    print("\nContact Management System Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def get_contact_details():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return Contact(name, phone_number, email, address)

def main():
    contact_book = ContactBook()
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            contact = get_contact_details()
            contact_book.add_contact(contact)
            print("Contact added successfully.")
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                print("Search Results:")
                for i, contact in enumerate(found_contacts, start=1):
                    print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            index = int(input("Enter the index of the contact to update: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                new_contact = get_contact_details()
                contact_book.update_contact(index, new_contact)
                print("Contact updated successfully.")
            else:
                print("Invalid index.")
        elif choice == '5':
            index = int(input("Enter the index of the contact to delete: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                contact_book.delete_contact(index)
                print("Contact deleted successfully.")
            else:
                print("Invalid index.")
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

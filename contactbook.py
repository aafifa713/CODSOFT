class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(self.contacts):
                print(f"{index + 1}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if not results:
            print("No matching contacts found.")
        else:
            for contact in results:
                print(contact)

    def update_contact(self, index, name=None, phone=None, email=None, address=None):
        if 0 <= index < len(self.contacts):
            if name:
                self.contacts[index].name = name
            if phone:
                self.contacts[index].phone = phone
            if email:
                self.contacts[index].email = email
            if address:
                self.contacts[index].address = address
        else:
            print("Invalid contact number.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
        else:
            print("Invalid contact number.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)
        elif choice == '4':
            index = int(input("Enter the contact number to update: ")) - 1
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            contact_book.update_contact(index, name or None, phone or None, email or None, address or None)
            print("Contact updated successfully.")
        elif choice == '5':
            index = int(input("Enter the contact number to delete: ")) - 1
            contact_book.delete_contact(index)
            print("Contact deleted successfully.")
        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

import pickle

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        self.contacts.append({
            "name" : name,
            "phone" : phone,
            "email" : email
        })    
    def list_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено


def main():
    book = load_data()
    
    book.add_contact("Ольга", "пошта@gmail.com", "(992) 914-3792")
    book.add_contact("Степан", "пошта2@gmail.com", "(294) 840-6685")

    book.list_contacts()


    save_data(book)  
if __name__ == "__main__" :
        main()
    

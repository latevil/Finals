import csv

def load_contacts(file_name):
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_contacts(contacts, file_name):
    fieldnames = ["name", "email", "phone"]
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contacts)
    except Exception as e:
        print(f"Failed to save contacts: {str(e)}")

import tkinter as tk
from tkinter import messagebox
import re
import csv_handler

class AddressBookGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Address Book")

        self.file_name = "contacts.csv"
        self.contacts = csv_handler.load_contacts(self.file_name)

        self.create_widgets()

    def add_contact(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email format")
            return

        if not re.match(r"^\d{10}$", phone):
            messagebox.showerror("Error", "Invalid phone number format (10 digits expected)")
            return

        if name and email and phone:
            # Check if a contact with the same name already exists
            existing_contact_names = [contact["name"] for contact in self.contacts]
            if name in existing_contact_names:
                messagebox.showerror("Error", "Contact with the same name already exists")
                return

            # If the name is unique, add the contact
            contact = {"name": name, "email": email, "phone": phone}
            self.contacts.append(contact)
            csv_handler.save_contacts(self.contacts, self.file_name)
            self.display_contacts()
            messagebox.showinfo("Success", "Contact added successfully")
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def search_contact(self):
        name = self.search_entry.get()
        found_contacts = [contact for contact in self.contacts if contact["name"] == name]
        if found_contacts:
            messagebox.showinfo("Search Result", f"Found {len(found_contacts)} contact(s):\n{found_contacts}")
        else:
            messagebox.showinfo("Search Result", "No contact found")

    def display_contacts(self):
        self.contacts_text.delete(1.0, tk.END)
        for contact in self.contacts:
            self.contacts_text.insert(tk.END, f"{contact['name']}: {contact['email']} - {contact['phone']}\n")

    def create_widgets(self):
        # Labels and entries for adding a contact
        tk.Label(self.master, text="Name:").grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.master, text="Email:").grid(row=1, column=0, sticky=tk.W)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=1, column=1)

        tk.Label(self.master, text="Phone:").grid(row=2, column=0, sticky=tk.W)
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=2, column=1)

        add_button = tk.Button(self.master, text="Add Contact", command=self.add_contact)
        add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Label and entry for searching a contact
        tk.Label(self.master, text="Search Name:").grid(row=4, column=0, sticky=tk.W)
        self.search_entry = tk.Entry(self.master)
        self.search_entry.grid(row=4, column=1)

        search_button = tk.Button(self.master, text="Search", command=self.search_contact)
        search_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Text area to display contacts
        self.contacts_text = tk.Text(self.master, height=10, width=50)
        self.contacts_text.grid(row=6, column=0, columnspan=2)

        # Disable editing in the result box
        self.contacts_text.config(state=tk.DISABLED)

        # Display existing contacts
        self.display_contacts()

# Create the main application window
root = tk.Tk()
app = AddressBookGUI(root)
root.mainloop()
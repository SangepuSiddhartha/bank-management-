import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self, account_holder, account_number, account_type, bank_name, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.account_type = account_type  # Account type (e.g., Savings, Checking, etc.)
        self.bank_name = bank_name  # Bank Name (e.g., SBI, Kotak, etc.)
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount}, New Balance: {self.balance}"
        else:
            return "Deposit amount must be greater than 0."

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return f"Withdrew: {amount}, New Balance: {self.balance}"
        elif amount <= 0:
            return "Withdrawal amount must be greater than 0."
        else:
            return "Insufficient funds."

    def check_balance(self):
        return f"Account Balance: {self.balance}"

    def display_account_details(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nAccount Type: {self.account_type}\nBank Name: {self.bank_name}\nBalance: {self.balance}"

class BankManagementSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, acc_number, account_type, bank_name):
        if acc_number in self.accounts:
            return "Account number already exists."
        else:
            self.accounts[acc_number] = BankAccount(name, acc_number, account_type, bank_name)
            return "Account created successfully!"

    def deposit_amount(self, acc_number, amount):
        if acc_number in self.accounts:
            return self.accounts[acc_number].deposit(amount)
        else:
            return "Account not found!"

    def withdraw_amount(self, acc_number, amount):
        if acc_number in self.accounts:
            return self.accounts[acc_number].withdraw(amount)
        else:
            return "Account not found!"

    def check_balance(self, acc_number):
        if acc_number in self.accounts:
            return self.accounts[acc_number].check_balance()
        else:
            return "Account not found!"

    def display_account_details(self, acc_number):
        if acc_number in self.accounts:
            return self.accounts[acc_number].display_account_details()
        else:
            return "Account not found!"

    def display_all_accounts(self):
        if len(self.accounts) == 0:
            return "No accounts found!"
        else:
            all_accounts_details = ""
            for acc in self.accounts.values():
                all_accounts_details += acc.display_account_details() + "\n\n"
            return all_accounts_details

class BankManagementGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bank_system = BankManagementSystem()
        self.title("Bank Management System")
        self.geometry("500x500")

        self.create_widgets()

    def create_widgets(self):
        # Label for instructions
        self.instruction_label = tk.Label(self, text="Welcome to the Bank Management System", font=("Arial", 14))
        self.instruction_label.pack(pady=10)

        # Dropdown menu for choosing actions
        self.option_var = tk.StringVar()
        self.option_var.set("Select an action")
        self.options = ["Create Account", "Deposit Amount", "Withdraw Amount", "Check Balance", "Display Account Details", "Display All Accounts"]
        self.option_menu = tk.OptionMenu(self, self.option_var, *self.options)
        self.option_menu.pack(pady=10)

        # Entry field for user input
        self.input_label = tk.Label(self, text="Enter details", font=("Arial", 10))
        self.input_label.pack()

        self.details_entry = tk.Entry(self, width=40)
        self.details_entry.pack(pady=10)

        # Button to perform selected action
        self.perform_button = tk.Button(self, text="Perform", command=self.perform_action)
        self.perform_button.pack(pady=10)

        # Text area for displaying results
        self.result_text = tk.Text(self, height=10, width=50)
        self.result_text.pack(pady=10)

    def perform_action(self):
        action = self.option_var.get()
        input_data = self.details_entry.get().split(",")  # expecting comma-separated values for actions

        self.result_text.delete(1.0, tk.END)  # Clear the previous result

        if action == "Create Account":
            if len(input_data) == 4:
                name, acc_number, account_type, bank_name = input_data
                result = self.bank_system.create_account(name.strip(), acc_number.strip(), account_type.strip(), bank_name.strip())
            else:
                result = "Please provide all details: Name, Account Number, Account Type, Bank Name"
        
        elif action == "Deposit Amount":
            if len(input_data) == 2:
                acc_number, amount = input_data
                try:
                    amount = float(amount.strip())
                    result = self.bank_system.deposit_amount(acc_number.strip(), amount)
                except ValueError:
                    result = "Invalid deposit amount"
            else:
                result = "Please provide both Account Number and Deposit Amount"

        elif action == "Withdraw Amount":
            if len(input_data) == 2:
                acc_number, amount = input_data
                try:
                    amount = float(amount.strip())
                    result = self.bank_system.withdraw_amount(acc_number.strip(), amount)
                except ValueError:
                    result = "Invalid withdrawal amount"
            else:
                result = "Please provide both Account Number and Withdrawal Amount"

        elif action == "Check Balance":
            if len(input_data) == 1:
                acc_number = input_data[0].strip()
                result = self.bank_system.check_balance(acc_number)
            else:
                result = "Please provide Account Number"

        elif action == "Display Account Details":
            if len(input_data) == 1:
                acc_number = input_data[0].strip()
                result = self.bank_system.display_account_details(acc_number)
            else:
                result = "Please provide Account Number"

        elif action == "Display All Accounts":
            result = self.bank_system.display_all_accounts()

        else:
            result = "Invalid action selected"

        self.result_text.insert(tk.END, result)

if __name__ == "__main__":
    app = BankManagementGUI()
    app.mainloop()

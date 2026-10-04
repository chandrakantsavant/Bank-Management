# Python OOP Bank Management System

A simple **command-line Bank Management System** built using **Core Python and Object-Oriented Programming (OOP)**.

The application manages bank accounts and stores account information in a local **JSON file**. Users can perform basic banking operations such as creating an account, updating account information, depositing money, withdrawing money, and closing an account.

> **Note:** This project is created for learning and educational purposes. It is not intended for real-world banking or financial use.

## Features

The application provides the following options:

1. **Create Account**

   * Create a new bank account.
   * Generate/store an account number.
   * Store customer information.
   * Store the initial account balance.

2. **Update Account Information**

   * Search for an existing account.
   * Update customer information.
   * Save the updated information to the JSON file.

3. **Deposit Money**

   * Search for an account.
   * Enter the amount to deposit.
   * Update the account balance.
   * Save the new balance.

4. **Withdraw Money**

   * Search for an account.
   * Enter the withdrawal amount.
   * Validate available balance.
   * Deduct the amount from the account.
   * Save the updated balance.

5. **Close Account**

   * Search for an account.
   * Confirm account closure.
   * Remove/deactivate the account.
   * Save the updated account data.

6. **Exit**

   * Close the application.

## Example Menu

```text
========================================
       PYTHON BANK MANAGEMENT SYSTEM
========================================

1. Create Account
2. Update Account
3. Deposit Money
4. Withdraw Money
5. Close Account
6. Exit

Enter your choice:
```

## Example Account Data

The account information will be stored in a JSON file such as `bank_data.json`.

Example:

```json
{
    "accounts": [
        {
            "account_number": "100001",
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "9876543210",
            "balance": 5000.0
        }
    ]
}
```

## Project Structure

```text
python-oop-bank-management/
│
├── main.py
├── bank.py
├── bank_data.json
├── README.md
└── .gitignore
```

### `main.py`

The entry point of the application.

Responsible for:

* Starting the application
* Displaying the menu
* Accepting user input
* Calling appropriate Bank Management methods

### `bank.py`

Contains the main classes and business logic.

Possible responsibilities include:

* Creating accounts
* Updating accounts
* Depositing money
* Withdrawing money
* Closing accounts
* Finding accounts
* Validating account information

### `bank_data.json`

Stores account information persistently.

The application reads from and writes to this file whenever account information changes.

## OOP Concepts Practiced

This project is designed to practice the following Python concepts:

* Classes
* Objects
* Constructors
* Instance methods
* Encapsulation
* `self`
* Class attributes
* Conditional statements
* Loops
* Functions
* Exception handling
* Input validation
* JSON handling
* File handling
* CRUD operations

## Python Modules

The project uses Core Python and does not require external packages.

Expected modules:

```python
json
os
```

Additional standard-library modules can be introduced as the project evolves.

## Data Storage

Account information is stored locally in:

```text
bank_data.json
```

The application will:

```text
Application
     │
     ▼
Read JSON
     │
     ▼
Perform Operation
     │
     ├── Create Account
     ├── Update Account
     ├── Deposit
     ├── Withdraw
     └── Close Account
     │
     ▼
Write Updated JSON
```

## Validation

The application should validate important inputs before performing operations.

Examples:

### Account

* Account number must exist before updating, depositing, withdrawing, or closing.
* Account number should be unique.

### Deposit

* Amount must be greater than zero.
* Amount should be a valid number.

### Withdrawal

* Amount must be greater than zero.
* Withdrawal amount must not exceed the available balance.

### Account Creation

* Customer name should not be empty.
* Email should be validated.
* Phone number should be validated.
* Initial deposit should not be negative.

## Example Workflow

### 1. Create Account

```text
Enter your choice: 1

Enter customer name: John Doe
Enter email: john@example.com
Enter phone: 9876543210
Enter initial deposit: 5000

Account created successfully!

Account Number: 100001
Current Balance: 5000.00
```

### 2. Deposit Money

```text
Enter your choice: 3

Enter account number: 100001
Enter amount to deposit: 2000

Deposit successful!

Current Balance: 7000.00
```

### 3. Withdraw Money

```text
Enter your choice: 4

Enter account number: 100001
Enter amount to withdraw: 1500

Withdrawal successful!

Current Balance: 5500.00
```

### 4. Close Account

```text
Enter your choice: 5

Enter account number: 100001

Are you sure you want to close this account? (yes/no): yes

Account closed successfully.
```

## How to Run

Make sure Python 3 is installed:

```bash
python --version
```

Clone the repository:

```bash
git clone https://github.com/<your-username>/python-oop-bank-management.git
```

Move into the project directory:

```bash
cd python-oop-bank-management
```

Run the application:

```bash
python main.py
```

## Future Improvements

Once the basic version is working, the project can be extended with:

* Account transaction history
* Mini statement
* Transfer money between accounts
* Account balance enquiry
* Customer login
* PIN/password authentication
* Transaction timestamps
* Transaction IDs
* Interest calculation
* Multiple account types

  * Savings Account
  * Current Account
* Transaction limits
* Daily withdrawal limits
* Search customer
* Display all accounts
* Export transaction history
* Unit testing
* Logging
* Better CLI interface

## Learning Objectives

The primary goal of this project is to understand how **Object-Oriented Programming and JSON-based persistence** can be used to build a small real-world-style application.

The project demonstrates the flow:

```text
User Input
    ↓
Menu
    ↓
Bank Management Class
    ↓
Validation
    ↓
Business Logic
    ↓
JSON File
    ↓
Updated Data
```

## Disclaimer

This project is intended strictly for **educational and practice purposes**.

It does not implement the security, compliance, encryption, authentication, auditing, concurrency controls, or financial safeguards required by a real banking application.

## Author

**Chandrakant Savant**

Learning Core Python, Object-Oriented Programming, and Python backend development.

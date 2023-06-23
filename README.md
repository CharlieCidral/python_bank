###Console Banking System
This is a simple console-based banking system implemented in Python. It provides a set of functionalities for managing bank accounts, performing transactions, and accessing account information. The system supports the following features:

Deposit funds
Withdraw funds
Transfer funds to another account
View account information
Generate account statements
View balance history
Update personal information
Password protection
Error handling for invalid operations

###Getting Started
To run the banking system, make sure you have Python installed on your machine. Clone this repository and navigate to the project directory.

####shell
```git clone https://github.com/your_username/banking-system.git
    cd banking-system```

###Usage
Run the Python script to start the console-based banking system.

####shell
```python bank.py```

The system will present a menu with different options. Select the desired operation by entering the corresponding letter. Follow the prompts and provide the required information to perform transactions, view account details, or update personal information.

###User Accounts
The banking system utilizes a user_accounts data structure to store account information. The structure is defined as follows:

###python
```
user_accounts = {
    "user1": {
        "senha": "password1",
        "saldo": 1000.0,
        "extrato": "",
        "historico_saldo": [],
        "nome": "João da Silva",
        "numero_conta": "123456789",
        "contato": "joao.silva@email.com",
        "type": "admin"  # Type of account
    },
    "user2": {
        "senha": "password2",
        "saldo": 500.0,
        "extrato": "",
        "historico_saldo": [],
        "nome": "Maria Oliveira",
        "numero_conta": "987654321",
        "contato": "maria.oliveira@email.com",
        "type": "regular"  # Type of account
    },
    # Add more user accounts as needed
}
```
Feel free to modify the user accounts data structure to add or update account information.

###Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a pull request or submit an issue.

###License
This project is licensed under the MIT License.

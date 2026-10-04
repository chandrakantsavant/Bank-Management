from pathlib import Path
import json
class Bank:
    data = []
    filePath = Path('bankData.json')
    try:
        if filePath.exists():
            with open(filePath) as fs:
                data = json.loads(fs.read())
        else:
            print("File was not exist. Created a new file")
            open('bankData.json', 'w')
    except Exception as err:
        print(f"An Error occured -- {err}")

    @classmethod
    def __update(cls):
        with open(cls.filePath, 'w') as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def __generateAccountNo(cls):
        pass

    def createAccount(self):
        info = {
            "name": input("Enter your name:- "),
            "age": int(input("Enter your age:- ")),
            "email": input("Enter your email:- "),
            "pin": int(input("Enter your pin:- ")),
            "account_no": 1234,
            "balance": 0
        }

        if info['age'] < 18 or len((str(info['pin']))) < 4:
            print("Your age is not acceptable or pin code is incorrect")
        else:
            Bank.data.append(info)
            Bank.__update()
            print("Your account has been created successfully")
            print("Please check your account info below and note down the account number---")
            for i in info:
                print(f"{i}: {info[i]}")


    
user = Bank()
print("Please provide your input from below options-")
print("1. Create Account")
print("2. Update Account")

userChoice = int(input("Enter your choice--"))
if userChoice == 1:
    user.createAccount()
elif userChoice == 2:
    pass
else: print("The selected option is not available")


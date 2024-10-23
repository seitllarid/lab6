#Respo created by Dajana Seitllari


def encode(password):
    encoded_password= ""
    for number in str(password):
        encoded_password += str(int(number)+3)
    return encoded_password

def main_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    option= int(input("Please enter an option:"))
    return option

password_storage=""

while True:
    choice=main_menu()
    if choice ==1:
        while True:
            try:
                password_input= input("Please enter your password: :")
                password_input=int(password_input)
            except:
                print("Please enter only numbers for your password")
            if len(str(password_input)) !=8:
                print("Password must be 8 characters long!")
            elif type(password_input)==int:
                break
        password_storage=encode(password_input)
        print("Your password had been encoded and stored!\n")
    elif choice ==2:
        #TODO choice 2
        pass
    elif choice ==3:
        break




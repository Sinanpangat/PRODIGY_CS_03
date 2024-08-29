import string
def check(password): #function for check password complexity
  if len(password) < 8:
    print("\n! Password too short")

  has_uppercase = False
  has_lowercase = False
  has_digit = False
  has_special_char = False
  
  for char in password:
     if char.isupper():
        has_uppercase = True
     elif char.islower():
        has_lowercase = True
     elif char.isdigit():
        has_digit = True
     elif not char.isalnum():
        has_special_char = True
  if not (has_uppercase and has_lowercase and has_digit and has_special_char):
     print("\n! Password weak ,lack of characters\n\n  For Better password mix digits,uppercase,lowercase,special characters")

  # Additional checks for common patterns can be added here
  else:
     print("\nPassword is strong")


choise=input("\ncheck password complexity \n       --------\nEnter 1 to Continue \nEnter 0 for exit\n")
if choise == '1':
   password=input("Enter the password :")
   check(password)
else:
   exit

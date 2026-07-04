import random
import string

print("====================================")
print("      SIMPLE PASSWORD GENERATOR")
print("====================================")

length = int(input("Enter the password length: "))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

password = ""

for i in range(length):
    random_character = random.choice(all_characters)
    password = password + random_character

print("\nGenerating Password...")

print("\nYour Generated Password is:")
print(password)

print("\nPassword Length:", len(password))

if length < 6:
    print("Password Strength: Weak")
elif length >= 6 and length <= 10:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

choice = input("\nDo you want to generate another password? (yes/no): ")

while choice.lower() == "yes":

    length = int(input("\nEnter the password length: "))

    password = ""

    for i in range(length):
        random_character = random.choice(all_characters)
        password = password + random_character

    print("\nGenerated Password:", password)
    print("Password Length:", len(password))

    if length < 6:
        print("Password Strength: Weak")
    elif length >= 6 and length <= 10:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Strong")

    choice = input("\nGenerate another password? (yes/no): ")

print("\nThank you for using the Password Generator!")

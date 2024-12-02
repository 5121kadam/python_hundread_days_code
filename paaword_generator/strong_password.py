import random
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!@#$%^&*()_+-=[]{}|;:',.<>?/`~")

print("Welcome to the Pypassword generator")
nr_letters = int(input("How many letters would you like in you password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

lenght_of_password = nr_letters+nr_numbers+nr_symbols
password_generator = []
for i in range(0,nr_letters):
    password_generator.append(random.choice(letters))
for i in range(0,nr_numbers):
    password_generator.append(random.choice(numbers))
for i in range(0,nr_symbols):
    password_generator.append(random.choice(symbols))

random.shuffle(password_generator)

'''password = ""
for char in password_generator:
    password += char'''

print(f"your strong password is {''.join(password_generator)}")

#print(f"your strong password is {password}")


print("<<<<< Exercise 5-8 >>>>>")
usernames = ["Admin","Beth","Charlie","Daisy","Ed"]
for name in usernames:
    if name == "Admin":
        print(f"Hello, how are you today, {name}?")
    else:
        print(f"Thank you for logging in, {name}.")

print("\n<<<<< Exercise 5-9 >>>>>")
usernames = []
if usernames:
    for name in usernames:
        if name == "Admin":
            print(f"Hello, how are you today, {name}?")
        else:
            print(f"Thank you for logging in, {name}.")
else:
    print("We need to get some users!")

print("\n<<<<< Exercise 5-10 >>>>>")
current_users = ["Admin","Beth","Charlie","Daisy","Ed"]
new_users = ["Admin", "Bernard", "Cecil", "Daisy", "Eloise"]

lower_current_users=[]
for user in current_users:
    lower_current_users.append(user.lower())

lower_new_users=[]
for user in new_users:
    lower_new_users.append(user.lower())

for user in lower_new_users:
    if user in lower_current_users:
        print(f"Please select a different name, \"{user.title()}\" is already taken.")
    else:
        print(f"Welcome, {user.title()}!")
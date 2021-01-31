print("\n<<<<< Hands on #3: 7-8 >>>>>")
orders = ["grilled cheese","turkey","pulled pork","manwich","tuna","bologna","pastrami"]
finished = []

while orders:
    current = orders.pop()
    print(f"I have made your {current} sandwich.")
    finished.append(current)

print("\nSandwiches I have compelted: ")
for s in finished:
    print(s.title())


print("\n<<<<< Hands on #3: 7-9 >>>>>")
orders = ["grilled cheese","turkey","pulled pork","manwich","tuna","bologna","pastrami","pastrami","pastrami"]
finished = []

print("I am sorry, we are out of pastrami.\n")
while "pastrami" in orders:
    orders.remove("pastrami")

while orders:
    current = orders.pop()
    print(f"I have made your {current} sandwich.")
    finished.append(current)

print("\nSandwiches I have compelted: ")
for s in finished:
    print(s.title())
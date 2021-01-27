print("------------------ Exercise 3-4 ------------------")
guests = ["Nikola Tesla", "Leornardo Da Vinci", "Immanuel Kant"]

print(guests[0],", would you be able to come to dinner Saturday?")
print(guests[1],", would you be able to come to dinner Saturday?")
print(guests[2],", would you be able to come to dinner Saturday?")

print("------------------ Exercise 3-5 ------------------")
print(guests[2],", I am sorry you cannot make it to dinner Saturday.")
guests[2] = "Socrates"

print(guests[0],", would you be able to come to dinner Saturday?")
print(guests[1],", would you be able to come to dinner Saturday?")
print(guests[2],", would you be able to come to dinner Saturday?")

print("------------------ Exercise 3-6 ------------------")
print("Great news! I found a bigger table! We can have more guests!")
guests.insert(0,"Isaac Asimov")
guests.insert(2,"William Shakespeare")
guests.append("Abraham Lincoln")

print(guests[0],", would you be able to come to dinner Saturday?")
print(guests[1],", would you be able to come to dinner Saturday?")
print(guests[2],", would you be able to come to dinner Saturday?")
print(guests[3],", would you be able to come to dinner Saturday?")
print(guests[4],", would you be able to come to dinner Saturday?")
print(guests[5],", would you be able to come to dinner Saturday?")
print(guests)

print("------------------ Exercise 3-7 ------------------")
print("I just realized I only have three chairs, so I can only invite two guests, Oops!")
print(guests[0],", I'm sorry, you are not invited.")
print(guests[2],", I'm sorry, you are not invited.")
print(guests[4],", I'm sorry, you are not invited.")
print(guests[5],", I'm sorry, you are not invited.")
guests.pop(0)
guests.pop(1)
guests.pop(2)
guests.pop(2)
print(guests[0],", you are still invited to dinner Saturday.")
print(guests[1],", you are still invited to dinner Saturday.")
del guests[0]
del guests[0]
print(guests)

print("------------------ Exercise 3-9 ------------------")
guests = ["Isaac Asimov", "Nikola Tesla", "William Shakespeare", "Leornardo Da Vinci", "Socrates", "Abraham Lincoln"]
print("I am inviting", len(guests), "guests to dinner in Exercise 3-6")


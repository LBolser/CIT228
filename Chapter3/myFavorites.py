foods = ["Pizza","Pasta","Green Beans","Sushi","Grilled Cheese","Snow Crab"]
numbers = [3,7,13,27,123,999]
movies  = ["Spirit, Stallion of the Cimmaron","Blazing Saddles","Princess Bride"]
combo = ["Sushi","Pasta",3,7,"Blazing Saddles","Princess Bride"]


print("------------------ Hands On #1 ------------------")
print(foods)
print(numbers)
print(movies)
print(combo)

print(foods[-1])
print("2nd = ", numbers[1])
print("4th = ", numbers[3])
print("6th = ", numbers[5])

print("1st Movie = ",movies[0])
print("2nd Movie = ",movies[1])
print("3rd Movie = ",movies[2])

print("First food, First number, First movie = ", combo[0], combo[2], combo[4])

print(" ")
print("------------------ Hands On #2 ------------------")
movies.append("Airplane")
print("Movie added to end: ",movies)

numbers.insert(3,42)
print("Number added to position 3: ",numbers)

foods.insert(5, "PBJ")
print("Food added to position 5: ",foods)

numbers.pop()
print("Number deleted from the end: ",numbers)

numbers.pop(2)
print("Deleted subscript 2: ",numbers)

print(" ")
print("------------------ Hands On #3 ------------------")

movies.sort()
print("Sorted List: ",movies)

foods.sort()
print("Sorted List: ",foods)

print("Temp Sorted List: ",sorted(numbers))
print("Original Sorted List: ",numbers)

movies.reverse()
print("List orted in Reverse Order: ",movies)
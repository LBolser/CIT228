
print("------------------ Exercise 3-10 ------------------")
bigCats = ["Tiger", "Jaguar", "Cougar", "Leopard", "Cheetah", "Snow Leopard", "Lynx", "House Cat", "Serval", "Mountain Lion"]
print("Original List:",bigCats)
bigCats.append("Clouded Leopard")
print("With Append:",bigCats)
bigCats.insert(1,"Lion")
print("With Insert:",bigCats)
del bigCats[8]
print("With Delete:",bigCats)
bigCats.pop(8)
print("With Pop:",bigCats)
bigCats.remove("Mountain Lion")
print("With Remove:",bigCats)
print("With Sorted: ", sorted(bigCats))
bigCats.reverse()
print("With Reverse:",bigCats)
bigCats.sort()
print(f"With Sort and f-string: {bigCats}")
print("The final length is", len(bigCats),"in the list.")

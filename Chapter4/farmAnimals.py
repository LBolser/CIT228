farm = ["horse","mule","donkey","chicken","rabbit","barn cat"]
farm2 = farm[:]
farm2.append("duck")
farm2.append("llama")
farm2.append("goat")
farm2.append("sheep")
print("-----farm-----")
for item in farm:
    print(f"{item}")
print("-----farm2-----")
for item in farm2:
    print(f"{item}")
print("----- 4-10 -----")
print("The first three items are: ", farm2[:3])
print("The items from the middle are: ", farm2[3:7])
print("The last three items are: ", farm2[7:10])
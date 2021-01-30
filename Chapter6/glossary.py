print("\n<<<<< Hands on #1, 6-3 >>>>>")
glossary={
    "Dictionary":"Python datatype that stores value pairs.",
    "Tuple":"List of items that do not change.",
    "String":"A series of characters inside quotes.",
    "Range":"Displays a sequence of number, must include a stopping number, may include a starting number and a step amount.",
    "List":"A function that creates a collection which is ordered and changeable. ",
}
print("Dictionary - ",glossary["Dictionary"])
print("Tuple - ",glossary["Tuple"])
print("String - ",glossary["String"])
print("Range - ",glossary["Range"])
print("List - ",glossary["List"])


print("\n<<<<< Hands on #2, 6-4 >>>>>")
glossary={
    "Dictionary":"Python datatype that stores value pairs.",
    "Tuple":"List of items that do not change.",
    "String":"A series of characters inside quotes.",
    "Range":"Displays a sequence of number, must include a stopping number, may include a starting number and a step amount.",
    "List":"A function that creates a collection which is ordered and changeable. ",
    "Key":"A Value used to access data stored in the dictionary",
    "Operators":"Used in conditions such as ==, !=, <=, >=, <, >",
    "Boolean":"Variables that can only be true or false.",
    "Comments":"Lines that begin with # that aren't part of the code.",
    "elif":"Python's take on if/else",
}
for k,v in glossary.items():
    print(k.title(), "-", v)
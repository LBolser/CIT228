print("\n<<<<< Hands on #3.2 >>>>>")

rivers={
    "Nile":["Tanzania", "Uganda", "Rwanda", "Burundi", "the Democratic Republic of the Congo", "Kenya", "Ethiopia", "Eritrea", "South Sudan", "Sudan", "Egypt"],
    "Amazon":["Brazil", "Peru", "Bolivia", "Colombia", "Ecuador", "Venezuela", "Guyana"],
    "Yangtze":"China",
}

for k,value in rivers.items():
    if type(value)==list:
        print(f"\nThe {k} river flows through: ")
        for v in value:
            print("\t -", v)
    else:
        print(f"\nThe {k} river flows through:\n \t -{value}")
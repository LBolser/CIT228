rivers={
    "Nile":["Tanzania", "Uganda", "Rwanda", "Burundi", "the Democratic Republic of the Congo", "Kenya", "Ethiopia", "Eritrea", "South Sudan", "Sudan", "Egypt"],
    "Amazon":["Brazil", "Peru", "Bolivia", "Colombia", "Ecuador", "Venezuela", "Guyana"],
    "Yangtze":"China",
}
print("\n<<<<< Rivers & Countries >>>>>")
for k,v in rivers.items():
    print(f"the {k} river flows through {v}.")

print("\n<<<<< Rivers >>>>>")
for k in rivers.items():
    print(k)

print("\n<<<<< Countries >>>>>")
for v in rivers.items():
    print(v)

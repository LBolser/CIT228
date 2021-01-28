buffet = ("eggs","bacon","pancakes","hashbrowns","toast")
print("<<<<<< Buffett >>>>>")
for item in buffet:
    print(f"{item}")
#buffet[0] = "omlette"

print("\n <<<<<< New Buffett >>>>>")
buffet = ("omlette","bacon","pancakes","hashbrowns","toast")
for item in buffet:
    print(item)
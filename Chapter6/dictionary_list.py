print("\n<<<<< Hands on #3.1 >>>>>")
kitchen={
    "Table":"Oak",
    "Sink":"Stainless Steel",
    "Microwave":"Over Stove",
    "Dishwaer":"None",
}
living={
    "Couch":"Three Seater",
    "Ottoman":"Oversized",
    "Television":"Yes",
    "Cat Tree":"Well Worn",
}
bathroom={
    "Bathtub":"Yes",
    "Separate Shower":"No",
    "Mirrored Cabinet":"No",
    "Closet":"Yes",
}

house = [kitchen,living,bathroom]
for h in house:
    print(h)
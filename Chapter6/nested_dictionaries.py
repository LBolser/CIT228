users = {
    "emc2": {
        "First":"Albert",
        "Last":"Einstein",
        "Born":"1879",
    },
    "meow": {
        "First":"Erwin",
        "Last":"Schrodinger",
        "Born":"1887",
    },
    "dogdrool":{
        "First":"Ivan",
        "Last":"Pavlov",
        "Born":"1849",
    },
}

for key,value in users.items():
    print(f"\nUsername: {key}")
    for k,v in value.items():
        print(k,":",v)
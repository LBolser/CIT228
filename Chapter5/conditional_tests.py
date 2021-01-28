color = "Lime green"
number1 = 3
number2 =  8
cats = ["Lion","Tiger","Jaguar","Cheetah"]

print("<<<<< True Results >>>>>")
print(number1,"<", number2,"--", number1<number2)
print(number1,"<=", number2,"--", number1<=number2)
print(number1, "+", number2, "= 11","--", number1+number2==11)
print(number1, "-", number2, "= -5","--", number1-number2==-5)
print(number1, "*", number2, "= 24","--", number1*number2==24)
print(f"Is {number1} or {number2} > 5 --",number1>5 or number2>5)
print(color, "= Lime green","--", color=="Lime green")
print(color.lower(), "!= Lime green","--", color.lower()!="Lime green")
if "Tiger" in cats:
    print("Tiger is in cats list.")
else:
    print("Tiger is not in cats list.")

print("\n<<<<< False Results >>>>>")
print(number1,">", number2,"--", number1>number2)
print(number1,">=", number2,"--", number1>=number2)
print(number1, "+", number2, "= 12","--", number1+number2==12)
print(number1, "-", number2, "= -3","--", number1-number2==-3)
print(number1, "*", number2, "= 16","--", number1*number2==16)
print(f"Is {number1} and {number2} > 5 --",number1>5 and number2>5)
print(color, "= Cherry red","--", color=="Cherry red")
print(color.lower(), "= Lime green","--", color.lower()=="Lime green")
if "Tiger" not in cats:
    print("Tiger is not in cats list.")
else:
    print("Tiger is in cats list.")


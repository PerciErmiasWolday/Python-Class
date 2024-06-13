# import random
#
# x=random.randrange(1,6)
# print(x)
#
# y=" hfherh , frhSDSDD  ,r h!"
#
# z=y.strip()
# print(z.upper())
#
# print(y.strip().upper().split('h'))

# price = 59.5764
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# txt = "We a\re the so-call\ted  fro\bm the north."
# print(txt)
# print(bool(''))
# x=5
# y=4
#
# print(not((x<6) and (y>7)))
#
# thislist = ["apple", "banana", "cherry"]


# print(len(thislist))
#
# print(type(thislist))


# thislist = ["apple", "banana", "cherry"]
# thislist[0] = "blackcurrant"
# print(thislist)
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:4] = ["blackcurrant", "watermelon"]
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(0, "watermelon")
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
tropical.extend(thislist)
print(tropical)
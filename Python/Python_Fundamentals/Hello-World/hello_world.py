#1 

print("Hello World")

#2

name = "Ali"
print("My name is "+ name + "!")
print("My name is", name + "!")

#3

num = 7
print("Hello", num)
#In order to concatenate a string with number we need to change the data type for one value, eather change the number to string or versa
print("Hello" + " " +str(num))

#4

fav_food1 = "Sushi"
fav_food2 = "Pizza"

print("I love to eat {} and {}".format(fav_food1, fav_food2))
print(f"I love to eat {fav_food1} and {fav_food2}")

#NINJA BONUS

name = "Alli"
print(name.upper())

info = "I am full-stack trainee in AXSOS Academy"
print(info.count("a"))
print(info.split())
print(info.split(" in "))
print(info.isalnum())

info1 = "IamfullstacktraineeinAXSOSAcademy"
print(info1.isalnum())

infos = info.split()
print(infos)
print(" ".join(infos))
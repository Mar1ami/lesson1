my_name= "Mari"
my_surname="lomidze"
my_age=20
my_height=170
my_weight=53
my_sentence="aa {1} bb {0} cc {3} dd {4} ee{2}".format(my_name,my_surname,my_age,my_height,my_weight)
print(my_sentence)
my_name=input("enter your name:")
print(my_name)
age=23
age-=3
print("age")
float=135.3
new_age=28
new_height=167.2
new_weight=57.5
print(new_age + int(float) + int(new_height) + (new_weight))
#თუ ნამრავლი მეტია 133-ზე ნიშნავს მოგებას
num1= int(input("enter num1: "))
num2= int(input("enter num2: "))
product=num1 * num2
if product > 133:
    print(product)
else:
    print("you lose")

my_name="Mariam"
my_surname="lomidze"
my_age=20
my_height=168
my_weight=52
my_sentence="aa {1} bb {0} cc {3} dd {4} ee {2}".format(my_name, my_surname, my_age, my_height, my_weight)
print(my_sentence)
my_name=input("enter your name: ")
print(my_name)
age = 23
age -= 3
print("age")
float=127.8
new_age=26
new_height=171.3
new_weight=57.5
print(new_age + int(float) + int(new_height) + int(new_weight))

# თუ ნამრავლი ნაკლებია 117-ზე ნიშნავს წაგებას
num1= int(input("enter num1: "))
num2= int(input("enter num2: "))
product= num1 * num2
if product > 117:
    print(product)
else:
    print("you lose")
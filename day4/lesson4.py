#მომხმარებელს შემოატანინე ორი სახელი და ის დაპრინტე რომელშიც მეტი თანხმოვანი იქნება
#(დააფორმატეთ პასუხი ლამაზად)
name1=input("enter name1: ")
name2=input("enter name2: ")
#შევქმენი ორი საინკრემენტაციო ცვლადი
ammount_of_consonants_in_name1 = 0
ammount_of_consonants_in_name2 = 0
for char in name1:
    if char in "bcdfghjklmnpqrvxwz":
        ammount_of_consonants_in_name1 += 1
        
          
for char in name2:
    if char in "bcdfghjklmnpqrvxwz":
        ammount_of_consonants_in_name2 += 1
        
if ammount_of_consonants_in_name1 >= ammount_of_consonants_in_name2:
     print("the ammount of consonants in name1 is more and it contains {} consonants".format
  (ammount_of_consonants_in_name1))
     
#sum
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))

my_sum=0
15,17,7
if num1 % 2 == 1:
    my_sum += num1
if num2 % 2 == 1:
    my_sum += num2
if num3 % 2 == 1:
    my_sum += num3

print("the sum of odd numbers is {}".format(my_sum))


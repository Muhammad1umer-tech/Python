# from exercises.bigger_guy import bigger_guy
from exercises.bigger_guy import bigger_guy
#1--
# for comment ctrl + /

#print("Hello");

#variable
#name = "Rafeh Qazi";

#print(name);
#python is snake casing . small letter with _

#width, height = 100, 200;

# concatinate
# name = input("Please enter your Name")  --> this is string.
# print(name)
# print("Hi", name)

# a = int(input("num: "))

#tip calculator

# amount = int(input("Enter Food Amount "))
# tip = .20
# amount = amount + (amount * .20)
# print("Total Amount ", str(amount))

#20/100 -> 0.2.
#20//100 -> 0.
## 2**4 = 16. power


def say_my_name():
    name = "MY NAME"
    print(name)


# say_my_name()


def say_my_name_2(name):
    print(name)


#say_my_name_2("M umer")


# multiple arguments
def greeting(greet, name):
    print(f"{greet} {name}")


# greeting("Aloha","Umer");


def food_Calculator(foodamount, tip=.20):
    total = foodamount + (foodamount * tip)
    return total


#print(food_Calculator(100, .30))

#print(bigger_guy(4,3));

#4----------------------
#lambda -> allows to create and anonyms function

# implecet return -> automatically return
# sum2: int = lambda a,b: a+b
#print(sum2);

# sum3: int = lambda: a,b,c:
#   sum = a+b;
#   sum*=c;
#   return sum;


# 5------------
# testing
def sum(a: int, b: int):
    return a + b


assert sum(2, 1) == 3, "write for debug..."

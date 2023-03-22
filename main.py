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

# print("huh")

#list

fruit = ['cake', 'pear', 'banana', 'banana']
#list has no problem with specific datatype. ['cake', 'pear','banana', 'banana', 1,2,3.5, [4,3] ]

# print(fruit)

#method fruit.append()
#['cake', 'pear','banana', 'banana']
#0 1 2 3 4 ->  ,  <- -4 -3 -2 -1

# slicing
# to access only specific use fruirts[0:2];
#to get length len(fruits)
#reverse the array.
#fruits[::-1]

#fruits[0:5:1]
#      from : till : step by (a++, a+=2, a+=2).

# appendm insert, clear, index, count, remove, sort, pop, reversed

#7 dictionary. is like map


def introducer():
    person = {
        'name': 'Qazi',
        'shirt': 'black',
        'laptop': 'apple',
      'phone number' : "0310301313",
        'assets': 100,
        'debt': 50,
        'favorite_fruits': ['banana', 'apple'],
        'networth': lambda: person['assets'] - person['debt']
    }
    print(
        f"Hi, my name is {person['name']}, Hi, a shirt that i am wearing is {person['shirt']}, my favorites fruits are {person['favorite_fruits'][0]} , and my networth is {person['networth']()}"
    )


#introducer()

#method 
person = {
        'name': 'Qazi',
        'shirt': 'black',
        'laptop': 'apple',
      'phone number' : "0310301313",
        'assets': 100,
        'debt': 50,
        'favorite_fruits': ['banana', 'apple'],
        'networth': lambda: person['assets'] - person['debt']
    }
person['assets']=1000
# print(person.values());
  #dictionary is ordered

#list and dictionary are mutable (Can change them).
#touples are unmutables.


#8---------------> touples

numbers = (1,2);
# print(numbers)

#9--------------> sets{} used for unique elements

programming_lan1 = ['ruby','javascript','python','react']
programming_lan2 = ['ruby','javascript','python','c++']

programming_lan = set(programming_lan1 + programming_lan2)




# print(programming_lan)

# ruby in programming_lan.

def unique(arr: list)->list: 
  arr = set(arr);
  return list(arr)

arr = ['ruby', 'python', 'python'];


ar = lambda arr: list(set(arr));


# print(ar)



# for a in programming_lan:
#   print(a)  

def double_fun(num: list)->list:
  counter = 0;
  while counter<len(num):
    num[counter] = (num[counter] + num[counter])
    counter+=1
  return num


#arr = double_fun([1,2,3,4])
#print(arr);

# def countwords(arr: str)->int:
#   n = len(arr)
#   i = 0;
#   sp = 0;
#   while i < n:
#     if i!=0 and i!=n-1:
#       if arr[i] == ' ':
#         sp+=1;
#     i+=1
#   return sp
# arr = "HI MY NAME IS M UMER"
# print("Total Spaces", countwords(arr))

def word_frequency(arr: str)->dict :
  di = {}
  i=0;
  n = len(arr)
  while i < n :
    if arr[i] not in di.keys():
      di[arr[i]]=1
    else:
      di[arr[i]]+=1
    i+=1
    
  return di;

print(word_frequency("I LOVE BATMAN BECAUSE I AM BATMAN"))

"""
def maximum():
    numbers=[]
    x=1
    for i in range(3):
        b=input("Enter number "+ str(i+1) +": ")
        numbers.append(int(b))
        if numbers[i]>x:
            x=numbers[i]
    return x
print("The Maximum number is",maximum())



"""

'''
def sum(rangex):
    numbers=[]
    x=0
    for i in range(int(rangex)):
        b = input("Enter number " + str(i + 1) + " of the list: ")
        numbers.append(int(b))
        x=numbers[i]+x
    return x

print("The sum of all numbers in the list is",sum(5))

'''

'''

def mul(rangex):
    sample=[]
    x=1
    for i in range(int(rangex)):
        b = input("Enter number " + str(i + 1) + " of the list: ")
        sample.append(int(b))
        x=sample[i]*x
    return x
print("The multiplication of all  numbers of the list is",mul(5))

'''

'''

def rev(sstring):
    rev = ''
    index = len(sstring)
    while index:
        index -= 1
        rev += sstring[index]
    return rev
print("Reverse of entered string is: ",rev(input("Enter a string: ")))


'''
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input("Enter a number for factorial: "))))

'''

'''
def test(n):
    if n in range(5,40):
        print( "Number " + str(n) + " is in the range")
    else :
        print("The number is outside the given range.")
test(25)



'''


'''

def calculate(sstr):
    upper=0
    lower=0
    for c in sstr:
            if c.isupper():
                upper=upper+1
            elif c.islower():
                lower=lower+1
    print("No. of Upper case characters :"+ str(upper))
    print("No. of Lower case Characters : "+ str(lower))

calculate(input("Enter a string: "))

'''


'''
def unique(List):
    unique = []
    for element in List:
        if element not in unique:
            unique.append(element)
    return unique

print(unique([1,2,3,3,3,3,4,5]))


'''

'''
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True

print("Prime: "+ str(test_prime(int(input("Enter the number to be checked for prime: ")))))

'''


'''
def filter_even(list):
    even_list= []
    for num in list:
        if num % 2==0:
            even_list.append(num)

    return even_list

print(filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))

'''

'''

lam1 = lambda x : x + 15
print("Addition in lambda function is:",(lam1(3)))

lam2 = lambda x, y : x * y
print("Multiplication is:",(lam2(2, 9)))

'''

'''
def mul(num):
    return num*int(input("Enter a random number: "))

print(mul(3))

'''

'''
def sort_tuple(list):
    print("Original list of tuples:")
    print(list)
    list.sort(key = lambda x: x[1])
    return list

subject_marks = [('social', 74), ('maths', 98), ('nepali', 67), ('eph', 82)]
print("The sorted list of tuple is: "+ str(sort_tuple(subject_marks)))


'''


'''
sample=[{"salary":90000},{"salary":1200000},{"salary":1400000},{"salary":60000},{"salary":100000}]

sample.sort(key= lambda x: x["salary"])

print(sample)

'''

'''
def odd(List):
    b=list(filter(lambda x: (x % 2 != 0), List))
    return b

print("Odd numbers from given list",odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))

'''


'''

def mul(List):
    c = list(map(lambda x: x**2, List))
    d = list(map(lambda x: x **3, List))
    return c,d

print("Square and Cube  of given list are: ",mul([1, 2, 3, 4, 5, 6, 7, 8, 9]))

'''

'''
check = lambda x: True if x.startswith('P') else False
print("Starts with P: " + str(check('Pardesh')))


'''

'''
is_num = lambda q: q.isdigit()
print("Is Number?: " + str(is_num('9842042640')))
print("Is Number?: " + str(is_num('ram')))


'''

'''
def fibonacci(count):
    list = [0, 1]
    any(map(lambda a : list.append(sum(list[-2:])),
            range(2, count)))
    return list[:count]
print(fibonacci(10))


'''


'''

rr1=[1,2,3,4,5,6,7,8,9]
arr2=[1,3,5,7,9]
inter=[]
inter=list(filter(lambda a: a in arr2, arr1))
print(inter)

'''
a
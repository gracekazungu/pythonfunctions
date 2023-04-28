#  Write a function to reverse a string in Python without using any built-in functions.
def reverse_string(stringarr):
    str1=""
    for i in range(len(stringarr)-1,-1,-1):
        str1+=stringarr[i]
    return str1

# Write a function that takes an array of integers and returns the sum of all the even 
# numbers in the array.
def Evennumbers(nums):
    empty=[]
    for i in nums:
        if i%2==0:
            empty.append(i)
    return empty

def Evennums(numberss):
    summ=0
    for i in numberss:
        if i%2==0:
            summ+=i
    return summ

# Write a function that takes an array of integers and returns the sum
#  of all the odd numbers in the array.
def Oddnums(oddnumbers):
    add=0
    for i in oddnumbers:
        if i%2!=0:
            add+=i
    return add

# Write a function that takes an array of integers and returns the largest number in the array.
def largenum(largestnums):
    largest=largestnums[0]
    for i in largestnums:
        if i>largest:
            largest=i
    return largest


def g(hoo):
    longest=0
    for i in hoo:
        if i>longest:
            longest=i
    return longest
# Write a function that takes an array of integers and returns the smallest number in the array.
def smallestnum(smallnum):
    smallest=smallnum[0]
    for i in smallnum: 
        if i<smallest:
            smallest=i
    return smallest

# def small(nums):
#     smalles=0
#     for i in nums:
#         if i<smalles:
#             smalles=i
#     return smalles

# Write a function that takes an array of integers and returns a
#  new array with all the even numbers removed
def Remove_even(odd):
    for i in odd:
        if i%2==0:
            odd.remove(i)
    return odd

def Removeodd(nums):
    d=[]
    for i in nums:
        if i%2!=0:
            d.append(i)
    return d

# Write a function that takes an array of integers and returns 
# a new array with all the odd numbers removed.
def Remove_odd(even):
    r=[]
    for i in even:
        if i%2!=0:
            r.append(i)
    return r

# Write a function that takes an array of integers and returns a new 
# array with all the duplicates removed.
def Remove_dup(dupli):
  return list(set(dupli))

# Write a function that takes an array of integers and returns the 
# second largest number in the array.
def secondlarge(large):
    for i in large:
        large.sort()
    return large[-2]

def secondlarge(large):
    large.sort()
    return large[-2]

def find_second_largest(arr):
    # Initialize the two largest values
    largest = arr[0]
    second_largest = arr[0]

    # Iterate over the array
    for i in range(len(arr)):
        # If the current element is larger than the largest value, update both largest and second_largest
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        # If the current element is smaller than the largest but larger than the second largest, update second_largest
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    return second_largest
# Write a function that takes an array of integers and returns the second smallest number in the array.
def second_smallest(nums):
    nums.sort()
    return nums[1]
# Write a function that takes two arrays of integers and returns a new array containing
#  the elements that appear in both arrays.
def all(summm,roo):
    k=set(roo)
    u=set(summm)
    s=list (k.intersection(u))
    return s
def common_elements(arr1, arr2):
    result = []
    for element in arr1:
        if element in arr2 and element not in result:
            result.append(element)
    return result

# def alllo(str1,str2):
#     y=set(str1)
#     t=set(str2)
#     g=y.intersection(t)
#     n="".join(g)
#     return n

# Write a function that takes an array of integers and returns a
#  new array containing only the prime numbers.
def get_primes(arr):
    primes = []
    for num in arr:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


def get_primes(arr):
    primes = []
    for num in arr:
        if num > 1:
            for i in range(2,int(num/2)+1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

# def primenumbers(n):
#     if n<2:
#         for i in range(2,n):
#                 if n%i==0:
#                     break
#                 else:
#                     n
#     return n
# # Write a function that takes an array of integers and returns the product 
# # of all the numbers in the array.
# def num_product(products):
#     prdt=1
#     for i in products:
#         prdt*=i
#     return prdt

# # Write a function that takes an array of integers and returns the median value.
def median_num(nummode):
    r=sorted(nummode)
    p=len(r)
    if p%2==0:
        middleindx=p//2
        return (r[middleindx-1]+r[middleindx])/2
    else:
        middleindx=p//2
        return r[middleindx]

# Write a python function that takes one argument as a list a = [2,4,6,8] and
#  remove the second last item from that list and returns the whole list without the removed item   
def Removenum(nums):
    del nums[-2]
    return nums

def Removenumm(nums):
    nums.pop(-2)
    return nums

def Removen(nums):
   return nums[ :-2]+[nums[-1]]

# Write a python program that has a list days = [ “Monday”, “Tuesday”, “Friday”, “Monday”] 
# and counts the number occurrences of Monday
def h(days):
    count=0
    for day in days:
        if day=="Monday":
            count+=1
    return count

def mon(days):
    count=days.count("Monday")
    return count

def daiz(days):
    count = len([day for day in days if day == "Monday"])
    return (count)  # Output: 2




# def b(days):
#     count = 0
#     i=0
#     while i < len(days):
#         if days[i] == "Monday":
#             count += 1
#             i += 1   
#     return count

# Write a Python function named smallest that accepts a list of unsorted integers 
# and returns the smallest number in the list. Example:
# smallest([3,6,8,2,4,1,5,7]) returns 1
def smallest(numbers):
    small=numbers[0]
    for i in numbers:
        if i <small:
            small=i
    return small

def smallestt(numbers):
    t=sorted(numbers)
    return t[0]

def smallest(nums):
    return min(nums)

def largest(nums):
    return max(nums)


# Write a python function named divisible_by_seven that; using the range function and a
#  for loop returns a list containing all the numbers between 100 and 200 that are divisible by 7.
def divisible_by_seven():
    g=[]
    for i in range(100,200):
        if i%7==0:
            g.append(i)
    return g
    # solution 2
def divisible_by_seven():
    return [i for i in range(100, 201) if i % 7 == 0]


# 5.Write a python program that takes two inputs(as integers) from a user and adds
# the 2 numbers, checks  if the sum is greater than than 10, less than 10 or equal 10 
# and prints a statement  after each check   
def two_inputs(arr1,arr2):
    r=arr1+arr2
    if r>10:
        return ("f{r} is greater than 10")
    elif r<10:
        return("f{r} is less than 10")
    elif r==10:
        return ("f{r} is equal to 10")

#  6.Write a python function that takes one argument which is a list,  a=[1,2,3,4,5] 
#  and returns    True if 4 is present in the list and False is 4 is not in the list
def four_present(numbers): 
    d=4
    if d in numbers:
        return True
    else:
        return False
#  Write a python function that takes one argument which is a list    
#  fruits=["apples","grapes","pineapple"] and removes the last fruit  from the list then 
# returns the list without the removed fruit
def g(fruits):
    fruits.pop()
    return fruits

#   8.Write a python program that takes in a list of cars, cars = ['Ford', 'BMW', 'Volvo'] 
#       and returns a sorted list 
def carslist(cars):
    d=sorted(cars)
    return d


   



    
    
   





    
    
    




    



    





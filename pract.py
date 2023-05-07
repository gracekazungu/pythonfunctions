# Write a function that takes a list of strings as input and
#  returns a new list that contains only the strings with more than 5 characters.
def ListStrings(*strings):
    empty=[]
    for string in strings:
        if len(string)>5:
            empty.append(string)
    return empty

    # Write a function that takes a string as input and returns true if the string
    #  is a palindrome, false otherwise.
def is_palindrome(str):
    if len(str)<1:
        return True
    else:
        if str[0]==str[-1]:
            return is_palindrome(str[1:-1])
        else:
            return False    

# Write a function that takes a list of numbers as input and 
# returns a new list that contains the square of each number in the input list.
def product(*numbrs):
    prdt=[]
    for num in numbrs:
        prdt.append(num**2)
    return prdt

# Write a function that takes a number as input and returns
#  true if the number is a prime number, false otherwise.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        
    return True
   
# Write a function that takes a list of strings as input 
# and returns the string with the most characters.
def Str(*strr):
    max=0
    longest=""
    for i in strr:
        if len(i)>max:
            max=len(i)
            longest=i
    return longest

# Write a function that takes a list of numbers as input and 
# returns a new list that contains only the numbers that are divisible by 3.
def List(*inputs):
    b=[]
    for i in inputs:
        if i%3==0:
            b.append(i)
    return b
# Write a function that takes a string as input and returns true 
# if the string contains only unique characters, false otherwise.
def has_unique_chars(s):
    seen_chars = set()
    for c in s:
        if c in seen_chars:
            return False
        seen_chars.add(c)
    return True

# Write a function that takes a list of numbers as input and returns the median of those numbers.
def numms(*nummms):
    sortnum=sorted(nummms)
    p=len(sortnum)
    if(p%2==0):
        middleindx=p//2
        return (sortnum[middleindx-1]+sortnum[middleindx])/2
    else:
        middleindx=p//2
        return sortnum[middleindx]
    

def median(*numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        # If the list has an even number of elements, take the average of the two middle values
        middle_index = n // 2
        return (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
    else:
        # If the list has an odd number of elements, return the middle value
        middle_index = n // 2
        return sorted_numbers[middle_index]

# # Write a function that takes a list of numbers as input and returns 
# the most frequently occurring number in the list.

# def most_frequent(*numbers):
#     count = Counter(numbers)
#     return count.most_common(1)[0][0]

def all(*nums):
    if len(nums)>1:
        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]

def sortedarr(left,right):
    emptyarr=[]
    while len(left) and len(right):
        if left[0]<right[0]:
            emptyarr.append(left.pop())
        else:
            emptyarr.append(right.pop())
    return (emptyarr)

# Write a function that takes two numbers as input and returns their sum.
def two_nums(*two):
    summ=0
    for i in two:
        summ+=i
    return summ

# Write a function that takes a list of numbers as input and returns the average of those numbers.
def average(*avr):
    u=0
    t=len(avr)
    for i in avr:
        u+=i
    return u//t

# Write a function that takes a string as input and returns the length of the string.
def lengthh(numlength):
    n=len(numlength)
    return n


# Write a function that takes a list of numbers as input and returns the largest number in the list.
def arraynumbers(*numarr):
    g=sorted(numarr)
    h=g[-1]
    return h

def arraynumber(nums):
    largest=0
    for i in nums:
        if i>largest:
            largest=i
    return largest


# Write a function that takes a list of strings as input and returns the longest string in the list.
def longeststr(long):
    max_len=1
    longeststrr=""
    for i in long:
        if len(i)>max_len:
            max_len=len(i)
            longest=i
    return longest

def longest_string(str_list):
    max_len = 0
    longest_str = ""
    for string in str_list:
        if len(string) > max_len:
            max_len = len(string)
            longest_str = string
    return longest_str



# sum
def summnums(nums):
    r=0
    for i in nums:
        if i%2==0:
            r+=i
    return r




        









        
    
     


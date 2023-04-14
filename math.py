def add(a,b):
    answer=a+b
    return answer

def subtract(c,d):
    answer2= c-d
    return answer2

def divide(e,f):
    answer3=e/f   
    return answer3

def multiply(g,h):
    answer4=g*h
    return answer4

def remainder(i,j):
    answer5=i%j
    return answer5

def sum(*numbers):
    answer=0
    for number in numbers:
        answer+=number
    return answer

def multiply(*nums):
    multi=1
    for num in nums:
        multi*=num
    return multi
def my_country(country="Kenya"):
    print(f"Hello from {country}")

def greet(*names):
    for name in names:
        print(f"Hello {name}")

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

def student_attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

# A function named concatenate_args that takes any number of string arguments 
# in positional arguments format and concatenates them into a single string
def concatenate_args(*strings):
    concat=""
    for num in strings:
        concat+=num
    return concat
        

    
# A function named concatenate_kwargs that takes any number of string 
# arguments in keyword arguments  format and concatenates them into a single string

def concatenate_kwargs(numbs):
    summ=""
    for key,value in words.items():
        summ+=value
    return summ  

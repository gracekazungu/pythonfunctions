# Write a function that uses while, if and continue statements to print all 
# the even numbers between 0 and 50. 
def Even_numbers():
    numbers=0
    while numbers<50:
        numbers+=1
        if numbers%2!=0:
            continue
        print(numbers) 

# Write a function that takes an integer argument and prints "Prime" if the number 
# is prime, and "Not prime" if the number is not prime.
def check_prime(n):
    if n <= 1:
        print(f"{n} Not prime")
    elif n == 2:
        print(f"{n} prime")
    else:
        for i in range(2,n):
            if n % i == 0:
                print(f"{n} Not prime")
                break
        else:
            print(f"{n} Prime")

# Write a function that takes a list of integers as input and prints the sum 
# of all the even numbers in the list.
def sum_even_numbers(listint):
    addition=0
    for i in listint:
        if i%2==0:
            addition+=i
    print(addition)

# Write a function that takes any two integers as input, and prints the sum of all the numbers
#  between the two integers (inclusive) that are divisible by 3.
def sum_two_intergers(int1,int2):
    add=0
    for i in range(int1,int2):
        if i%3==0:
            add+=i
    print(add)

            
    
                
            


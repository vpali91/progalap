def prime_checker(number):
    isPrime =True
    for i in range(2,number):
        if number%i==0:
            isPrime = False
    if isPrime:
        print("This is prime number")
    else:
        print("This is not prime number")
    
prime_checker(10)

import time

def is_prime(num):              # first version -> checks if num divides completely by any of the numbers lower than itself - ver memory consuming for larger ranges (100000+)
    for i in range(2, num) :
        if num % i == 0 :
            return False
    return True

def is_prime2(num):             #second version -> each time it checks it reduces the range that needs to be checked in the next step
    i = 2
    max = num
    while i < max :
        if num % i == 0 :
            return False
        else :
            i+=1
            max = num//i + 1    # to keep the max (range) integer and avoid fractions (num/i returns some non-prime numbers like 25, 49)
    return True

# both the above functions only check one number if it's prime and in order to find all from range both functions need to be used in loops
# in order to further streamline the process of finding all primes from a range, this 3rd function is written which will find all from range at once
# thanks to this approach we will be able to greatly limit the amount of operations, as if a number is indivisible by 2 it will never be indivisible by, 4, 6, 8 and any other even number
# if a number is indivisible by 3 it will never be divisible by 6, 9, 12 and any other number disible by 3 and so on. Therefore we only need to check if a number is divisible by
# any of the prime number smaller than itself. But it is only feasbiel if a function remembers all previously found prime numbers

def are_primes(ran) :            
    primes_list = [2] 
    max = ran
    i = 3
    while i < ran :
        isprime = False
        for j in primes_list :
            if j > max :
                break
            if i % j == 0 :
                isprime = False
                break
            else :
                isprime = True
            max = ran//j + 1

        if isprime :
            primes_list.append(i)

        i += 1       

    primes_list.insert(0, 1)    # 1 needs to be added to the list of primes at the end, otherwise every number % 1 == 0 
    return primes_list

def compareAndPrint(ran) :   #compares and outputs all prime numbers found by both functions
    for i in range(1, ran):
        if is_prime(i):
                print(i, end=" ")
    print()            
    for i in range(1, ran):            
        if is_prime2(i):
                print(i, end=" ")
    print()            
    list = are_primes(ran)
    for i in list :
        print(i, end=" ")
    print()

def compareSum(ran) :       #compares sums of all prime numbers found by all functions - more practical with larger ranges
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(1, ran):
        if is_prime(i):
            sum1 += i
        if is_prime2(i):
            sum2 += i
    sum3 = sum(are_primes(ran))
    if sum2 == sum1 == sum3 :
        print("OK")
    else :
         print("Error")

def compare_time(ran) :      #this function will compare how much time each function takes to fin all prime numbers from within range
    start_time = time.time()
    for i in range(1, ran):
        if is_prime(i):
            next
    print("Function No 1 took %f seconds to find all primes from range 1 to %d" % (time.time() - start_time, ran))

    start_time = time.time()
    for i in range(1, ran):
        if is_prime2(i):
            next
    print("Function No 2 took %f seconds to find all primes from range 1 to %d" % (time.time() - start_time, ran))

    start_time = time.time()
    are_primes(ran)
    print("Function No 3 took %f seconds to find all primes from range 1 to %d" % (time.time() - start_time, ran))

# TESTING: uncomment relevant line depending on what you wnat to test
#are_primes(5)
#print(are_primes(10))
compareAndPrint(200)
compareSum(10000)
compare_time(50000)
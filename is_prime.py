def is_prime(num):
    for i in range(2, num) :
        if num % i == 0 :
            return False
    return True
for i in range(2, 1000):
	if is_prime(i):
			print(i, end=" ")
print()

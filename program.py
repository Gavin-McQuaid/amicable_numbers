import math
total = 0
nums = []
i = 220
while i < 10000:
	j = 1
	sum_of_divisors = 0
	while j <= math.ceil(i/2):
		
		if i % j == 0:
			sum_of_divisors += j
		j += 1
	new_sum = 0
	k = 1
	while k <= sum_of_divisors/2:
		if sum_of_divisors % k == 0:
			new_sum += k
			
			
		k += 1
	if i == new_sum and i != sum_of_divisors:
		print i,sum_of_divisors
		total += i 
	i += 1
print total

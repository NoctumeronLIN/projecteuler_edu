# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143

start_problem_target_number = 13195
print('In this case we search prime factors of ', + start_problem_target_number)
searcheable_factor = 1
min_prime_factor = 1
max_prime_factor = start_problem_target_number
massive_of_founds=[]
mass_i = 0
check_mass = 1
for searcheable_factor in range(min_prime_factor, max_prime_factor):
    if max_prime_factor % searcheable_factor == 0 and searcheable_factor > 1:
        max_prime_factor = max_prime_factor // searcheable_factor
        min_prime_factor = searcheable_factor
        mass_i = mass_i+1
        massive_of_founds.append(searcheable_factor)
        print('we found', +searcheable_factor, 'and', +max_prime_factor)
for x in massive_of_founds:
    check_mass *= x
    largest_number = 0
    if x > largest_number:
        largest_number = x
print('Founded numbers confirmed with checksumm =', +check_mass, '\nand largest number is', +largest_number)
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
print('"In this task we found summ between natural numbers from 1 to 10, multiples of 3 and 5" \n "Check this out"')
max_number = 10
min_number = 1
mult_first = 3
mult_second = 5
sum_of_founds = 0
for Next_num in range(min_number, max_number):
    if((Next_num % mult_first == 0) or (Next_num % mult_second == 0)):
        sum_of_founds += Next_num
print('"The summ of founds in that case = ', +sum_of_founds)
print('"DO you want to check 2nd case (with 1000)? Type + or -')
decision = input()
if decision == "-":
    print('See you next time')
else:
    max_number = 1000
    sum_of_founds = 0
    for Next_num in range(min_number, max_number):
        if((Next_num % mult_first == 0) or (Next_num % mult_second == 0)):
            sum_of_founds += Next_num
    print('"The summ of founds in that case = ', +sum_of_founds)

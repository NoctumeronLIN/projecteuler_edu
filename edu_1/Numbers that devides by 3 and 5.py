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
print('The summ of founds in that case = ', +sum_of_founds)
print('DO you want to check another range? Type + or -')
decision_another_range = input()
if decision_another_range == "-":
    print('See you next time')
else:
    new_max_number = int(input())
    max_number = new_max_number
    sum_of_founds = 0
    print('Maybe you should try another multiplies? Type + or -')
    decision_another_mult = input()
    if decision_another_mult == '-':
        print('Ok, 3 and 5, as in problem')
        for Next_num in range(min_number, max_number):
            if((Next_num % mult_first == 0) or (Next_num % mult_second == 0)):
                sum_of_founds += Next_num
        print('The summ of founds in that case = ', +sum_of_founds)
    else:
        new_mult_first = int(input())
        mult_first = new_mult_first
        new_mult_second = int(input())
        mult_second = new_mult_second
        print('So, the problem now: \n "In this task we found summ between natural numbers from 1 to', +max_number, ', multiples of ', +mult_first, ' and ', +mult_second)
        sum_of_founds = 0
        for Next_num in range(min_number, max_number):
            if((Next_num % mult_first == 0) or (Next_num % mult_second == 0)):
                sum_of_founds += Next_num
        print('The summ of founds in that case = ', +sum_of_founds)
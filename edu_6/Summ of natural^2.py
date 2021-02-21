# The sum of the squares of the first ten natural numbers is,
# The square of the sum of the first ten natural numbers is,
# Hence the difference between the sum of the squares of the first 
#   ten natural numbers and the square of the sum is .
# Find the difference between the sum of the squares of the first 
#   one hundred natural numbers and the square of the sum.

how_much_number_need = input('How much numbers we need?\n')
list_of_founds=[]
list_of_counts=[i for i in range(0,(int(how_much_number_need)))]
found_devider = 0
last_for_range = int(how_much_number_need*2)
for number in range(2, int(last_for_range)):
    for devider in range(2, number):
        if number % devider == 0:
            found_devider += 1
    if found_devider == 0:
        list_of_founds.append(number)
        if len(list_of_founds) >= int(how_much_number_need):
            break
    else:
        found_devider = 0
print(list_of_founds)
#------------------------------------------------------------------
#---Summ all element and square them-------------------------------
Summ_of_elements = 0
for x in range(1, int(how_much_number_need)+1): 
    element_from_list_of_founds = list_of_founds[x-1]
    Summ_of_elements += element_from_list_of_founds
    Square_of_summ = Summ_of_elements**2
print('Square of summ :\n', +Square_of_summ)
#------------------------------------------------------------------
#---Square all element and summ them-------------------------------
summ_of_squares = 0
for x in range(1, int(how_much_number_need)+1, 1):
    element_from_list_of_founds = list_of_founds[x-1]
    Square_of_element = element_from_list_of_founds**2
    summ_of_squares += Square_of_element
print('Summ of all squares :\n', +summ_of_squares)
#------------------------------------------------------------------
#-----Summ of squares - square of summs----------------------------
print('Answer is', +Square_of_summ-summ_of_squares)
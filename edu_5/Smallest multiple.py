# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

print('Please enter a 2 digit number for max multiplier')
max_multiplier = int(input())
first_multiplier = 1
List_of_all_multipliers=[]
List_of_all_products=[]
check_list_of_deviders=[]
last_devider=max_multiplier
#-----------------------Перебор и запись множества множителей-------------------------
for multiplier in range(1, (max_multiplier + 1)):
    List_of_all_multipliers.append(multiplier)
    if multiplier == 1:
        List_of_all_products.append(multiplier)
    else:
        List_of_all_products.append(List_of_all_products[multiplier-2] * multiplier)
print(List_of_all_multipliers) # Проверка списка множителей
print(List_of_all_products) # Проверка результатов умножения
#-------------------------------------------------------------------------------------
#---Начинаем поиск наименьшего значения,делимого на все множители из первого списка---
last_number_of_production = int(max(List_of_all_products))
for search_min_of_production_for_all_deviders in range(1, last_number_of_production):
    if search_min_of_production_for_all_deviders % max_multiplier == 0:
        for each_devider in range(1, max_multiplier+1):
            result_of_last_dev = search_min_of_production_for_all_deviders % each_devider
            if result_of_last_dev == 0:
                check_list_of_deviders.append(each_devider)
            else:        
                each_devider = 1
        if len(check_list_of_deviders) == len(List_of_all_multipliers):
            print(search_min_of_production_for_all_deviders, 'is the less number that can be devide by', List_of_all_multipliers)
            break
        check_list_of_deviders.clear()            
    else:
        search_min_of_production_for_all_deviders += 1
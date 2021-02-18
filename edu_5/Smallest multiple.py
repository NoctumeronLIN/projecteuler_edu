# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

print('Please enter a 2 digit number for max multiplier')
max_multiplier = int(input())
List_of_all_multipliers=[]
List_of_all_products=[]
check_list_of_deviders=[]
#-----------------------Перебор и запись множества множителей------------------------
for multiplier in range(1, (max_multiplier + 1)):
    List_of_all_multipliers.append(multiplier)
    if multiplier == 1:
        List_of_all_products.append(multiplier)
    else:
        List_of_all_products.append(List_of_all_products[multiplier-2] * multiplier)
print(List_of_all_multipliers) # Проверка списка множителей
print(List_of_all_products) # Проверка результатов умножения
#------------------------------------------------------------------------------------
#---Начинаем поиск наименьшего значения,делимого на все множители из первогосписка---
last_number_of_production = int(max(List_of_all_products))
for search_min_of_production_for_all_deviders in range(1, last_number_of_production):
    devider = max_multiplier
    result_of_max_dev = int(search_min_of_production_for_all_deviders / devider)
    if result_of_max_dev >= 1 and search_min_of_production_for_all_deviders % devider == 0:
        next_devider = 1
        for next_devider in range(1, (devider+1)):
            result_of_next_dev = int(search_min_of_production_for_all_deviders % next_devider)
            if result_of_next_dev == 0:
                next_devider += 1
                if int((max(check_list_of_deviders))+1) < max_multiplier:
                    check_list_of_deviders.clear(check_list_of_deviders)
                else:
                    check_list_of_deviders.append(search_min_of_production_for_all_deviders)
                    print(check_list_of_deviders)
                
    else:
        search_min_of_production_for_all_deviders += 1


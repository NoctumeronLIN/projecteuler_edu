# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# So the thing is if we read left to right as "asasa" AND right to left "asasa" = then we got the point.
# To reach that we need take 100*100 in cycle from 100 to 999, take result like string and check spelling


result_of_product = 0
line_to_search_from_result = str
is_palindrome = str
mass_item_number = 0
mass_of_first=[]
mass_of_second=[]
mass_of_palindromes=[]
for first_number in range(100,999):
    for second_number in range(100,999):
        result_of_product = first_number * second_number
        line_to_search_from_result = str(result_of_product)
        is_palindrome = line_to_search_from_result[::-1]
        if is_palindrome == line_to_search_from_result:
            mass_item_number += 1
            mass_of_first.append(first_number)
            mass_of_second.append(second_number)
            mass_of_palindromes.append(result_of_product)
for search in range(1, mass_item_number):
    max_pallindrom = max(mass_of_palindromes)
    index_of_founded = mass_of_palindromes.index(max(mass_of_palindromes))
    max_number_in_mass_of_first = mass_of_first[index_of_founded]
    max_number_in_mass_of_second = mass_of_second[index_of_founded]
print('We found', + mass_item_number, 'palindromes')
print("Biggest palindrome", +max_pallindrom, 'with numbers', +max_number_in_mass_of_first, '*', +max_number_in_mass_of_second)
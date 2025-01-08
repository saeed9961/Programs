# Sample dictionary
my_dict = {'banana': 3, 'apple': 1, 'cherry': 2, 'date': 4}
print("Original list:", my_dict)
# Sort in ascending order
as_sorted_dict = dict(sorted(my_dict.items()))
print("Ascending order:", as_sorted_dict)
# Sort in descending order
des_sorted_dict = dict(sorted(my_dict.items(), reverse=True))
print("Descending order:", des_sorted_dict)



#based on values



# Sort by values in ascending order
as_sorted_dict_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending order by value:", as_sorted_dict_by_value)


# Sort by values in descending order
des_sorted_dict_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order by value:", des_sorted_dict_by_value)

a_dictionary = {
    'key_is_a_string': 'Value',
    2: 'key is a number'
}

a_dictionary['new_key'] = 55
a_dictionary['a_list'] = [1, 2, 3]
a_dictionary['another_dict'] = {'second_dict': 2}

for key in a_dictionary:
    print(f"key: {key} > value: {a_dictionary[key]} ")
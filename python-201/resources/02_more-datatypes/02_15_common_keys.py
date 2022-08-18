# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}


#empty dict where comnbined key and values will be stored

combined_dict = {}

# loop throughh dict_1 
for key_1 in dict_1.keys():
    for key_2 in dict_2.keys():
        #if both keys are the same
        if key_1 == key_2 :
            # abstarct both values with the same key
            value_1 = dict_1[key_1]
            value_2 = dict_2[key_2]
            # store the key and new value in the combined dict
            combined_dict[key_1] = value_1 + value_2
            break
        # if item is unique to dict_1
        else :
            combined_dict[key_1] = dict_1[key_1]

# if item is unique to dict_2, include it
for key in dict_2.keys():
    if key not in combined_dict.keys():
        combined_dict[key] = dict_2[key]


print(combined_dict)



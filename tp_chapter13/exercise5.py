from random import choices

## Find occurencies of elements in a list 
# @param t a list of elements
# @ return a dict with elements as keys and their occurencies as values
#
def ls_hist(t):
    d = {}
    for elem in t:
        if elem not in d:
            d[elem] = 1
        else:
            d[elem] += 1
    return d

# Store data from user in a list
user_inputs = input("Please, enter any kind of data (digit a white space before entering the next datus): ")
user_inputs = user_inputs.split()

# Use ls_hist function to compute the occurencies of the elements in the list
d = ls_hist(user_inputs)

# Convert all key-value pairs in a list of tuple
d_items = d.items()

# Create a list of tuple where the first store all the keys
# and the second all the values
t = list(zip(*d_items))

# Split each sequence in different variables
elems, freqs = t

# Each element will be returned randomly according to its frequence
random_weight_elem = choices(elems, freqs)

# Display the result
print(random_weight_elem)
    

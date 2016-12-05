string_input = raw_input('enter numbers')
input_list = string_input.split() #splits the input string on spaces
# process string elements in the list and make them integers
input_list = [int(a) for a in input_list]

print input_list
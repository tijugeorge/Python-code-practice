import numpy

string_input = raw_input('enter any 9 numbers')
input_list = string_input.split() #splits the input string on spaces
# process string elements in the list and make them integers
input_list = [int(a) for a in input_list]
print input_list
print sorted(input_list)
x = numpy.array(input_list)
y = numpy.array(sorted(input_list))

x.shape = (3, 3)
y.shape = (3, 3)
print x
print y
num_array = list()
num = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for i in range(int(num)):
    n = raw_input("num :")
    num_array.append(int(n))

    # remove duplicate 
    result_array = sorted(set(num_array))

    # sum values and print 
print sum(result_array)
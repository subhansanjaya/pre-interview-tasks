import re

num = '' 

while not re.match('^-?[0-9]*\.?[0-9]+$',num):
  num = raw_input("Enter a number please: ")


def collatz_sequence(x):
    num_seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
    # Added line
       num_seq.append(x)    
    return num_seq


print(collatz_sequence(int(num)) )


# Suppose you have a file called numbers.txt that has lists of three integers per line, like this:

# 10 20 23
# -7 8 15
# 0 12 -51
# 17 -12 -1

# There may also be more or fewer than four lines. However, each line contains exactly three integers. Write a program that computes the sum of each row and outputs that sum to another file called output.txt.

# For the file above, output.txt should contain the following when your program is finished:

# 63
# 16
# -39
# 4

import pickle

numbersfile= open ('numbers.txt','r')# as pickle_file:
sumfile = open('output.txt','w')
for line in numbersfile:
  numberSum = 0
  number = line.split()
  print(number)
  for n in number:
    print(n)
    numberSum += int(n)
  print(numberSum)
  sumfile.write(str(numberSum) + "\n")

numbersfile.close()
sumfile.close()

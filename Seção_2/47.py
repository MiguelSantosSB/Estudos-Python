"""
For / While
 0     10
 1      9
 2      8
 3      7  
 4      6
 5      5
 6      4
 7      3 
 8      2 
"""


num1 = range(9)
num2 = range((11-1), 1, -1)


for seq in num1:
    print(seq)             
    for seq2 in num2:
        print(seq2)


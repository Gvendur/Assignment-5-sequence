# Sequence algorithm:
# The first two numbers in the sequence do not follow a pattern so they are printed individually.
# Rest of the sequence works like this: 0 + 1 + 2 = 3
#                                       1 + 2 + 3 = 6
#                                       2 + 3 + 6 = 11
# Every new number generated is the sum of previous three numbers.

n = int(input("Enter the length of the sequence: ")) 

temp_1, temp_2, temp_3, temp_4  = 0, 1, 2, 1

for i in range(n):
    if(i <= 1):
        print(temp_4, end=" ")
        temp_4 += 1
    else:
        temp_4 = temp_1 + temp_2 + temp_3
        print(temp_4 , end=" ")
        temp_1 = temp_2
        temp_2 = temp_3
        temp_3 = temp_4
        
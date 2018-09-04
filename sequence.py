# Sequence algorithm:
# The first two numbers in the sequence do not follow a pattern so they are printed individually.
# Rest of the sequence works like this: 0 + 1 + 2 = 3
#                                       1 + 2 + 3 = 6
#                                       2 + 3 + 6 = 11
# Each number is added then each number moves to the left of their plus or equal sign and the leftmost number is removed.
# Then they are added again and moved to the left of their plus or equal sign and so on.

n = int(input("Enter the length of the sequence: ")) 

temp_1, temp_2, temp_3, temp_4  = 0, 1, 2, 1

import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
all = upper_case + numbers
length = 16

gene = ''.join(random.sample(all, length))
print("Code Is", gene)
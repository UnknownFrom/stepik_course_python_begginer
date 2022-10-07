num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

max_num = max(num_1, num_2, num_3)
min_num = min(num_1, num_2, num_3)

print(max_num)
print((num_1+num_2+num_3)-max_num-min_num)
print(min_num)

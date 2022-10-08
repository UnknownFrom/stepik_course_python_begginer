num = int(input())

first_dig = None
last_dig = num % 10
count_dig = 0
total_sum = 0
total_multy = 1

while num != 0:
    last = num % 10
    first_dig = last
    total_multy *= last
    total_sum += last
    count_dig += 1
    num //= 10
print(total_sum)
print(count_dig)
print(total_multy)
print(total_sum / count_dig)
print(first_dig)
print(first_dig + last_dig)

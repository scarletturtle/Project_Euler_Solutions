serial3 = 0
serial5 = 0
num3 = 3
num5 = 5
sum3 = 0
set3 = set()
set5 = set()
while True:
    sum3 = num3 * serial3
    serial3 += 1
    if sum3 >= 1000:
        break
    else:
        set3.add(sum3)
print(set3)
while True:
    sum5 = serial5 * num5
    serial5 += 1
    if sum5 >= 1000:
        break
    else:
        set5.add(sum5)
print(set5)
set3or5 = set3.union(set5)
print(set3or5)
sum3or5 = 0
for i in set3or5:
    sum3or5 += i
print(sum3or5)


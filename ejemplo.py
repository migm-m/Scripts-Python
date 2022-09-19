list = [7, 14, 81, 56, 9, 17, 43]
min = list[0]
for i in range(1, len(list)):
    if list[i] < min:
        min = list[i]
print("Min:" + min)
input()

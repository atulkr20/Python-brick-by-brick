# check if list is sorted or not

a = [12, 13, 14, 15, 16]

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        print("Your list is not sorted")
        break
else:
    print("Your list is sorted")
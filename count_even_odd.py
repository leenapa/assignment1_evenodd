list1 = [1,2,3,4,5,6,7,8,9]
even = 0
odd = 0
for i in list1:
    if (i%2==0):
        even=even+1
    else:
        odd=odd+1
print("Even number in list1 ",even)
print("Odd number in list1",odd)
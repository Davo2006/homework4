#xndir4.py (Write a Python program to remove duplicates from a list.)
x = [1,1,1,2,3,4,5,6,7,8,5,1]
y = []
for i in x:
    if i not in y:
        y.append(i)
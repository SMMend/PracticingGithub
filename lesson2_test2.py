#append- allows you to add just one value at a time
#extend -allows you to add multiple values at a time
#insert- allows yout o specify the positionw here youw ant it to be inserted

month =["January", "February"]
month.extend(["March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
print month

month.append(9)
print month

month.pop(0)
print month
#month.extend([1, 2, 3])
#month.pop(-3:-1)
#print month

month.insert( 0, 'January')
print month


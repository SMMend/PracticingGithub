#Use raw_input() to allow a user to type an address

#If that address contains a quadrant (NW, NE, SE, SW), then add it to #that quadrant's list.

#Allow user to enter 3 addresses; after three, print the length and #contents of each list.


NW=[]
NE=[]
SE=[]
SW=[]
Other=[]

address=raw_input("Please enter an address: ")
address_as_list =address.upper().split(" ")		# if address contains SEA SW it puts it in the SE list beacuse of thE SEA. Hence the split 
print address_as_list

if"NW" in address_as_list:
	NW.append(address)
elif "NE" in address_as_list:
	NE.append(address)
elif "SE" in address_as_list:
	SE.append(address)
elif "SW" in address_as_list:
	SW.append(address)
else:
	Other.append(address)

print "NW: ", NW
print "NE: ", NE
print "SE: ", SE
print "SW: ", SW 
print "Other: ", Other
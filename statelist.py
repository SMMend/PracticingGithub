state =["CO", "CA"]
state_name= ["Colorado", "California"]

print "<select>"
for item, cat in zip(state, state_name):
	print "<option value = ",item,">", cat,"</option>"

print"</select>"

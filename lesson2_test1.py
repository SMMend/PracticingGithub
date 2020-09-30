#Practicing days of the week
#adding another line because I want to see how history works
days_of_week=["Monday", "tuesday"]
print days_of_week

days_of_week.append("Wednesday")
print days_of_week

days_of_week.append("Thursday") #append allows you to apend just one value at a time
days_of_week.append( "Friday")
days_of_week.append( "Saturday")
days_of_week.append("Sunday")
print days_of_week
print len(days_of_week)

day = days_of_week.pop()
print day
print days_of_week

day=days_of_week.pop(3)
print day, days_of_week



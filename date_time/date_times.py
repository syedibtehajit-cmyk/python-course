from datetime import datetime

#current=datetime.now()
#print(current)
#print(current.date())
#print(current.time())
#print(current.year)
#print(current.month)
#print(current.day)
#print(current.hour)
#print(current.minute)

# Print Date and time Beautiful format

current =datetime.now()
print(current.strftime("%d-%m-%Y %H:%M"))
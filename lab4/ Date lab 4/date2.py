import datetime 

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)

print("Yesterday: ",yesterday.strftime("%d.%m.%y"))
print("Today: ",today.strftime("%d.%m.%y"))
print("Tomorrow: ",tomorrow.strftime("%d.%m.%y"))

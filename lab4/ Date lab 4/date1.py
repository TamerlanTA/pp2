import datetime 

today = datetime.datetime.now()

fivedays = today - datetime.timedelta(days = 5)

print(fivedays.strftime("%d.%m.%y"))

import datetime 

today = datetime.datetime.now()

today = today.replace(microsecond=0)

print(today.strftime("%d-%m-%y, %H:%M:%S"))

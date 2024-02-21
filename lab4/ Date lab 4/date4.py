from datetime import datetime
def date_difference_in_seconds(date1, date2):
    if not isinstance(date1, datetime):
        date1 = datetime.strptime(date1, "%y:%m:%d")
    if not isinstance(date2, datetime):
        date2 = datetime.strptime(date2, "%y:%m:%d")
    
    difference = abs(date2 - date1).total_seconds()
    return difference

date1 = str(input("Write first date: YY:MM:DD - "))
date2 = str(input("Write second date: YY:MM:DD - "))

difference_seconds = date_difference_in_seconds(date1, date2)
print("Difference in seconds:", difference_seconds)

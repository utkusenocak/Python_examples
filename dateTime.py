from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, "")
moment = datetime.now()

# print(moment.year)
# print(moment.month)
# print(moment.hour)
print(datetime.ctime(moment))
print(datetime.strftime(moment, "%Y %B %A"))
moment = datetime.now()
second = datetime.timestamp(moment)
print(second)
moment2 = datetime.fromtimestamp(second)
print(moment2)
print(datetime.fromtimestamp(0))
date = datetime(2019, 12, 1)
moment = datetime.now()
print(date - moment)


import datetime

hundred_days = datetime.timedelta(days=100)
print(datetime.datetime.now() + hundred_days)

print('--------------------------------------')

hundred_after = datetime.datetime.now().replace(hour=9, minute=0, second=0) + hundred_days
# print(hundred_after)

print('{}년 {}월 {}일'.format(hundred_after.year, hundred_after.month, hundred_after.day))

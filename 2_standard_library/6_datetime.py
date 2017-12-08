#! /usr/bin/python3

from datetime import date

now = date.today()
print (now)

formatted_datetime = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print (formatted_datetime)

birthday = now - date(1992, 12, 20)
print (birthday.days)

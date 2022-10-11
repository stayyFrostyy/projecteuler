
# You are given the following information, but you may prefer to do some research for yourself.

#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date

def main(y1, y2):
    sundays = 0
    for i in range(y1, y2):
        for j in range(1, 13):
            if date(i, j, 1).weekday() == 6:
                sundays += 1
    
    return sundays

print(main(1901, 2001))
import time;

mytime = time.time()

#this is a implementation of the ticks
print("the time is ", mytime)

localtime1 = time.localtime(time.time())
print("the localtime is ", localtime1)

localtime2 = time.asctime(time.localtime(time.time()))
print(localtime2)

import calendar;

cal = calendar.month(2008,12)

print("the month of the calender \n", cal)

print("another method to print the time is ", time.ctime(100456456))

#another representation of the time is --
t = (2009,12,31,12,00,00,00,00,00)

secs = time.mktime(t)
print ("the seconds calculates is ", secs)
print("the seconds of the time is", time.ctime(secs))


#sleep implementation
print ("the start of the execution", time.ctime())

#time.sleep(15)
print("the execution stops for some seconds")

print ("the stop of the execution", time.ctime())

#calender of the year is --

print(calendar.firstweekday())
print(calendar.isleap(2020))

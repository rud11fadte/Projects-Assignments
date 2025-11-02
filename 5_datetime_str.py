#!/usr/bin/python3
print("python Code")

import datetime

currentDateTime=datetime.datetime.now()
print(currentDateTime)

month={
 "01":"January",
 "02":"February",
 "03":"March",
 "04":"April",
 "05":"May",
 "06":"June",
 "07":"July",
 "08":"August",
 "09":"September",
 "10":"October",
 "11":"November",
 "12":"December",
 }
 

def getMonthName(dt):
	dt_str=str(dt)
	monthNum=dt_str.split('-')
	monthNum=monthNum[1]
	return month[monthNum]

def getDate(dt):
	month=getMonthName(dt)
	dateNum=((((str(dt)).split(" "))[0]).split("-"))[2]
	datesuffix="th"
	if int(dateNum) %10 == 1:
		datesuffix="st"
	elif int(dateNum) %10 == 2:
		datesuffix = "nd"
	elif int(dateNum) %10 == 3:
		datesuffix = "rd"
	return(dateNum + datesuffix +" "+ month)
	
def getTime(dt):
	month=getMonthName(dt)
	date=getDate(dt)
	time=((((str(dt)).split(" "))[1]).split(":"))[0]	
	t=int(time)
	if t < 6 and t >=12:
		return "Morning"
	elif t>12 and t<=14:
		return "afternoon"
	elif t>14 and t<=20:
		return "Evening"
	elif t>20 and t<=6:
		return "Night"

print(getDate(currentDateTime),end=" ")
print(getTime(currentDateTime))

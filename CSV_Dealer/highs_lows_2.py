
import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_name1='death_valley_02_2014.csv'
file_name2='sitka_weather_02_2014.csv'

dates_1=[]
highs_1=[]
lows_1=[]

with open(file_name1) as file_1:
    reader=csv.reader(file_1)
    header_row=next(reader)

    for row in reader:
        try:
            current_date=datetime.strptime(row[0],"%Y/%m/%d")
            high=int(row[1])
            low=int(row[3])
        except ValueError:
            print("Missing Date:",current_date)
        else:
            dates_1.append(current_date)
            highs_1.append(high)
            lows_1.append(low)

dates_2=[]
highs_2=[]
lows_2=[]

with open(file_name2) as file_2:
    reader=csv.reader(file_2)
    header_row=next(reader)

    for row in reader:
        try:
            current_date=datetime.strptime(row[0],"%Y/%m/%d")
            high=int(row[1])
            low=int(row[3])
        except ValueError:
            print("Missing Date:",current_date)
        else:
            dates_2.append(current_date)
            highs_2.append(high)
            lows_2.append(low)

fig=plt.figure(dpi=64,figsize=(25,12))

#plt.plot(dates_1,highs_1,c='red',alpha=0.5)
#plt.plot(dates_1,lows_1,c='blue',alpha=0.5)
#plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#plt.plot(dates_2,highs_2,c='orange',alpha=0.5)
#plt.plot(dates_2,lows_2,c='green',alpha=0.5)

plt.scatter(dates_1,highs_1,c='r',edgecolors=None,s=20)
plt.scatter(dates_1,lows_1,c='b',edgecolors=None,s=20)

plt.scatter(dates_2,highs_2,c='y',edgecolors=None,s=20)
plt.scatter(dates_2,lows_2,c='g',edgecolors=None,s=20)

plt.title("Daily High Temperature,2014",fontsize=48)
plt.xlabel("Date",fontsize=32)
fig.autofmt_xdate()
plt.ylabel("Temperature",fontsize=32)

plt.tick_params(axis='both',which='major',labelsize=32)

plt.show()

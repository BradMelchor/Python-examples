#!/usr/bin/env python3

from datetime import date,time,datetime, timedelta

def get_departure_time():
    departuredatestr = input("Estimated date of departure (YYYY-MM-DD): ")
    departuredate = datetime.strptime(departuredatestr, "%Y-%m-%d")
    return departuredate
def get_time():
    departuretimestr = input("Estimated date of departure (HH:MM AM/PM): ")
    departuretime = datetime.strptime(departuretimestr, "%I:%M %p")
    return departuretime
def main():
    choice = "y"
    while choice.lower() == "y":
        print("Arrival Time Estimator")
        print()
        #get input
        departure_date = get_departure_time()
        departure_time = get_time()
        miles = int(input("Enter miles: "))
        mph = int(input("Enter miles per hour: "))
        print()
        #calculate hours and minutes
        time =(miles / mph) * 60
        time = round(time)
        hours = time // 60
        time = time - (hours * 60)
        minutes = time // 1

        #calulate arrival

        arrivaltime = departure_time + timedelta(hours= int(hours), minutes = int(minutes))
        if departure_time.strftime("%H:%M %p") < arrivaltime.strftime("%H:%M %p"):
            day = 0
            arrivaldate = departure_date + timedelta(days = day)
        else:
            day = 1
            arrivaldate = departure_date + timedelta(days = day)
            

        #display
        print("Estimated travel time")
        print("Hours: " + str(hours))
        print("Minutes: " + str(minutes))
        print("Estimated date of arrival (YYYY-MM-DD): " + arrivaldate.strftime("%Y-%m-%d"))
        print("Estimated time of arrival (HH:MM AM/PM): " + arrivaltime.strftime("%I:%M %p"))

        choice = input("Continue? (y/n): ")
        print()


if __name__ == "__main__":
    main()

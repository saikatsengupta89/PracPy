import calendar
def which_day(day_str):
    month, day, year= day_str.split(" ")
    if (int(year) < 2000 or int(year) > 3000):
        print("INVALID")
    else:
        weekday= calendar.weekday(int(year), int(month), int(day))
        if(weekday==0):
            print("Monday")
        elif (weekday==1):
            print("Tuesday")
        elif (weekday==2):
            print("Wednesday")
        elif (weekday==3):
            print("Thursday")
        elif (weekday==4):
            print("Friday")
        elif (weekday==5):
            print("Saturday")
        else:
            print("Sunday")

if __name__=="__main__":
    inp=input("Enter day in format MM DD YYYY :")
    which_day(inp)
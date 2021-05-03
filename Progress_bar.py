#Responsible for Creating the Progress
import datetime
import calendar


def ProgressBar():
    fill = "▓"
    empty ="░"

    now = datetime.datetime.now()
    current_date = now.day
    total_days = calendar.monthrange(now.year, now.month)[1]

    percentage = round(current_date/total_days,2)
    print(current_date,total_days)

    bar = ""
    to_fill = int(percentage*15)
    to_empty = 15 - to_fill

    for i in range(to_fill):
        bar += fill
    
    for j in range(to_empty):
        bar += empty
    
    full_bar = bar + " " + str(int(percentage*100)) + "%" + " of " + calendar.month_name[now.month] + " is Complete!"


    return full_bar


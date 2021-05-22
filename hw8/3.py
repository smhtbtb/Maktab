# from datetime import time, timedelta, date, datetime
import datetime


def week_days():
    # t1_str = input('first date time with this format ->YYYY-MM-DD<-\n')
    t1_str = '2018-09-01'
    t1 = datetime.datetime.fromisoformat(t1_str)
    # t2_str = input('second date time with this format ->YYYY-MM-DD<-\n')
    t2_str = '2017-10-02'
    t2 = datetime.datetime.fromisoformat(t2_str)
    # day_num = input('which day do you want to show? (0-6)')
    day_num = 4
    week_day = int(day_num) + 1

    first_time = t1 if t1 < t2 else t2
    second_time = t2 if t1 < t2 else t1
    first_year = first_time.strftime(f'{str(first_time)[0]}{str(first_time)[1]}' + '%y')
    first_month = first_time.strftime('%m')
    first_day = first_time.strftime('%d')
    second_year = second_time.strftime(f'{str(second_time)[0]}{str(second_time)[1]}' + '%y')
    second_month = second_time.strftime('%m')
    second_day = second_time.strftime('%d')

    t11 = datetime.date(int(first_year), int(first_month), int(first_day))
    t22 = datetime.date(int(second_year), int(second_month), int(second_day))
    # print(t11, t22)

    # for i in range(20):
    i = 0
    while i >= 0:
        delta = datetime.timedelta(t11.isoweekday() + 7 * i)
        i += 1
        if t11 + delta < t22:
            yield t11 + delta
        else:
            break

    return 0


for i in week_days():
    print(i)


# baraye estefade az ye rooze daqiq bayad az isocalender() estefade knm

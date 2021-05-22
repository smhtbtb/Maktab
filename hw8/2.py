from datetime import time, timedelta, date, datetime
from persiantools.jdatetime import JalaliDate
import jdatetime


def time_():
    # t1 = input('first date time with this format ->YYYY-MM-DD HH:MM:SS<-\n')
    t1 = '2022-09-01 04:56:16'
    t1 = datetime.fromisoformat(t1)
    # t2 = input('second date time with this format ->YYYY-MM-DD HH:MM:SS<-\n')
    t2 = '2014-10-02 05:00:00'
    t2 = datetime.fromisoformat(t2)
    a = abs(t2 - t1).total_seconds()
    print(f'{a}seconds')
    # _________________________________________________________________________________
    # jalali (پ)
    first_time = t1 if t1 < t2 else t2
    second_time = t2 if t1 < t2 else t1
    # print(first_time, second_time)
    jalili_date_first = JalaliDate.fromtimestamp(int(first_time.timestamp()))
    jalili_date_second = JalaliDate.fromtimestamp(int(second_time.timestamp()))

    print(jalili_date_first, jalili_date_second)

    # _________________________________________________________________________________
    # changing time

    first_day = jalili_date_first.strftime('%d')
    second_day = jalili_date_second.strftime('%d')
    first_month = jalili_date_first.strftime('%m')
    second_month = jalili_date_second.strftime('%m')
    first_year = jalili_date_first.strftime('%y')
    second_year = jalili_date_second.strftime('%y')
    first_month_day = jalili_date_first.strftime('%m %d')
    second_month_day = jalili_date_second.strftime('%m %d')

    if '07 01' < first_month_day < '01 02':
        first_changing_time = 'Farvardin'
    else:
        first_changing_time = 'Mehr'

    if '01 01' <= second_month < '06 31':
        second_changing_time = 'Farvardin'
    else:
        second_changing_time = 'Mehr'

    # print(first_changing_time, second_changing_time, second_year, first_year)

    if first_changing_time == 'Farvardin' and second_changing_time == 'Farvardin':
        print('changing time happened ', 2 * (int(second_year) - int(first_year)) + 1, ' times')
    elif first_changing_time == 'Farvardin' and second_changing_time == 'Mehr':
        print('changing time happened ', 2 * (int(second_year) - int(first_year) + 1), ' times')
    elif first_changing_time == 'Mehr' and second_changing_time == 'Farvardin':
        print('changing time happened ', 2 * (int(second_year) - int(first_year)) - 1, ' times')
    elif first_changing_time == 'Mehr' and second_changing_time == 'Mehr':
        print('changing time happened ', 2 * (int(second_year) - int(first_year)) + 1, ' times')

    #
    # _________________________________________________________________________________
    # kabise
    first_year_miladi = first_time.strftime('%y')
    second_year_miladi = second_time.strftime('%y')

    for i in range((int(second_year_miladi) - int(first_year_miladi)) + 1):
        one_year_after = first_time + timedelta(days=365 * i)
        if one_year_after.strftime('%d') != (one_year_after - timedelta(days=365)).strftime('%d'):
            print(one_year_after.strftime('%y'))

    return 0


print(time_())

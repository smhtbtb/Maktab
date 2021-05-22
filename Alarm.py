from datetime import datetime, time, date
from time import sleep

if __name__ == '__main__':
    now_min = int(datetime.now().strftime('%M'))
    now_hour = int(datetime.now().strftime('%H'))
    now_second = int(datetime.now().strftime('%S'))

    time1 = input('enter: ')
    if len(time1) <= 2:
        if int(time1) <= 59:
            if now_second + int(time1) > 59:
                now_min += 1
                now_second -= 59
                if now_min > 59:
                    now_hour += 1
                    now_min -= 59

    try:
        if now_second + int(time1) < 10:
            time1 = time.fromisoformat(f"{now_hour}:{now_min}:0{now_second + int(time1)}")
        else:
            time1 = time.fromisoformat(f"{now_hour}:{now_min}:{now_second + int(time1)}")
        print(time1)
        today = str(date.today())
        # print(today)
        t1 = datetime.fromisoformat(f"{today} {time1}")
        print(t1)
        # print(type(t1))
        now = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        t0 = datetime.fromisoformat(now)
        while t0 <= t1:
            now = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            t0 = datetime.fromisoformat(now)
            # print(t0)
            print(t1 - t0)
            sleep(1)
            if t1 - t0 == '0:00:00':
                break
    except KeyboardInterrupt:
        print("\nFinished:")

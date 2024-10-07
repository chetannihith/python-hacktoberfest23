#countdowntimer
import time

timeinp = int(input("enter time for countdown in sec :"))

for x in reversed(range(1,timeinp)):
    hour = int(x/3600)
    minutes = int(x/60)%60
    seconds = x % 60
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!!!")
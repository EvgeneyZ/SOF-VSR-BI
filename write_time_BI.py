from datetime import datetime


with open('BI_time.txt', 'a') as f:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f.write(current_time + '\n')
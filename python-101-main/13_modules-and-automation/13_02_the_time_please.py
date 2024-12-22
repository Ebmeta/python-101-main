# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.
import datetime
current_date = datetime.date.today()
current_time = datetime.datetime.now().strftime('%H:%M')
print(f"Today is {current_date}, now it's {current_time}")

date = datetime.datetime.today()
print(date.strftime('%H:%M') , date.date() )
from datetime import datetime
current_date=datetime.datetime.now()
def display_current_datetime():
    Date=current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:",Date)

def calculate_future_date():
    D=int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + datetime.timedelta(days=D)
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(formatted_date)
def _main():
    display_current_datetime()
    calculate_future_date()
_main()

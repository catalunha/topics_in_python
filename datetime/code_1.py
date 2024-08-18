from datetime import datetime, timedelta

current_date = datetime.now()
print("current_date", current_date)
formatted_date = current_date.strftime("%d-%m-%Y %H:%M:%S")
print("formatted_date", formatted_date)


future_date = current_date + timedelta(days=7)
print("future_date", future_date)

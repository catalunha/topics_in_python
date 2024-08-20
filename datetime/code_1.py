import time
from datetime import datetime, timedelta

current_date = datetime.now()
print("current_date", current_date)
formatted_date = current_date.strftime("%d-%m-%Y %H:%M:%S")
print("formatted_date", formatted_date)


future_date = current_date + timedelta(days=7)
print("future_date", future_date)

# elapsed time
start_time: float = time.time()
# long process
value: int = 1
for i in range(100000):
    value += i
end_time: float = time.time()
elapsed_time = end_time - start_time
print("value", value)
print("elapsed_time", f"{elapsed_time:.6f} seconds")

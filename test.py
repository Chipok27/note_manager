from datetime import datetime
from calendar import monthrange

current_year = datetime.now().year
month = 2  # int(input())

days = monthrange(current_year, month)[1]
print(days)


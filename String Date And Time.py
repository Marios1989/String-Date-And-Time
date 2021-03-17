# Getting the Current Date and Time
from datetime import datetime
now = datetime.now()
print(now)

# Extracting Information
from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

# Hot Date
from datetime import datetime
now = datetime.now()

print('%02d/%02d/%04d' % (now.month, now.day, now.year))

# Pretty Time
from datetime import datetime
now = datetime.now()

print('%02d:%0d:%04d' % (now.hour, now.minute, now.second))

# Final
from datetime import datetime
now = datetime.now()

print('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))

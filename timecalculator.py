from datetime import datetime, timedelta

def getWeek(weekday,days_later):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    new_day_index = (days_of_week.index(weekday.capitalize()) + days_later) % 7
    return days_of_week[new_day_index]
"""
Struct inCapsulation example
"""
class MTime():
    def __init__(self, sTime, h, m, weekday = None):
        self.total_minutes = (sTime.hour * 60 + sTime.minute + h * 60 + m)
        self.new_hour = (self.total_minutes // 60) % 24
        self.new_minutes = self.total_minutes % 60
        self.days_later = self.total_minutes // (24 * 60)
        self.hours = self.new_hour % 12 or 12
        self.period = "AM" if self.new_hour < 12 else "PM"
        self.weekday = weekday
        if weekday:
          self.weekLine = f", {getWeek(weekday, self.days_later)}"
        self.nLine = f' (next day)' if self.days_later == 1 else f" ({self.days_later} days later)" if self.days_later > 1 else ""
    def __str__(self):
        tmp = f"{self.hours}:{str(self.new_minutes).zfill(2)} {self.period}"
        if self.weekday:
         tmp += self.weekLine

        tmp += self.nLine

        return tmp

def add_time(start, duration, weekday=None):
    sTime = datetime.strptime(start, "%I:%M %p")
    d = duration.split(":")
    h = int(d[0]) 
    m = int(d[1])
    # TODO: Refactoring struct name 
    mTime = MTime(sTime, h, m, weekday)
    new_time = str(mTime)
    return new_time
print(add_time('2:59 AM', '24:00', 'saturDay'))
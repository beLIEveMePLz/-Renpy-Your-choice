 #FONT DOOM
 #  _______ _                                  _    _____      _                _            
 # |__   __(_)                                | |  / ____|    | |              | |           
 #    | |   _ _ __ ___   ___    __ _ _ __   __| | | |     __ _| | ___ _ __   __| | __ _ _ __ 
 #    | |  | | '_ ` _ \ / _ \  / _` | '_ \ / _` | | |    / _` | |/ _ \ '_ \ / _` |/ _` | '__|
 #    | |  | | | | | | |  __/ | (_| | | | | (_| | | |___| (_| | |  __/ | | | (_| | (_| | |   
 #    |_|  |_|_| |_| |_|\___|  \__,_|_| |_|\__,_|  \_____\__,_|_|\___|_| |_|\__,_|\__,_|_|   
 #
 ############################################################################################

 # In "Time and Calendar" section simply count time flow. Time is counted from 
 #    @ miliseconds - use for quests "time is runnin"
 #    @ seconds minutes hours - use for normal time counting
 #    @ days months year - use for calendar purpose including leap year
 #    @ season - use for changing daytime during season like in winter dusk comes faster than in summer
 #    @ daytimes weekdays- use for depend on it a schelude of player and npc

 # This section works fine

 # To do:
 # >>Make an reset miliseconds if it is not an a quests
 # >>make an a counter from actual miliseconds to how much more miliseconds left
 # >>make a schelude section

init python:
    import datetime
    import random
    from math import floor

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    daytimes = ["Midnight", "Night", "Dawn", "Morning", "Noon", "Afternoon", "Dusk", "Night"]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    seasons = ["Winter", "Spring", "Summer", "Autumn"]


    class Clock(object):
        def __init__(self, year, month, day, hour=0, minute=0, second=0, millisecond=0):
            self._year = year 
            self._month = month 
            self._day = day 
            self._hour = hour 
            self._minute = minute 
            self._second = second 
            self._millisecond= millisecond
            self._weekday = None
            self._season = None
            self._season_nr = None
            self._daytime = None
            self._daytime_nr = None 
            self._weekend = None
            self._datetime = datetime.datetime(year, month, day, hour, minute, second, millisecond)
            self.datetimeToClock()
             
        def datetimeToClock(self):
            self._year = self._datetime.year
            self._month = self._datetime.month
            self._day = self._datetime.day
            self._hour = self._datetime.hour
            self._minute = self._datetime.minute
            self._second = self._datetime.second
            self._millisecond = self._datetime.microsecond
        
            __weekday = self._datetime.weekday()
            self._weekday = weekdays[__weekday]
            self._weekend = __weekday in [5, 6]
            
            self._season_nr = int(floor((self._month % 12)/3))
            self._season = seasons[self._season_nr]
            
            daytime_hours_all = [
                # Midnight Night Dawn Morning Noon Afternoon Dusk Night
                [ 0,       7,    8,   11,     12,  16,       17,  24 ], # Winter
                [ 0,       5,    6,   11,     12,  18,       19,  24 ], # Spring
                [ 0,       4,    5,   11,     12,  20,       21,  24 ], # Summer
                [ 0,       5,    6,   11,     12,  18,       19,  24 ], # Autumn
            ]
    
            daytime_hours = daytime_hours_all[self._season_nr]
            for i in range(len(daytime_hours)):
                if daytime_hours[i] < self._hour:
                    continue
                elif daytime_hours[i] >= self._hour:
                    self._daytime_nr = i
                    self._daytime = daytimes[i]
                    break
    
        def add(self, hours=0, minutes=0, seconds=0, milliseconds=0):
            delta = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)
            self._datetime += delta
            self.datetimeToClock()
    
        @property
        def nm(self):
            return months[self._month-1]
        
        @property
        def wk(self):
            return self._weekday
    
        @property
        def we(self):
            if self._weekend:
                weekend = "It's weekend"
            else:
                weekend = "It's working day"
            return weekend
    
        @property
        def sz(self):
            return self._season
        
        @property
        def dt(self):
            return self._daytime
                     
        @property
        def yy(self): 
            return "{:04d}".format(self._year)
  
        @property
        def mn(self):
            return "{:02d}".format(self._month)
                
        @property
        def dd(self):
            return "{:02d}".format(self._day)

        @property
        def hh(self):
            return "{:02d}".format(self._hour)
    
        @property
        def mm(self): 
            return "{:02d}".format(self._minute)
        
        @property
        def ss(self):
            return "{:02d}".format(self._second)

        @property
        def ms(self):
            return "{:04d}".format(self._millisecond)


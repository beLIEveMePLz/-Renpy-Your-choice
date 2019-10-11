init python:
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    seasons = ["winter","spring","summer","autumn"]
    SEASONS = {
    'winter': (11, 12, 1, 2, 3),
    'spring': (4, 5),
    'summer': (6, 7, 8),
    'autumn': (9, 10),
    }

    DAYTIMES = {
    'winter': {
        'midnight': (0, 1),
        'night': (1, 7),
        'dawn': (7, 8),
        'morning': (8, 11),
        'noon': (12, 13),
        'afternoon': (14, 17),
        'dusk': (18, 19),
        'night': (20, 23),
        },
    'spring': {
        'midnight': (0, 1),
        'night': (2, 6),
        'dawn': (6, 7),
        'morning': (7, 11),
        'noon': (12, 13),
        'afternoon': (14, 18),
        'dusk': (19, 20),
        'night': (20, 23),
        },
    'summer': {
        'midnight': (0, 1),
        'night': (2, 4),
        'dawn': (5, 6),
        'morning': (7, 11),
        'noon': (12, 13),
        'afternoon': (14, 17),
        'dusk': (18, 19),
        'night': (20, 23),
        },
    'autumn': {
        'midnight': (0, 1),
        'night': (2, 4),
        'dawn': (5, 6),
        'morning': (7, 11),
        'noon': (12, 13),
        'afternoon': (14, 17),
        'dusk': (18, 19),
        'night': (20, 23),
        },
    }


    class Clock(object):
        def __init__(self, year, month, day, hour, minute, second, millisecond, weekday, season, daytime):
            self._year = year 
            self._month = month 
            self._day = day 
            self._hour = hour 
            self._minute = minute 
            self._second = second 
            self._millisecond= millisecond
            self._weekday = weekday
            self._season = season
            self._daytime = daytime 
             
            
        def add(self , hours , minutes , seconds, milliseconds, ):

            if self._month < 3 :                                    # Week day segment
                __m = self._month + 12
                __y = self._year - 1
            else :
                __m = self._month
                __y = self._year
            __weekday = ((__y+__y/4-__y/100+__y/400+(13*__m+8)/5+self._day) % 7) - 1
            self._weekday = weekdays[__weekday]

            self._millisecond += milliseconds
            self._second += seconds                         #Adding time segment
            self._minute += minutes
            self._hour += hours

            self._second += self._millisecond // 1000
            self._minute += self._second // 60
            self._hour += self._minute // 60
            self._day += self._hour // 24

            if self._month in (1,3,5,7,8,10,12):            # Limit day segment
                if self._day > 31:
                    self._day = 1
                    self._month += 1
            elif self._month in (4,6,9,11):
                if self._day > 30:
                    self._day = 1
                    self._month += 1
            else :
                if (self._year % 4) == 0 and (self._year % 100) != 0 or (self._year % 400) == 0:
                    __d = 29                     
                else:
                    __d = 28

                if self._day > __d:
                    self._day = 1
                    self._month += 1

            if self._month > 12:
                self._month = 1
                self._year += 1
            
            self._millisecond = self._millisecond % 1000
            self._second = self._second % 60
            self._minute = self._minute % 60
            self._hour = self._hour % 24
            
            

        @staticmethod
        def overlapping_in_range(value, min_val, max_val): 
            if min_val < max_val:
                return min_val <= value < max_val
            elif min_val > max_val:
                return value >= min_val or value < max_val
 
        def get_season(month):
            for season, months in SEASONS.items():
                if month in months:
                    return SEASONS.key()


        def get_daytime(hour , month):
            # get the current season based on month
            season = get_season(month)
            # addressing DAYTIMES[season] to get the
            # sub-dict.
            for daytime, (mmin, mmax) in DAYTIMES[season].items():
                if overlapping_in_range(hour, mmin, mmax):
                    return daytime
            return ''

        
        @property                       # properting for easy use
        def wk(self):                   # [clk.wk] ---> weekday name
            return self._weekday                                    #Still not working

        @property
        def sz(self):                                    #Still not working
            season = str(self._season)
            return season[:]           
        
        @property
        def dt(self):                                    #Still not working
            daytime = str(self._daytime)
            return daytime[:]
                     
        @property
        def yy(self): 
            year = "000" + str(self._year)
            return year[-4:]        
              
        @property
        def mn(self):
            month = "0" + str(self._month)
            return month[-2:]
                
        @property
        def dd(self): 
            day = "0" + str(self._day)
            return day[-2:]
        
        @property
        def hh(self):
            hour = "0" + str(self._hour)
            return hour[-2:] 

        @property
        def mm(self): 
            minute = "0" + str(self._minute)
            return minute[-2:]
        
        @property
        def ss(self):
            second = "0" + str(self._second)
            return second[-2:]


        @property
        def ms(self):
            millisecond = "000" + str(self._millisecond)
            return millisecond[-4:]


        
        

#def __init__(self, year, m, da, ho, m, s, m, weekday, season,      daytime)   
default clk = Clock(2019, 8, 25, 10, 0, 0, 0,"1st day", "1st season", None)

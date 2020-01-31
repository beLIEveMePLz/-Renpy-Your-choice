
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
        def __init__(self, year, month, day, hour, minute, second, millisecond):
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

# #################################################
#  _    _            _   _               
# | |  | |          | | | |              
# | |  | | ___  __ _| |_| |__   ___ _ __ 
# | |/\| |/ _ \/ _` | __| '_ \ / _ \ '__|
# \  /\  /  __/ (_| | |_| | | |  __/ |   
#  \/  \/ \___|\__,_|\__|_| |_|\___|_|   
# ################################################
    Temperatures = ["Freezing", "Cold", "Unconfortable", "Confortable", "Hot", "Scorcher"]
    Winds = ["Without", "Light", "Medium", "Strong", "Hurracane"]
    Clouds = ["Sunny", "Slightly Cloudy", "Cloudly", "Overcast" ]
    Atmosperics = ["Clear", "Breeze", "Rain", "Storm"]
    Temp_list = []
    Weather_days = ["Today","Tomorrow","2nday","3rday","4thday","5thday","6thday","7thday","8thday","9thday","10thday"] 
    
    
    class Weather(Clock):
        def __init__(self, year, month, day, hour, minute, second, millisecond):
            super(Weather, self).__init__(year, month, day, hour, minute, second, millisecond)
            self.temp_out = None
            self.wind = None
            self.cloud = None
            self.phenomen = None
            self.change_weather()
        
        def change_weather(self):
            temp_min_max = [
                [-256, 1450], # else
                [-10, 15], # Jan
                [-8, 20], # Feb
                [-1, 23], # Mar
                [6, 27], # Apr
                [10, 32], # May
                [15, 36], # Jun
                [16, 37], # Jul
                [16, 38], # Aug
                [10, 30], # Sep
                [0, 26], # Oct
                [-5, 21], # Nov
                [-25, 15], # Dec
            ]
            min_temp, max_temp = temp_min_max[self._month]
    
            if not Temp_list:
                while len(Temp_list) < 11:
                    day_temp = random.randint(min_temp, max_temp)
                    Temp_list.append(day_temp)
            else:
                Temp_list.pop(0)
                day_temp = random.randint(min_temp, max_temp)
                Temp_list.append(day_temp)
                
            self.temp_out = Temp_list[0]
            
        @property
        def temp(self):
            actual_temp = self.temp_out
            
            temp_daytime_mode = [
                # Midnight Night Dawn Morning Noon Afternoon Dusk Night
                  -2,      -5,   -6,  -3,     3,   5,        2,   0
            ]
            return str(actual_temp + temp_daytime_mode[self._daytime_nr])

        def add(self, hours=0, minutes=0, seconds=0, milliseconds=0):
            old_day = self._day
            super(Weather, self).add(hours, minutes, seconds, milliseconds)
            if old_day != self._day:
                self.change_weather()
        



#######################################################
#  _____                      _                       #
# |     |                    | |                      #
#   | |  _ ____   _____ _ __ | |_ ___  _ __ _   _     #
#   | | | '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |    #
#  _| |_| | | \ V /  __/ | | | || (_) | |  | |_| |    #
# |_____|_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |    #
#                                            __/ |    #
#                                           |___/     #
#                                                     #
#######################################################

    # sizes = ["Tiny", "Small", "Medium", "Big", "Huge"]

    # class Item(object):
    #     def __init__(self, name, quantity, volume, size, weight, spiece, info, price, craft, thumb, image):
    #         self.name = name            #1 Nazwa            Name of item for identification purpose
    #         self.quantity = quantity    #2 Ilość            Amount of items we have                               Ex. 15xbatteries
    #         self.volume = volume        #3 Objetosc         Amount of volume taken from Container                 all items(volume)<=max_volume
    #         self.size = size            #4 Rozmiar          Amount of volume taken from Container                 (huge, big, medium, small, tiny) huge>big>medium>small>tiny
    #         self.weight = weight        #5 Ciężar           Strengh(actual_max_weight)=>weight<max weight container
    #         self.spiece = spiece        #6 Rodzaj           Type of item
    #         self.info = info            #7 Informacje       Infos         
    #         self.price = price          #8 Cena             Price
    #         self.craft = craft          #9 Tworzenie        Crafting
    #         self.thumb = thumb          #10 Miniaturka      Thumbinal
    #         self.image = image          #11 Obrazek         Bigger thumb 

    # class Container():
    #     def __init__(self, max_size, item_volume, max_volume, max_weight, spiece, info, image, ):
    #         self.inventory = []                 # List for items
    #         self.max_size = max_size 
           #  self.item_volume =item_volume
    #         self.max_volume = max_volume        # Max amount of total volume of items
    #         self.max_weight = max_weight    
    #         self.spiece = spiece
    #         self.image = image

    #     def add(Item):
            #  for j in k:
              #    self.item_volume = self.volume*self.quantity


    #         if size <= max_size:
             #     if self.
                  




            



#def __init__(self, year, m, da, ho, m, s, m,ms)   
default calendar = Weather(2019, 8, 25, 10, 0, 0, 0)


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

    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    daytimes = ["Midnight", "Night", "Dawn", "Morning", "Noon", "Afternoon", "Dusk", "Night"]
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
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
    
            if self._weekday in ("Saturday","Sunday"):
                self._weekend = True
            else:
                self._weekend = False
    
            season_nr = int(floor((self._month % 12)/3))
            self._season = seasons[season_nr]
            
            # daytimes = ["Midnight", "Night", "Dawn", "Morning", "Noon", "Afternoon", "Dusk", "Night"]
            daytime_hours_all = [
                [0, 7, 8, 11, 12, 16, 17, 24], 
                [0, 5, 6, 11, 12, 18, 19, 24],
                [0, 4, 5, 11, 12, 20, 21, 24],
                [0, 5, 6, 11, 12, 18, 19, 24],
            ]
    
            daytime_hours = daytime_hours_all[season_nr]
            for i in range(len(daytime_hours)):
                if daytime_hours[i] < self._hour:
                    continue
                elif daytime_hours[i] >= self._hour:
                    self._daytime_nr = i
                    self._daytime = daytimes[i]
                    break
    
        def add(self, hours, minutes, seconds, milliseconds):
            delta = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)
            self._datetime += delta
            self.datetimeToClock()
    
        @property
        def nm(self):
            name_month = str(months[self._month-1])
            return name_month
        
        @property                       # properting for easy use
        def wk(self):                   # [clk.wk] ---> weekday name
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
            season = str(self._season)
            return season           
        
        @property
        def dt(self):
            daytm = str(self._daytime)
            return daytm
                     
        @property
        def yy(self): 
            year = "000" + str(self._year)
            return year[-4:]        
              
        @property
        def mn(self):
            month ="00" +str(self._month)
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

# #################################################
#  _    _            _   _               
# | |  | |          | | | |              
# | |  | | ___  __ _| |_| |__   ___ _ __ 
# | |/\| |/ _ \/ _` | __| '_ \ / _ \ '__|
# \  /\  /  __/ (_| | |_| | | |  __/ |   
#  \/  \/ \___|\__,_|\__|_| |_|\___|_|   
# ################################################
    Temperatures = ("Freezing", "Cold", "Unconfortable", "Confortable", "Hot", "Scorcher")
    Winds = ("Without", "Light", "Medium", "Strong", "Hurracane")
    Clouds = ("Sunny", "Slightly Cloudy", "Cloudly", "Overcast" )
    Atmosperics = ("Clear", "Breeze", "Rain", "Storm")
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
                [-256, 1450],
                [-10, 15],
                [-8, 20],
                [-1, 23],
                [6, 27],
                [10, 32],
                [15, 36],
                [16, 37],
                [16, 38],
                [10, 30],
                [0, 26],
                [-5, 21],
                [-25, 15],
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
            temp_daytime_mode = [-2, -5, -6, -3, 3, 5, 2, 0]
            return str(actual_temp + temp_daytime_mode[self._daytime_nr])

        def add(self, hours, minutes, seconds, milliseconds):
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
    #     def __init__(self, max_size, max_volume, max_weight, spiece, info, image, ):
    #         self.inventory = []                 # List for items
    #         self.max_size = max_size            # 
    #         self.max_volume = max_volume        # Max amount of total volume of items
    #         self.max_weight = max_weight    
    #         self.spiece = spiece
    #         self.image = image

    #     def add(Item):
    #         pass
    #         #if max_size == sizes[5]:




            



#def __init__(self, year, m, da, ho, m, s, m,ms)   
default calendar = Weather(2019, 8, 25, 10, 0, 0, 0)
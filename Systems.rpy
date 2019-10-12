
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
    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    daytimes = ["Midnight", "Night", "Dawn", "Morning", "Noon", "Afternoon", "Dusk", "Night"]
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    seasons = ["Winter", "Spring", "Summer", "Autumn"]
    

    class Clock(object):
        def __init__(self, year, month, day, hour, minute, second, millisecond, weekday, season, daytime, weekend):
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
            self._weekend = weekend
             
            
        def add(self , hours , minutes , seconds, milliseconds):

            if self._month < 3 :                                    # Week day segment
                __m = self._month + 12
                __y = self._year - 1
            else :
                __m = self._month
                __y = self._year
            __weekday = ((__y+__y/4-__y/100+__y/400+(13*__m+8)/5+self._day) % 7) - 1

            self._weekday = weekdays[__weekday]
            if self._weekday in ("Saturday","Sunday"):
                self._weekend = True
            else:
                self._weekend = False

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


            if self._month in (12,1,2):
                self._season = seasons[0]
                if self._hour == 0:
                    self._daytime = daytimes[0]
                if self._hour > 0 and self._hour < 7:
                    self._daytime = daytimes[1]
                if self._hour > 7 and self._hour < 8:
                    self._daytime = daytimes[2]
                if self._hour > 8 and self._hour < 11:
                    self._daytime = daytimes[3]
                if self._hour == 12:
                    self._daytime = daytimes[4]
                if self._hour >= 13 and self._hour < 16:
                    self._daytime = daytimes[5]
                if self._hour > 16 and self._hour < 17:
                    self._daytime = daytimes[6]
                if self._hour > 17 and self._hour < 24:
                    self._daytime = daytimes[7]
            if self._month in (3,4,5):
                self._season = seasons[1]
                if self._hour == 0:
                    self._daytime = daytimes[0]
                if self._hour > 0 and self._hour < 5:
                    self._daytime = daytimes[1]
                if self._hour > 5 and self._hour < 6:
                    self._daytime = daytimes[2]
                if self._hour > 6 and self._hour < 11:
                    self._daytime = daytimes[3]
                if self._hour == 12:
                    self._daytime = daytimes[4]
                if self._hour >= 13 and self._hour < 18:
                    self._daytime = daytimes[5]
                if self._hour > 18 and self._hour < 19:
                    self._daytime = daytimes[6]
                if self._hour > 19 and self._hour < 24:
                    self._daytime = daytimes[7]
            if self._month in (6,7,8):
                self._season = seasons[2]
                if self._hour == 0:
                    self._daytime = daytimes[0]
                if self._hour > 0 and self._hour < 4:
                    self._daytime = daytimes[1]
                if self._hour > 4 and self._hour < 5:
                    self._daytime = daytimes[2]
                if self._hour > 5 and self._hour < 11:
                    self._daytime = daytimes[3]
                if self._hour == 12:
                    self._daytime = daytimes[4]
                if self._hour >= 13 and self._hour < 20:
                    self._daytime = daytimes[5]
                if self._hour > 20 and self._hour < 21:
                    self._daytime = daytimes[6]
                if self._hour > 21 and self._hour < 24:
                    self._daytime = daytimes[7]
            if self._month in (9,10,11):
                self._season = seasons[3]
                if self._hour == 0:
                    self._daytime = daytimes[0]
                if self._hour > 0 and self._hour < 5:
                    self._daytime = daytimes[1]
                if self._hour > 5 and self._hour < 6:
                    self._daytime = daytimes[2]
                if self._hour > 6 and self._hour < 11:
                    self._daytime = daytimes[3]
                if self._hour == 12:
                    self._daytime = daytimes[4]
                if self._hour >= 13 and self._hour < 18:
                    self._daytime = daytimes[5]
                if self._hour > 18 and self._hour < 19:
                    self._daytime = daytimes[6]
                if self._hour > 19 and self._hour < 24:
                    self._daytime = daytimes[7]


        @property
        def nm(self):
            name_month = str(months[self.month])
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
    Temp_dict = []
    Weather_days = ["Today","Tomorrow","2nday","3rday","4tday","5tday","6tday","7tday","8tday","9tday","10tday"] 
    

    class Weather(Clock):
        def __init__(self, temp_out):#, wind, cloud, phenomen):
            self.temp_out = temp_out
            # self._wind = wind
            # self._cloud = cloud
            # self._phenomen = phenomen
        
        def change_weather(self, temp_out):#, actual_wind, actual_atmospheric, actual_phenomen):

            if self._month == 1:
                min_temp = -10
                max_temp = 15
            elif self._month == 2:
                min_temp = -8
                max_temp = 20
            elif self._month == 3:
                min_temp = -1
                max_temp = 23
            elif self._month == 4:
                min_temp = 6
                max_temp = 27
            elif self._month == 5:
                min_temp = 10
                max_temp = 32
            elif self._month == 6:
                min_temp = 15
                max_temp = 36
            elif self._month == 7:
                min_temp = 16
                max_temp = 37
            elif self._month == 8:
                min_temp = 16
                max_temp = 38
            elif self._month == 9:
                min_temp = 10
                max_temp = 30
            elif self._month == 10:
                min_temp = 0
                max_temp = 26
            elif self._month == 11:
                min_temp = -5
                max_temp = 21
            elif self._month == 12:
                min_temp = -25
                max_temp = 15
            else:
                min_temp = -256
                max_temp = 1450

            if Temp_list is None:
                while len(Temp_list) < 11:
                    day_temp = random.randrange(min_temp, max_temp)
                    Temp_list.append(day_temp)
            elif self._hour == 0:
                Temp_list.pop(0)
                day_temp = random.randrange(min_temp, max_temp)
                Temp_list.append(day_temp)
            today_temp = Temp_list[0]
            if self._daytime == daytimes[0]:
                self.temp_out = today_temp -2 
            elif self._daytime == daytimes[1]:
                self.temp_out = today_temp -5
            elif self._daytime == daytimes[2]:
                self.temp_out = today_temp -6
            elif self._daytime == daytimes[3]:
                self.temp_out = today_temp -3
            elif self._daytime == daytimes[4]:
                self.temp_out = today_temp +3
            elif self._daytime == daytimes[5]:
                self.temp_out = today_temp +5
            elif self._daytime == daytimes[6]:
                self.temp_out = today_temp +2
            elif self._daytime == daytimes[7]:
                self.temp_out = today_temp 
        @property
        def temp(self):
            Temperature = str(self.temp_out)
            return Temperature



        







#######################################################
#  _____                      _                       #
# |     |                    | |                      #
#   | |  _ ____   _____ _ __ | |_ ___  _ __ _   _     #
#   | | | '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |    #
#  _| |_| | | \ V /  __/ | | | || (_) | |  | |_| |    #[;/]
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
default clk = Clock(2019, 8, 25, 10, 0, 0, 0, "A Day", "An season", "An daytime", " ")
default wea = Weather(0)

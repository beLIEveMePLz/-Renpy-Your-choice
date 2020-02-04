# #################################################
#  _    _            _   _               
# | |  | |          | | | |              
# | |  | | ___  __ _| |_| |__   ___ _ __ 
# | |/\| |/ _ \/ _` | __| '_ \ / _ \ '__|
# \  /\  /  __/ (_| | |_| | | |  __/ |   
#  \/  \/ \___|\__,_|\__|_| |_|\___|_|   
# ################################################
init python:

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


default calendar = Weather(2019, 8, 25, 10, 0, 0, 0)
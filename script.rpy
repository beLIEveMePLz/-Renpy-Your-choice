
#Setting

$turtorial = False 


init:
    $ pn = ""
    $ psn = ""
    $ pal = ""

#Characters


define p = DynamicCharacter("pn", color="#fd9501") 

define ps = DynamicCharacter("psn")
define pa = DynamicCharacter("pal")

define d = Character("Douchebags")
define t = Character("Teacher")
define j = Character("Jennifer", who_color ="#524de1")
define cr = Character("Creator", color = "#00F429")
define dc = Character("Dot")

# The game starts here.

label start:

    while True:
        "Day : [calendar.yy]/[calendar.mn]/[calendar.dd]" 
        "Weekday : [calendar.wk] [calendar.we]   Season : [calendar.sz]    Daytime : [calendar.dt] "
        "Temperaure [calendar.temp]"
        "Time : [calendar.hh]:[calendar.mm]   Seconds : [calendar.ss] / [calendar.ms]"
        menu:
            "2 Hours":
                $calendar.add(2,0,0,0)
                jump start
            "Day":
                $calendar.add(24,0,0,0)
                jump start
            "10 Day":
                $calendar.add(240,0,0,0)
                jump start
            "Pass":
                jump here

        return 

        
    return

    label here:
        cr "The story has begun"
        cr "And how will be..."
        cr "It's Your choice"
        cr "Where would you begin?"
        menu:
            "Introduction Day":
                jump story
            "Pass turtorials":
                jump game
            "Change name":
                jump nameMc

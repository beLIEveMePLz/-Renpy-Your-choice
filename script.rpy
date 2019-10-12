
#Setting


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
define cr = Character("Creator")
define dc = Character("Amount of córkas")

# The game starts here.

label start:

    while True:
        "Day : [clk.yy]/[clk.mn]/[clk.dd]" 
        "Weekday : [clk.wk] [clk.we]   Season : [clk.sz]    Daytime : [clk.dt] "
        "Temperaure [wea.temp]"
        "Time : [clk.hh]:[clk.mm]   Seconds : [clk.ss] / [clk.ms]"
        menu:
            "Day":
                $clk.add(24,0,0,0)
                jump start
            "10 Day":
                $clk.add(240,0,0,0)
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

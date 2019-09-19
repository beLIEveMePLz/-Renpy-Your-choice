###
#Punkt w którym wszystko sie zaczyna
#Pierwszy Start
###



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
        "Weekday : [clk.wk]    Season : [clk.sz]    Daytime : [clk.dt]"
        "Time : [clk.hh]:[clk.mm]   Seconds : [clk.ss] / [clk.ms]"
        menu:
            "meconds 1":
                $clk.add(0,0,0,1)
                jump start
            "meconds 10":
                $clk.add(0,0,0,10)
                jump start
            "meconds 900":
                $clk.add(0,0,0,900)
                jump start
            "Seconds 5":
                $clk.add(0,0,5,0)
                jump start
            "Minutes 1":
                $clk.add(0,1,0,0)
                jump start
            "Minutes 15":
                $clk.add(0,15,0,0)
                jump start
            "Hour 1":
                $clk.add(1,0,0,0)
                jump start
            "Hour 6":
                $clk.add(6,0,0,0)
                jump start
            "Hour 12":
                $clk.add(12,0,0,0)
                jump start
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

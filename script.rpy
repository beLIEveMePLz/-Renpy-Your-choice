#Setting




init:
    $ intro = False 
    $ pn = ""
    $ psn = ""
    $ pal = ""

#Characters


define plr_name = DynamicCharacter("pn", color="#fd9501") 

define plr_surname = DynamicCharacter("psn")
define plr_alias = DynamicCharacter("pal")

define d = Character("Douchebags")
define t = Character("Teacher")
define j = Character("Jennifer", who_color ="#524de1")
define cr = Character("Creator", color = "#00F429")
define dc = Character("Dot")

# The game starts here.

label start:
    show screen TestScreen


    while True:
        
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
                jump storytell
            "Pass turtorials":
                jump game
            "Change name":
                jump nameMc


    

    

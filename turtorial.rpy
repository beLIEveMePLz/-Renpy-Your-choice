label nameMc:
    $ pn = renpy.input("My name is.. ", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", )
    if pn == "":
        cr "What? An no name? No no..."
        jump nameMc
    if pn is not None:
        $ check_name = len(pn)
        if check_name == 1:
            "I dont remember that my name is soo short"
            jump nameMc
        if check_name >= 15:
            "I dont remember that my name is soo long"
            jump nameMc
    $ p = pn.title()
    # Yay, your name doesn't hit any conditions. You can name them that!
    "[p]...!"
    "Hmm It is for sure [p]?"
    menu:
        
        "Oh! No! It is not [p]":
            jump nameMc
        "Oh! Yes!It is [p]":
            if turtorial:
                if psn == "":
                    jump surnameMc
                else:
                    jump name_chk
            else:
                jump nameask
    
label surnameMc:
    $ psn = renpy.input("So my name is [p] and surname is...", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", )
    if psn == "":
        "What? An no surname? No no..."
        jump surnameMc
    if psn is not None:
        $ check_surname = len(psn)
        if check_surname == 1:
            "I dont remember that my surname is soo short"
            jump surnameMc
        if check_surname >= 15:
            "I dont remember that my surname is soo long"
            jump surnameMc
    $ psn = psn.title()
    # Yay, your name doesn't hit any conditions. You can name them that!
    "[p] [ps]...!"
    "Hmm is for sure [p] [ps]?"
    menu:
        
        "Oh! No! It is not [ps]":
            jump surnameMc
        "Oh! It is [ps] but not [p]":
            jump nameMc
        "Oh! Yes!It is [p] [ps]":
            if turtorial:
                if pal == "":
                    "I have a nickname too and friends always called me by this"
                    jump aliasMc
                else:
                    jump name_chk
            else:
                jump surnameask
            
    
label aliasMc:
    $ pal = renpy.input("So my nickname is..", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", )
    if pal == "":
        "Noo! I have a nickname!"
        jump aliasMc
    if pal is not None:
        $ check_alias = len(pal)
        if check_alias == 1:
            "I dont remember that my nickname is soo short"
            jump aliasMc
        if check_name >= 15:
            "I dont remember that my nickname is soo long"
            jump aliasMc
    $ pal = pal.title()
    # Yay, your name doesn't hit any conditions. You can name them that!
    "[p] [ps] aka [pa]!"
    if turtorial:
        jump name_chk
    else:
        jump aliasask
    
    label name_chk:
        menu:
            "Yes i remember. I was always [p] [pa] [ps]":
                jump continuturt
            "Nope! My name is not right":
                jump nameMc
            "Nope! My surname is not right":
                jump surnameMc
            "Nope! My nickname is not right":
                jump aliasMc
    
    
    
    # game continues  
label storytell:
        
         
    
    "Have u wish to see the past?"
    menu:
        "Just play!":
            jump game
        
        "I wish to see some past":
            jump turtorial

label turtorial:
    "Let me start from begin"
    ####### STORY #############
    $ turtorial = True
    jump nameMc

label continuturt:
    


label game:
    
    scene black
    j "Time to wake up honey <3"
    j "You dont wanna be late"
    p "What?"
    scene home_room_bed_lay
    with dissolve
    p "Where am i?"
    p "Oh ok i am in my room"
    if turtorial:
        jump nameask
    else:
        "But hey?"
        "What was my name?"
        jump nameMc
    
    label nameask:
        j "[p]! Breakfast!"
        "Oh that lovely voice"
        "Cannot wait to see you"
        p " I/'m comming!"
    
    "Meet some dushbags"
    d "How they called you"
    if turtorial:
        jump aliasask
    else:
        jump aliasMc
    
    label aliasask:
    p "[pa]"
    p "Get off my way"
    p "So mr [pa], can go to school"
    
    "School"
    t "We have new student"
    t "Introduce yourself"
    p "Hi I am [p]"
    t "Just [p] ?"
    p "No you can call me [pa]"
    t "The question was..."
    t "What is your surname"
    if turtorial:
        jump surnameask
    else:
        jump surnameMc
    
    label surnameask:
    p "[ps]"
    p "[p] [ps]"
    p "aka [pa]!"




    
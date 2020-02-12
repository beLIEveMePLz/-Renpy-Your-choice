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
    "[plr]...!"
    "Hmm It is for sure [plr]?"
    menu:
        
        "Oh! No! It is not [plr]":
            jump nameMc
        "Oh! Yes!It is [plr]":
            if intro:
                if psn == "":
                    jump surnameMc
                else:
                    jump name_chk
            else:
                jump nameask
    
label surnameMc:
    $ psn = renpy.input("So my name is [plr] and surname is...", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", )
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
    "[plr] [plr_surname]...!"
    "Hmm is for sure [plr] [plr_surname]?"
    menu:
        
        "Oh! No! It is not [plr_surname]":
            jump surnameMc
        "Oh! It is [plr_surname] but not [plr]":
            jump nameMc
        "Oh! Yes!It is [plr] [plr_surname]":
            if intro:
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
    "[plr] [plr_surname] aka [plr_alias]!"
    if intro:
        jump name_chk
    else:
        jump aliasask
    
    label name_chk:
        menu:
            "Yes i remember. I was always [plr] [plr_alias] [plr_surname]":
                jump storytell
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
            jump introduction

label introduction:
    "Let me start from begin"
    "My life.."
    "So fucked.."
    "..."
    "I'v grow up child care home"
    "They found me by the door"
    "Seen a young women running far"
    "She wanna to be unrecognized"
    "Soo i was alone asking myself why she did this"
    "Grow up with fate that someone take me"
    "No one show"
    "I spent 17 years there dreamed of a normal home"
    "On my 18th birthday a miracle happened"
    "She visited the orphanage"
    "Nice looking brunette"
    "Look on me and said"
    j "Would you like to have a normal house?"
    "I agree without asking"
    "Now my day look like this"

    $ intro = True
    jump nameMc


label game:
    
    scene black
    j "Time to wake up honey <3"
    j "You dont wanna be late"
    plr "What?"
    plr "Where am i?"
    plr "Oh ok i am in my room"
    if intro == True:
        jump nameask
    else:
        "But hey?"
        "What was my name?"
        jump nameMc
    
    label nameask:
        j "[plr]! Breakfast!"
        "Oh that lovely voice"
        "Cannot wait to see you"
        plr " I'm comming!"
    
    "Meet some dushbags"
    d "How they called you"
    if intro == True:
    plr "No you can call me [plr_alias]"
    t "The question was..."
    t "What is your surname"
    if intro == True:
            jump surnameask
    else:
        jump surnameMc
    
    label surnameask:
    plr "[plr_surname]"
    plr "[plr] [plr_surname]"
    plr "aka [plr_alias]!"




    

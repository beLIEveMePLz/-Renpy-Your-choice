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
    "[plr_name]...!"
    "Hmm It is for sure [plr_name]?"
    menu:
        
        "Oh! No! It is not [plr_name]":
            jump nameMc
        "Oh! Yes!It is [plr_name]":
            if tuto:
                if psn == "":
                    jump surnameMc
                else:
                    jump name_chk
            else:
                jump nameask
    
label surnameMc:
    $ psn = renpy.input("So my name is [plr_name] and surname is...", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", )
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
    "[plr_name] [plr_surname]...!"
    "Hmm is for sure [plr_name] [plr_surname]?"
    menu:
        
        "Oh! No! It is not [plr_surname]":
            jump surnameMc
        "Oh! It is [plr_surname] but not [plr_name]":
            jump nameMc
        "Oh! Yes!It is [plr_name] [plr_surname]":
            if tuto:
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
    "[plr_name] [plr_surname] aka [plr_alias]!"
    if tuto:
        jump name_chk
    else:
        jump aliasask
    
    label name_chk:
        menu:
            "Yes i remember. I was always [plr_name] [plr_alias] [plr_surname]":
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
            jump tutorial

label tutorial:
    "Let me start from begin"
    "My life.."
    "So fucked.."
    "Because of best choices of my parents"
    "I am here"
    "..."
    "My parents meets on studies"
    "After studies they get married"
    "Short after i were born"
    "They were happy"
    "Thats what i was remember"
    "The true was different"
    "Parents always hide before me when they fight"
    "After one fight father leave"
    "They were separated and short after.."
    "The divorce papers come"
    "Mom and Dad were so love and now were hate eachother"
    "From now on I was made to make choices or mom or dad"
    "Mom never forgive dad so i never mention about him.."
    "Dad was clearly hate her soo didn't mention about her to him"
    "Mom never grabbed yourself"
    "But dad meet that [j]"
    "[j] was divorced. She had [dc] daughters"
    "They were in love soo Dad and [j] decide to marry "
    "I remember that day"
    "I was church witness of my dad"
    ""
    
    "My dad try to make normal life"
    "He tried so he almost married"
    "Rozwodnik poznaje kobiete co ma ze 3 córki"
    "Rodzi się rodzinna więź czego dowodem jest ślub"    
    "Po 3 dniach "
    "Na kawalerskim dzwoni mama "
    "Błaga by przyjechał"
    "Że zdarzylo sie cos strasznego i potrzebuje pomocy"
    "Ojciec pojechał do matki i okazało się że ta jest w cięzkim stanie"
    "Zostajesz sierotą z niedoszła macochą"
    "Ona bierze Cie pod swój dach"
    "Jest jej zal ze zostales sierota"
    "A ona Ci może pomoc"
    "I oczywiscie przypominasz jej ojca ktorego kochała"
    $ tuto = True
    jump nameMc


label game:
    
    scene black
    j "Time to wake up honey <3"
    j "You dont wanna be late"
    plr_name "What?"
    plr_name "Where am i?"
    plr_name "Oh ok i am in my room"
    if tuto == True:
        jump nameask
    else:
        "But hey?"
        "What was my name?"
        jump nameMc
    
    label nameask:
        j "[plr_name]! Breakfast!"
        "Oh that lovely voice"
        "Cannot wait to see you"
        plr_name " I/'m comming!"
    
    "Meet some dushbags"
    d "How they called you"
    if tuto == True:
            jump aliasask
    else:
        jump aliasMc
    
    label aliasask:
    plr_name "[plr_alias]"
    plr_name "Get off my way"
    plr_name "So mr [plr_alias], can go to school"
    
    "School"
    t "We have new student"
    t "Introduce yourself"
    plr_name "Hi I am [plr_name]"
    t "Just [plr_name] ?"
    plr_name "No you can call me [plr_alias]"
    t "The question was..."
    t "What is your surname"
    if tuto == True:
            jump surnameask
    else:
        jump surnameMc
    
    label surnameask:
    plr_name "[plr_surname]"
    plr_name "[plr_name] [plr_surname]"
    plr_name "aka [plr_alias]!"




    

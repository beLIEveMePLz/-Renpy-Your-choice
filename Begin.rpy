label story:
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
    jump game

label nameMc:
    $ pn = renpy.input("My name is.. ", allow=" 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", )
    if pn == "":
        "What? An no name? No no..."
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
        cr "What? An no surname? No no..."
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









    
#######################################################
#  _____                      _                       #
# |     |                    | |                      #
#   | |  _ ____   _____ _ __ | |_ ___  _ __ _   _     #
#   | | | '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |    #
#  _| |_| | | \ V /  __/ | | | || (_) | |  | |_| |    #
# |_____|_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |    #
#                                            __/ |    #
#                                           |___/     #
#                                                     #
#######################################################
init python:
    sizes = ("Tiny", "Small", "Medium", "Big", "Huge")
    Inventory = []

    class Item(object):
        def __init__(self, name, quantity, volume, size, weight, spiece, info, price, craft, thumb, image):
            self.name = name            #1 Nazwa            Name of item for identification purpose
            self.quantity = quantity    #2 Ilość            Amount of items we have                               Ex. 15xbatteries
            self.volume = volume        #3 Objetosc         Amount of volume taken from Container                 all items(volume)<=max_volume
            self.size = size            #4 Rozmiar          Amount of volume taken from Container                 (huge, big, medium, small, tiny) huge>big>medium>small>tiny
            self.weight = weight        #5 Ciężar           Strengh(actual_max_weight)=>weight<max weight container
            self.spiece = spiece        #6 Rodzaj           Type of item
            self.info = info            #7 Informacje       Infos         
            self.price = price          #8 Cena             Price
            self.craft = craft          #9 Tworzenie        Crafting
            self.thumb = thumb          #10 Miniaturka      Thumbinal
            self.image = image          #11 Obrazek         Bigger thumb 

    class Container():
        def __init__(self, max_size, item_volume, max_volume, max_weight, spiece, info, image, ):
            
            self.max_size = max_size 
            self.item_volume = item_volume
            self.current_volume = current_volume
            self.max_volume = max_volume         #Max amount of total volume of items
            self.item_weight = item_weight
            self.current_weight = current_weight
            self.max_weight = max_weight
            self.current_quantity = current_quantity
            self.spiece = spiece
            self.image = image

        def add(Item):
            self.item_volume + self.volume*self.quantity
            self.current_volume = self.current_volume+self.item_volume
            self.item_weight + self.weight*self.quantity
            self.current_weight = self.current_weight+self.item_weight
            
            if size > max_size:
                "This will not fit"
            elif self.current_volume > self.max_volume:
                self.current_volume = self.current_volume-self.item_volume
                "This is too big"
            elif self.current_weight > self.max_weight:
                self.current_weight = self.current_weight-self.item_weight
                "This is too heavy"
            else:
                self.current_volume = self.current_volume+self.item_volume
                self.current_weight = self.current_weight+self.item_weight
                self.current_quantity = self.quantity + self.current_quantity
                self.Inventory.append
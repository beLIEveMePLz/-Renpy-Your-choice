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
        def __init__(self, max_size, max_volume, max_weight, spiece, info, image):
            self.items = []
            self.max_size = max_size
            self.max_volume = max_volume         #Max amount of total volume of items
            self.max_weight = max_weight
            self.current_volume = 0
            self.current_weight = 0
            self.spiece = spiece
            self.info = info
            self.image = image

        def add(item):
            left_volume = self.max_volume - self.current_volume
            left_weight = self.max_weight - self.current_weight
            item_volume_total =  item.volume * item.quantity
            item_weight_total =  item.weight * item.quantity

            if item.size > self.max_size:
                "This will not fit"
            elif item_volume_total > left_volume:
                "This is too big"
            elif item_weight_total > left_weight:
                "This is too heavy"
            else:
                self.current_volume += item_volume_total
                self.current_weight += item_weight_total
                self.items.append(item)

        
        def remove(Item):
            self.item_volume = self.volume*self.quantity
            self.current_volume = self.current_volume-self.item_volume
            self.item_weight = self.weight*self.quantity
            self.current_weight = self.current_weight-self.item_weight
            self.Inventory.pop 
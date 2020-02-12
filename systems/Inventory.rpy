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
    
    class Item(object):
        def __init__(self, name, quantity, volume, size, weight, spiece, info, price, craft, thumb, image, value):
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
            self.value = value

    class Consumable(Item):
        def __init__(self, name, quantity, image):
            super().__init__(self, name, quantity, image)
            self.thirst_loss = thirst_loss
            self.hunger_loss = hunger_loss

        def use(self, target):
            

    class Eqquipable(Item):
        def __init__(self, name, weight, image):
            super().__init__(self, name, weight, image)
            self.is_equipped = False
            self.equipped_to = None

        def equip(self, target):
            self.is_equipped = True
            self.equipped_to = target

        def unequip(self, target):
            self.is_equipped = False
            self.equipped_to = None

    class Container():
        def __init__(self, max_size, max_volume, max_weight, spiece, info, image):
            self.items = {}
            self.max_size = max_size
            self.max_volume = max_volume         #Max amount of total volume of items
            self.max_weight = max_weight
            self.current_volume = 0
            self.left_volume = self.max_volume - self.current_volume
            self.current_weight = 0
            self.left_weight = self.max_weight - self.current_weight
            self.spiece = spiece
            self.info = info
            self.image = image
            self.sizecount()
    
        def __iter__(self):
            return iter(self.items.items())
    
        def __len__(self):
            return len(self.items)
    
        def __contains__(self, item):
            return item.name in self.items
    
        def __getitem__(self, item):
            return self.items[item.name]
    
        def __setitem__(self, item, value):
            self.items[item.name] = value
            return self[item]


        def add(self, item):
            self.left_volume = self.max_volume - self.current_volume
            self.left_weight = self.max_weight - self.current_weight
            item_volume_total =  item.volume * item.quantity
            item_weight_total =  item.weight * item.quantity

            if item.size > self.max_size:
                return False, "This will not fit"
            elif item_volume_total > self.left_volume:
                return False, "This is too big"
            elif item_weight_total > self.left_weight:
                return False, "This is too heavy"
            else:
                self.current_volume += item_volume_total
                self.current_weight += item_weight_total
                if item in self:
                    self[item].quantity += 1
                else:
                    self[item] = item
                return True, "ok"

        def remove(self, item):
            item_volume_total =  item.volume # * item.quantity
            item_weight_total =  item.weight # * item.quantity
            self.left_volume += self.current_volume
            self.left_weight += self.current_weight
            self.current_volume -= item_volume_total
            self.current_weight -= item_weight_total
            if self[item].quantity > 1:
                self[item].quantity -= 1
            else:
                del self.items[item.name]

        def sizecount(self):
            return sizes[self.max_size]





        #@property
        

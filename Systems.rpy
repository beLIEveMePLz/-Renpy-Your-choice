#  _____                      _                   
# |     |                    | |                  
#   | |  _ ____   _____ _ __ | |_ ___  _ __ _   _ 
#   | | | '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
#  _| |_| | | \ V /  __/ | | | || (_) | |  | |_| |
# |_____|_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
#                                            __/ |
#                                           |___/ 
######################################################################


                                                                       
                  
python :
    class Item(object):
        def __init__(self, name, quantity, volume, size, weight, spiece, info, price, craft, thumb, image):
            self.name = name            #1 Nazwa        
            self.quantity = quantity    #2 Ilość
            self.volume = volume        #3 Objetosc
            self.size = size            #4 Rozmiar    
            self.weight = weight        #5 Ciężar
            self.spiece = spiece        #6 Rodzaj   
            self.info = info            #7 Informacje   
            self.price = price          #8 Cena
            self.craft = craft          #9 Tworzenie
            self.thumb = thumb          #10 Miniaturka
            self.image = image          #11 Obrazek         
            
            # 1 Name
            # Name of item for identification purpose

            # 2 Quantity
            # Amount of items we have
            # Ex. 15xbatteries

            # 3 Volume
            # Amount of volume taken from Container
            # all items(volume)<=max_volume

            # 4 Size
            # Size type for logical fit it to container
            # (huge, big, medium, small, tiny) 
            # big items can not fit to small container
            # small can fit to big, medium and small container size
            # 1 huge = 2 big = 4 medium = 6 small = 10 tiny
            # huge>big>medium>small>tiny
            
            # 5 Weight
            # Weight of 1 Item 
            # containers have capability of max weight of themself
            # Player must have enough sterngh to pic up enough
            # Strengh(actual_max_weight)=>weight<max weight container

            # 6 Spiece
            # Type of item
            # Static, useful, eatable 

            # 7 Info
            # Simple info about Item
            # Hover window best scenario

            # 8 Price
            # The price of Item

            # 9 Craft
            # For crafting purpose

            # 10 Thumb
            # Placeholder for thumbinal wiev of item

            # 11 Image
            # Full wiev of item



    class Container():
        def __init__(self, max_size, max_volume, max_weight, spiece, info, image, ):
            self.inventory = []             # List for items
            self.max_size = max_size 
            self.max_volume = max_volume        # Max amount of total volume of items
            self.max_weight = max_weight    
            self.spiece = spiece
            self.image = image



        def add_item(self, item):
            self.inventory.append(item)




















                                                                                                                                                                     

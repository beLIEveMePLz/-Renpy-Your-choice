init python:
    
    directions= []

    class Location(object):
        """docstring for Location"""
        def __init__(self, name, actual, links ):
            self.name = name
            self.direction = 0
            self.directions = []    

    class Movement(object):
        """docstring for Movement"""
        def __init__(self, left, foward, right, target, direction):
            super(Movement, self).__init__()
            self.left = left
            self.foward = foward
            self.right = right
            self.target = target
            self.direction = direction

        def fwd(self):
            target = directions[1]

        def left(self):
            deleted_dir = directions[:-1]
            directions.pop()
            directions.append[0:] = deleted_dir

        def right(self):
            deleted_dir = directions[0:]
            directions.pop(0:)
            directions.append[:-1] =deleted_dir
            
           

class Entity(object):
    def __init__(self, draw_id, position):
        self._pos = position
        self._draw_id = draw_id
        self._is_alive = True

    def get_position(self):
        """
        _pos is a tuple. Tuples cannot be changed or assigned to, 
        so the returned value cannot be accidentally changed.
        If we were returning something like a list here then a copy
        would need to be made before returning it.
        """
        return self._pos
    def is_alive(self):
        return self._is_alive
    def collide(self, other_entity):
        pass
    def get_id(self):
        return self._draw_id
    def update(self):
        pass

class Pac_Person(Entity):
    pass

class Ghost(Entity):
    pass

class Game_Board(object):
    def __init__(self):
        start_position = (13.0, 23.0)
        self._entities = []
        self._player = Pac_Person("Pac_Person", start_position)
    def add_entity(self, position, draw_id):
         

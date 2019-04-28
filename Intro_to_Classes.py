import math

class Point:
    'Represents a point in 2-dim space'

    def __init__(self, x=0, y=0):
        'initialize the position of a new point (default 0,0)'
        self.move(x,y)

    def reset(self):
        'reset point back to 0,0'
        self.x = 0
        self.y = 0

    def move(self,x,y):
        'move a point to a new loc'
        self.x = x
        self.y = y


    def calc_dist(self,other_point):
        'calc eucl_dist between 2 points, returns float'
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

p1 = Point()
p2 = Point()

p1.x = 2
p1.y = 2

p2.x = 3
p2.y = 2

print(p1.calc_dist(p2))

p4 = Point()
p1.calc_dist(p4)


from package_mgmt.package_tutorial.db_conn.database import Database
db1 = Database(name = 'nowa')
db1.__str__()
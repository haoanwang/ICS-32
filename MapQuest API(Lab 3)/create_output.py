#Kevin Luu 48783106 Lab Section #

import apimapquest

class direction_display:
    def __init__(self, jsons_stuff):
        self.jsons_stuff = jsons_stuff
        
    def step_direction(self:'json') ->list:
        """takes json code and returns step by step direction"""
        final = []
        print ("DIRECTIONS")
        for elements in self.jsons_stuff['route']['legs']:
            for items in elements['maneuvers']:
                final.append(items['narrative'])
        for item in final:
            print (item)

class distance_display:
    def __init__(self,jsons_stuff):
        self.jsons_stuff = jsons_stuff
        
    def total_distance(self:'json') ->str:
        """takes json code and returns total distance"""
        total = (self.jsons_stuff['route']['distance'])
        print ("Total Distance: {0:0.0f} miles".format(round(total, -1 )))

class time_display:
    def __init__(self, jsons_stuff):
        self.jsons_stuff = jsons_stuff
        
    def total_time(self:'json') ->str:
        """takes json code and returns total time of trip"""
        time = (self.jsons_stuff['route']['time'])
        print ("Total Time: {0:0.0f} minutes".format(round(time / 60, -1)))

class lat_long_display:
    def __init__(self,jsons_stuff):
        self.jsons_stuff = jsons_stuff
        
    def lat_long(self:'json') ->list:
        """takes json code and returns latitude and longitude of each location"""
        for obj in self.jsons_stuff['route']['locations']:
            alpha = None
            beta = None
            if obj['latLng']['lat'] <= 0:
                alpha = (str(obj['latLng']['lat'] * -1) + "S")
            elif obj['latLng']['lat'] >= 0:
                alpha = (str(obj['latLng']['lat']) + "N")
            if obj['latLng']['lng'] <= 0:
                beta = (str(obj['latLng']['lng'] * -1) + "W")
            elif obj['latLng']['lng'] >= 0:
                beta = (str(obj['latLng']['lng']) + "E")
            print (alpha + " " + beta)

             
            
            

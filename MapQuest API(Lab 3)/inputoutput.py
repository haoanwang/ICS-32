#Kevin Luu 48783106 Lab Section #

import apimapquest
import create_output

def map_input()-> None:
    """basic input"""
    while True:
        num_destinations = int(input())
        if num_destinations >= 2:
            destinations = []
            for trips in range(num_destinations):
                destinations.append(str(input()))
            url = apimapquest.build_destinations(destinations)
            results = apimapquest.result_destinations(url)
            map_outputs(results)
        else:
            print ("Error")
def map_outputs(results:'jsons')-> None:
    """displays outputs on user based inputs"""
    num_outputs = int(input())
    if num_outputs  > 0:
        things_print = []
        for outputs in range(num_outputs):
            things_print.append(str(input()))
            
        for i in range(len(things_print)):
            if things_print[i] == ("STEPS"):
                steps = create_output.direction_display(results)
                (steps.step_direction())
                print ('')
                
            elif things_print[i] == ("TOTALDISTANCE"):
                distance = create_output.distance_display(results)
                distance.total_distance()
                print ('')
                    
            elif things_print[i] == ("TOTALTIME"):
                time = create_output.time_display(results)
                time.total_time()
                print ('')
                    
            elif things_print[i] == ("LATLONG"):
                geo = create_output.lat_long_display(results)
                geo.lat_long()
                print ('')
            else:
                print ("Error")
            
        print ("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")
                
    
    
if __name__ == '__main__':
    map_input()


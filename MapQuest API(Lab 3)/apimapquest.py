#Kevin Luu 48783106 Lab Section #

import json
import urllib.parse
import urllib.request



def build_destinations(place_url:list) ->str:
     """takes locations and retruns encoded url"""
     api_key = "Fmjtd%7Cluu821682u%2Crw%3Do5-942n0r"
     mapquest = "http://open.mapquestapi.com"
     built_locations = []
     for i in range(0,len(place_url)):
          if i == 0:
               built_locations.append(('from', place_url[i]))
          else:
               built_locations.append(('to',place_url[i]))
     return str((mapquest + '/directions/v2/route?key=' + api_key + '&' +urllib.parse.urlencode(built_locations)))

       
def result_destinations(built_url)-> 'json':
     """takes eoncoded urls and returns json code"""
     data = None
     try:
          data = urllib.request.urlopen(built_url)
          json_text = data.read().decode(encoding = 'utf-8')
          return json.loads(json_text)
    
     finally:
          if data != None:
               data.close()
               





    
    

import requests
from urllib.parse import urlencode
from typing import List

"""Google Maps Geocode API script for geocoding addresses as a list of one or n addresses"""

API_KEY = "" #user specific api key
data_type = "json" #data type to be returned from google, can also be xml


def geocode(addresses: List[str], data_type: str = "json"):  
    base = f"https://maps.googleapis.com/maps/api/geocode/{data_type}" #base url structure for request
    
    
    if len(addresses) == 1:
        params = {"address": addresses[0], #first url parameter for request
                  "key" : API_KEY}    #second url parameter for request

        url_params = urlencode(params) #url formatted parameters

        url = f"{base}?{url_params}"
    
        """request and return of valid lat lng locations"""
        r = requests.get(url)
        if r.status_code not in range(200, 299):
            return {}
        latlng = {}
        try: 
            latlng = r.json()['results'][0]['geometry']['location']
        except:
            pass
        return latlng
        
    locations = []
    for i in range(len(addresses)):
        params = {"address": addresses[i], #first url parameter for request
                  "key" : API_KEY}    #second url parameter for request

        url_params = urlencode(params) #url formatted parameters

        url = f"{base}?{url_params}"
    
        """request and return a list of valid lat lng locations"""
        r = requests.get(url)
        if r.status_code not in range(200, 299):
            return {}
        latlng = {}
        try: 
            latlng = r.json()['results'][0]['geometry']['location']
        except:
            pass
        locations.append(latlng)
        
    try:     
        return locations
    except:
        return latlng
 
 


def main():
    multi_address = ["1600 Amphitheatre Pkwy, Mountain View, CA 94043", 
                     "1 Hacker Way, Menlo Park, CA 94025", 
                     "1 Apple Park Way Cupertino, California, 95014"]
        
    ma = geocode(multi_address)
    print("multiple addresses:")
    print(ma)
    print(" ")
    
   
    sa = geocode(["1600 Amphitheatre Pkwy, Mountain View, CA 94043"])
    print("single address:")
    print(sa)

if __name__=="__main__":
    main()

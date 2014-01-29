# -*- coding: utf-8 -*-
#########################
#     Geo Utils
#########################

from math import radians, cos, sin, asin, sqrt, atan2
from geopy.distance import vincenty

paris = (48.856578, 2.351828)

def haversine(lon1, lat1, lon2, lat2):
    """
    Compute distance between two points using the Haversine formula. 
    Coordinates must be specified in decimal degrees.
    """
    # Convert decimal degrees to radians using builtin math library
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    
    # Haversine formula (http://en.wikipedia.org/wiki/Haversine_formula)
    # dist = 2*radius*arcsin(sqrt(sin((lat2-lat1)/2)+cos(lat1)*cos(lat2)*sin((lon2-lon1)/2)**2))
    longitudinal_distance = lon2 - lon1
    latitudinal_distance = lat2 - lat1
    a = sin(latitudinal_distance/2)**2 + cos(lat1) * cos(lat2) * sin(longitudinal_distance/2)**2
    b = 2*asin(sqrt(a))
    km = 6367 * b
    return km

def distance_from_paris_h(longitude, latitude):
    """
    Compute distance from Paris given arbitrary coordinates using Haversine formula
    """
    distance = haversine(paris[0], paris[1], longitude, latitude)
    return distance

def distance_from_paris_geopy(coordinates):
    """
    Compute distance from Paris given arbitrary coordinates using geopy package
    """
    point = (coordinates[1],coordinates[0])
    distance = vincenty(paris, point).km
    return distance 
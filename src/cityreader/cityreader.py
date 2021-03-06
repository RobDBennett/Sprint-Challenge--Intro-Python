# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
import csv


class City:
  """
  Class that accepts a city name, the latitude, and the longitude of the city.
  Other methods or demographics could be added for more functionality.
  """
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __str__(self):
    """Method that give the string details."""
    return f'{self.name}, {self.lat}, {self.lon}'


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities=[]):
  """Function that should pull from a csv file, find the proper columns to add to the Class,
  and then iterate over by rows, adding to the list 'cities'"""
  with open('cities.csv', mode='r', newline='') as csvfile:
    city_reader = csv.reader(csvfile, delimiter=',')
    next(city_reader)
    for row in city_reader:
      cities.append(City(row[0], float(row[3]), float(row[4])))

    return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
start = tuple(input("Please put in starting lat, lon:").split(','))
end = tuple(input("Please put in ending lat, lon:").split(','))


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  """Function that accepts inputs, sets them to a range and then creates a list comprehension from the cities list."""
  lat_range = [float(lat1), float(lat2)]
  lon_range = [float(lon1), float(lon2)]
  within = [city for city in cities if ((min(lat_range) <= city.lat <= max(lat_range)) and (min(lon_range) <= city.lon <= max(lon_range)))]

  # Go through each city and check to see if it falls within
  # the specified coordinates.

  return within

#x = cityreader_stretch(*start, *end, cities)
#print(x)
#for i in x:
#  print(x[i])
"""
The above doesn't seem strictly necessary to pass the test_stretch.py. This was more or less to ensure that the function operated correctly.
While I can't seem to parse out the list by an index, I'm running low on time and will start pushing things to git. If I can successfully do a 
pull request, I'll go back and see about this personal testing.
"""
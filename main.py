import json
import turtle
import requests
import time

# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# Load the world map image
screen.bgpic("map.gif")
screen.register_shape("iss.gif")

iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
    # Load the current status of the ISS in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    result = response.json()

    # Extract the ISS location
    location = result["iss_position"]
    lat = float(location['latitude'])
    lon = float(location['longitude'])

    # Update the ISS location on the map
    iss.goto(lon, lat)

    # Refresh every 3 seconds
    time.sleep(3)

# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)


# establish distance in km
distance_km = 1.6 * 10

#convert time to hrs
time_hr = (30/60) + ( 30 /3600)

#calculate speed
speed = distance_km/time_hr
print(f"{speed} km/hr" )
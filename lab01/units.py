num_m = 800.
print num_m
num_miles = 1.61 * (num_m/1000)
print num_miles

num_sec = 130.
num_min = num_sec / 60
print num_min

num_min_per_mile = num_min / num_miles
print num_min_per_mile

minutes = int(num_min_per_mile)
seconds = (num_min_per_mile*60) % 60
miliseconds = (num_min_per_mile*3600) % 60

print("%d:%02d:%02d" % (minutes, seconds, miliseconds))



#Note that this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal 
# to 444500000.0.

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
reservoir_volume = 4.445 * 10 **8
print(reservoir_volume)

# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
rainfall = 5 * 10 ** 6
print(rainfall)

# decrease the rainfall variable by 10% to account for runoff
runoff = (10/100) * rainfall

rainfall -=runoff
print(rainfall)


# add the rainfall variable to the reservoir_volume variable
sumof_rainfall_reservoir_volume = rainfall + reservoir_volume



# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm
overflow_5percent = (5/100) * reservoir_volume
print(overflow_5percent)

reservoir_volume_increase = reservoir_volume + overflow_5percent
print(reservoir_volume_increase)


# decrease reservoir_volume by 5% to account for evaporation
evaporation_5percent = overflow_5percent
reservoir_volume_descrease = reservoir_volume_increase - evaporation_5percent
print(reservoir_volume_descrease)

# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.
water_piped_to_AR = 2.5 * 10 **5
print(water_piped_to_AR)

reservoir_volume = reservoir_volume_descrease - water_piped_to_AR


# print the new value of the reservoir_volume variable
print(reservoir_volume)
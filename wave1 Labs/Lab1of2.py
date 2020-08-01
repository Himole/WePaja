#Quiz: Calculate
#In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long,
#the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

#total tiles for partA
length = 7
width = 9
partA = length * width
print(partA)

#total tiles for partB
length = 7
width = 5
partB = length * width
print(partB)

#1. How many tiles are needed?
tt_needed = partA + partB

#2. You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?
pack_purchased = 17
tile_per_pack = 6
tt_available = pack_purchased * tile_per_pack
tiles_leftover = tt_available - tt_needed





# Fill this in with an expression that calculates how many tiles are needed.
print(tt_needed)

print (tt_available)

# Fill this in with an expression that calculates how many tiles will be left over.
print(tiles_leftover)
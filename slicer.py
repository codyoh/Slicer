

# slicer software by codyoh
# input: STL file
# output: gcode file

#create list of all triangles
# [p1, p2, p3] ->
# [(x1, y1, z1), (x2, y2, z2), (x3, y3, z3)]

#translate all stl coordinates to be centered on bed


#create array of slicing plane z-heights based on layer height


### CREATING BOUNDARY LINE OF LAYER
#find equations for edges based on vertices of triangles

#find intersection of edge and slice plane

#check if intersection is w/in z-bounds of the edge
#if so, add it as a point in what will be the line that is intersection of slice plane and triangle
#find and add other point


#arrange all lines in the layer such that they form a closed loop
#find top leftmost point in the layer
#use other point in that line
#search over all points in layer to find the matching point that is next in line
#repeat until ending up at first point


### CHECKING FOR SURFACES WITHIN LAYER
#check if any triangles are completely within bounds of current layer height and the next
#if so, draw a bounding triangle from its projection onto this plane
#completely fill in that triangle


### CREATE INFILL



#repeat all above for every layer height




#prepend heating, fan

#append turning off heating, fan
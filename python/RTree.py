from rtree import index


# mystreet = {
#     "type": "Feature",
#     "geometry": {
#         "type":"MultiLineString",
#         "coordinates":[[
#             [1402528.63585071451962,7491973.552016104571521],
#             [1402597.665066956076771,7491840.036925406195223]
#         ]]
#     },
#     "properties": {
#         "name": "Anders Henriksens Gade",
#         "oneway": "yes"
#     },
#     "crs": {
#         "type":"link",
#         "properties": {
#             "http://spatialreference.org/ref/sr-org/6864/proj4/",
#             "proj4"
#         }
#     }
# }
 
idx = index.Index()
# minimum bounding rectangle for feature
left, bottom, right, top = (
    0.0, 0.0, 1.0, 1.0)

# create an in-memory R-tree index
#idx.insert(0, (left, bottom, right, top))
# disk-based R-tree: 
# idx = index.Index('spatial.db')
 
# Store the geojson object in the (now clustered) index
# In tutorial: idx.insert(id=0, bounds=(left, bottom, right, top), obj=mystreet)
# What actually worked... no keywords args for id and bounds:
#idx.insert(0, (left, bottom, right, top), obj=mystreet)

geometry = {"coordinates":["54.5816470,-5.9991820"]}

idx.insert(0, (left, bottom, right, top), obj=geometry)

feature1 = [n.object for n in idx.intersection((left, bottom, right, top), objects=True)]

# feature1 = list(idx.intersection((left, bottom, right, top), objects=True))[0].object
# feature2 = list(idx.nearest((left, bottom, right, top), objects=True))[0].object



print feature1
#print feature2
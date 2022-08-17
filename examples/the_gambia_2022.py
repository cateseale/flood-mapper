import ee
from flood_mapper import derive_flood_extents

ee.Initialize()
ee.Authenticate()

# Define a start and end date between to select imagery before the flooding event
before_start = '2022-07-01'
before_end = '2022-07-29'

# Define a start and end date between to select imagery after the flooding event
after_start = '2022-07-29'
after_end = '2022-08-17'

# Define a geographic region where the flooding occurred.
region = ee.Geometry.Polygon([[[-16.853846990569835,13.035840740140829],
                               [-15.977687322601085,13.035840740140829],
                               [-15.977687322601085,13.631814638022147],
                               [-16.853846990569835,13.631814638022147]]])

# Change the export flag to 'False' if you do not wish to export the results to Google Drive
detected_flood_vector, detected_flood_raster, before_imagery, after_imagery = derive_flood_extents(region,
                                                                                                   before_start,
                                                                                                   before_end,
                                                                                                   after_start,
                                                                                                   after_end,
                                                                                                   export=True,
                                                                                                   export_filename='the_gambia')


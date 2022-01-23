import gtfs
import gtfs_kit
import create_shapes

def main():
    # Parameters
    dataPath = r"C:\Users\tobia\Documents\Python Stuff\public_transit_visualisation\data\gtfs_train.zip"
    dataPathLines = r"C:\Users\tobia\Documents\Python Stuff\public_transit_visualisation\data\linie-mit-polygon.json"

    create_shapes.create_shapes_file(dataPathLines)

    feed = gtfs.load_data(dataPath)
    geometrized_routes = gtfs_kit.geometrize_routes(feed)


#### start programm

main()
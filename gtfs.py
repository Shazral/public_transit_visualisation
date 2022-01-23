import json
import gtfs_kit




def load_data(path):
   print("Datapath: " + path)
   feed = (gtfs_kit.read_feed(path, dist_units="km"))
   print("read feed")
   feed.validate()
   print("validated feed")
   return feed
import json

class TrackPart:
    def __init__(self, start_name, end_name, line_number, line_name, km_start, km_end, coordinates):
        self.start_name = start_name
        self.end_name = end_name
        self.line_number = line_number
        self.line_name = line_name
        self.km_start = km_start
        self.km_end = km_end
        self.coordinates = coordinates

def create_shapes_file(path):
    f = open(path)
    data = json.load(f)
    track_parts = []
    for entry in data:
        entry = entry["fields"]
        track_parts.append(TrackPart(start_name=entry["bp_anf_bez"], end_name=entry["bp_end_bez"], line_number=entry["linienr"], line_name=entry["liniename"], km_start=entry["km_agm_von"], km_end=entry["km_agm_bis"], coordinates=entry["geo_shape"]["coordinates"]))
        
    print(len(track_parts))
    lines = []
    for e in track_parts:
        lines.append(e.line_number)
    lines = list(dict.fromkeys(lines))

    for line in lines:
        relevant_track_parts = [x for x in track_parts if x.line_number == line]
        for y in relevant_track_parts:
             print(y.start_name + ", ")
        print("\n\n")



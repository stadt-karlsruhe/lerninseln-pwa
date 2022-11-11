import pandas as pd
import numpy as np
import findMeta as fm
from geopy.geocoders import Nominatim

df = pd.read_json("lerninsel-anbieter.json")

geolocator = Nominatim(user_agent="digital-codes")

meta = pd.DataFrame(columns=["Icon","Preview","Lat","Lon"])

for i in df.itertuples():
    print("URL:",i.Index,i.URL)
    m = fm.findMeta(i.URL)
    print(m)
    
    if "image" in m:
        icon  = m["image"]
    elif "icon" in m:
        icon = m["icon"]
    else:
        icon = ""


    if "description" in m:
        preview = m["description"]
    elif "title" in m:
        preview = m["title"]
    else:
        preview = i.Titel

    try:
        loc = geolocator.geocode({"street":f"{i.Straße} {i.Hausnummer}",
                                  "city":i.Ort,
                                  "postcode":i.PLZ,
                                  "country":"Germany"})
    except:
        print("Geo error on ",i.URL)
        meta = meta.append({"Icon":icon,
                            "Preview":preview,
                            "Lat":np.nan,
                            "Lon":np.nan
                            },ignore_index=True)
        continue

    if loc == None:
        print("Geo failed on ",i.URL)
        meta = meta.append({"Icon":icon,
                            "Preview":preview,
                            "Lat":np.nan,
                            "Lon":np.nan
                            },ignore_index=True)
        continue

    meta = meta.append({"Icon":icon,
                        "Preview":preview,
                        "Lat":loc.latitude,
                        "Lon":loc.longitude
                        },ignore_index=True)

print (meta)

df.Icon = meta.Icon
df.Preview = meta.Preview
df.Lat = meta.Lat
df.Lon = meta.Lon


df.to_json("anbieter.json",orient="records")


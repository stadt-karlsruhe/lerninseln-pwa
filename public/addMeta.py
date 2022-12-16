import pandas as pd
import numpy as np
import findMeta as fm
from geopy.geocoders import Nominatim
import markdown as md
import math
import datetime as dt


#df = pd.read_json("lerninsel-anbieter.json")
df = pd.read_json("interim/li.json")

geolocator = Nominatim(user_agent="digital-codes")

meta = pd.DataFrame(columns=["Icon","Preview","Marker","Lat","Lon"])

for i in df.itertuples():
    print("URL:",i.Index,i.URL)
    m = fm.findMeta(i.URL)
    print(m)

    if (not isinstance(i.Icon,str)) and ((i.Icon == None) or math.isnan(i.Icon)):
        if "image" in m:
            icon  = m["image"]
        elif "icon" in m:
            icon = m["icon"]
        else:
            icon = "/assets/icon/icon.png" # local default
    else:
        icon = i.Icon

    # bv icon is wrong. overwrite
    if "bw-waldstadt" in icon.lower():
        icon = "https://www.bv-waldstadt.de/assets/img/kauz.png"

    # kairos is wrong. overwrite
    if "kairos13" in i.URL.lower():
        icon = "/assets/img/provider/kairos13.jpg"


    if (i.Preview == None) or math.isnan(i.Preview):
        if "description" in m:
            preview = m["description"]
        elif "title" in m:
            preview = m["title"]
        else:
            preview = i.Titel
    else:
        preview = i.Preview

    # set popup marker html
    marker = md.markdown(f"{i.Titel}\n\n{i.Strasse} {i.Hausnummer}\n\n{i.PLZ} {i.Ort}\n\n[Zum Angebot]({i.URL})\n\n")
    marker = marker.replace("<a href",'<a target="_blank" href')

    try:
        loc = geolocator.geocode({"street":f"{i.Strasse} {i.Hausnummer}",
                                  "city":i.Ort,
                                  "postcode":i.PLZ,
                                  "country":"Germany"})
    except:
        print("Geo error on ",i.URL)
        meta = meta.append({"Icon":icon,
                            "Preview":preview,
                            "Marker":marker,
                            "Lat":np.nan,
                            "Lon":np.nan
                            },ignore_index=True)
        continue

    if loc == None:
        print("Geo failed on ",i.URL)
        meta = meta.append({"Icon":icon,
                            "Preview":preview,
                            "Marker":marker,
                            "Lat":np.nan,
                            "Lon":np.nan
                            },ignore_index=True)
        continue

    meta = meta.append({"Icon":icon,
                        "Preview":preview,
                        "Marker":marker,
                        "Lat":loc.latitude,
                        "Lon":loc.longitude
                        },ignore_index=True)

print (meta)

df.Icon = meta.Icon
df.Preview = meta.Preview
df["Marker"] = meta.Marker
df.Lat = meta.Lat
df.Lon = meta.Lon
df["Kategorie"] = df["Lerninsel-Typ"]
df.Created = dt.datetime.now().strftime("%Y-%m-%d")

df.to_json("anbieter.json",orient="records")


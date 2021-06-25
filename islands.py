import pandas as pd
import requests

excel_file = "excel\\nagu_testing.xlsx"

api_key = "e99a7c7b-40c7-43e6-a062-b25cdbe7cd52"

# stop = 20
# counter = 0

try:
    df = pd.read_excel(excel_file, engine='openpyxl')
    print("Excel read.")
except Exception as e:
    print("Something went wrong. Check the error:")
    print(e)

def filter_islands(island):
    if (island["properties"]["label:placeType"] == "Saari tai luoto" or island["properties"]["label:placeType"] == "Saari- tai luotoryhmä") and island["properties"]["label:municipality"] == "Parainen":
        return True
    else:
        return False
     

for index in df.index: 

    # counter+=1
    
    # if counter == stop:
    #     break

    cur = df.loc[index, "itemLabel"]

    response = requests.get("https://avoin-paikkatieto.maanmittauslaitos.fi/geocoding/v1/pelias/search?sources=geographic-names&text=" + cur + "&api-key=" + api_key)

    if response.status_code == 200:

        islands = response.json()["features"]

        islands_parainen = list(filter(filter_islands, islands))
        length = len(islands_parainen)

        if length==0:
            print("Island not found.")
            print()
        elif length>1:
            print("More than one result.")
            print()
        else:
            prop = islands_parainen[0]["properties"]

            label = prop["label"]
            placeId = prop["placeId"]
            placeElevation = prop["placeElevation"]
            municipality = prop["label:municipality"]
            coordinates = islands_parainen[0]["geometry"]["coordinates"]

            # Printing out values in terminal
            print(label)
            print(placeId)
            print(placeElevation)
            print(municipality)
            print(coordinates)
            print()

        
            df.loc[index, "MML_label"] = label
            df.loc[index, "MML_placeId"] = placeId
            df.loc[index, "MML_coordinates"] = str(coordinates[0]) + ", " + str(coordinates[1])
            df.loc[index, "placeElevation"] = placeElevation
            df.loc[index, "MML_label:municipality"] = municipality

                
    else:
        print("Something went wrong. Status code " + response.status_code)

# Export dataframe as excel
df.to_excel("excel\\edited_nagu.xlsx", index = False)
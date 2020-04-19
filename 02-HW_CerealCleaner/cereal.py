import os
import csv

cereal_csv = os.path.join("Resources", "cereal.csv")

# Open the CSV
with open(cereal_csv) as cerealfile:
    cerealreader = csv.reader(cerealfile, delimiter=",")
    next(cerealfile)
    for row in cerealreader:
        
        name = row[0]
        fiber = row[7]
        

        if fiber >= str("5"):
         
            print(f"{name} has {fiber} grams of fiber")

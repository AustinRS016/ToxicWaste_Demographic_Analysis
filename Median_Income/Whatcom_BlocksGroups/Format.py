import csv, sys, string, os


csvi = r"H:\GIS\Data\Census_Records_2018\Median_Income\Whatcom_BlocksGroups\Whatcom_Med$_Reformatted.csv"


with open (csvi) as f:
    print("opened")
    reader = csv.reader(f)
    for x in reader:
        z = (x[0])
        WA_GEOID = (z[-12:])
        print(WA_GEOID)
        writer = csv.writer(f)
        with open (csvi) as f:
            if "US" in z:
                z = writer.writerow(WA_GEOID)
            
        
            



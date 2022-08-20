
import csv
# snippet
count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

with open("filecounts.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"], count[".md"], count[".png"]]
    countwriter.writerow(data)

#names and age of your friends
names = {"kiphcumba": 8, "sami": 2, "ralitr": 2, "famajo": 11}


#write field name
# declare field oprions
field_names = ["Name", "Age", "Favoritecolor"]
with open("names.csv","w") as csvfile:
    #create a write object
    f = csv.writer(csvfile)
    f.writerow(field_names)


# append data to the list
data = [["Sammy", 24, "pink"],["lawi", 78, "blue"],["cynthia", 34,"pink"] ]
with open("names.csv", "a") as n:
    #create writer object
    nm = csv.writer(n)
    # create data to be stored
    nm.writerows(data)




#reading the data
with open("names.csv", "r") as f:
    # reader object
    reader = csv.DictReader(f, fieldnames=["Name", "Age", "Favoritecolor"])
    print(reader)
    count = list(reader)
    print(count)

    for file in count:
        print(file["Name"])

def without_csv_module():
    #without csv module

    #names and age of your friends
    names = {"kiphcumba": 8, "sami": 2, "ralitr": 2, "famajo": 11}
    with open("friends.csv", "a") as fnd:
        # create data to be stored
        data = [names["kiphcumba"], names["sami"], names["ralitr"], names["famajo"]]
        # concateneated string
        new_data = str(names["kiphcumba"]) + "," + str(names["sami"]) + "," + str(names["ralitr"]) + "," + str(names["famajo"]) + "\n"
        fnd.write(new_data)
    
    # convert data into a string concatenated with commas in between



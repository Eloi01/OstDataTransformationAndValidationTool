import json
import pathlib

# Based on OstData-Metadatenschema V0.2.9

# List of all Filenames
input_list = ["DRK4_5", "DRK6", "DRK7", "DRK8", "DRK9", "DRK10", "DRK11", "DRK12", "DRK13", "DRK14", "DRK15", "DRK16",
              "DRK17", "DRK18", "DRK19", "DRK20", "DRK21", "DRK22", "DRK23", "DRK24", "DRK25", "DRK26", "DRK27",
              "DRK28", "DRK29", "DRK30", "DRK31", "DRK32", "DRK33", "DRK34", "DRK35", "DRK36",
              "DRK37", "ERK1", "ERK2", "ERK3"]

suffix = "_jpg.json"

input_path = pathlib.Path(r"C:\Users\alexk\Documents\GWZO\Metadaten\Metadaten_Files")
output_path = pathlib.Path(r'C:\Users\alexk\Documents\GWZO\Metadaten\Metadaten_Files\Output_Hermann_Preprocessing-Test.json')

with open(output_path, "w", encoding="utf-8") as output:
    output.write("[")
    for dictionary in input_list:
        dictionary = dictionary + suffix
        file_to_open = input_path / dictionary
        with open(file_to_open, "r", encoding="utf-8") as input_file:
            json_input_list = json.load(input_file)
            for dict in json_input_list:

                # checks if dict is empty
                key_list = dict.keys()
                if len(key_list) == 0:
                    continue

                # ID 3.a
                dict["ContributorType"] = "DataCurator"
                # ID 5
                dict["ProjectName"] = "Sachsen und das östliche Europa - Erschließung arkaner Quellen für die Osteuropaforschung"
                # ID 9
                dict["Language"] = ""
                # ID 20
                dict["Discipline"] = "05012"
                # ID 30
                """
                For Testing purposes rearranged
                if "SpecialInstructions" in key_list:
                    dict["PlaceOfCollection"] = dict["SpecialInstructions"]
                # ID 30.3
                if "Country-PrimaryLocationName" in key_list:
                    place_description = dict["Country-PrimaryLocationName"]
                if "Province-State" in key_list:
                    place_description = place_description + " / " + dict["Province-State"]
                if "City" in key_list:
                    place_description = place_description + " / " + dict["City"]
                if "Sub-Location" in key_list:
                    place_description = place_description + " / " + dict["Sub-Location"]
                if len(place_description) != 0:
                    dict["PlaceDescription"] = place_description
                """
                dict["PlaceDescription"] = "Test"
                dict["GeoLocation"] = "http://d-nb.info/gnd/4044429-6"
                dict["PlaceOfCollection"] = "http://d-nb.info/gnd/4044429-6"
                """ End-Test"""
                # ID 37
                dict["ResourceType"] = "Nachlass"
                # ID 37.a
                dict["resourceTypeGeneral"] = "Image"
                # writes dict into file
                json.dump(dict, output, ensure_ascii=False, indent=4)
                output.write(",")
                output.write("\n")
    output.write("]")

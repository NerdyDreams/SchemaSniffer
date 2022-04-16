import json

dataFile = input("Please enter correct directory and/or name of data file\n")


messageItems = []
dictOutput = {}

def SchemaSniffer(dataFile):

    # Opening JSON file
    f = open(dataFile)
        # returns JSON object as a dictionary
    data = json.load(f)

    # list for attributes within the 'message' key



    # Iterating through the json data list and appending "message" attribute
    for i in data['message']:
        messageItems.append(i)


    # dictionary of output json schema file



    y = 0

    # looping through the output json schema file json dictionary
    for i in messageItems:
        dictOutput["key_" + str(y)] = {}
        if type(messageItems[y]) == str:
            dictOutput["key_" + str(y)]['type'] = "String"
            dictOutput["key_" + str(y)]['tag'] = ""
            dictOutput["key_" + str(y)]['Description'] = ""
            dictOutput["key_" + str(y)]['Required'] = False
            y += 1
        elif type(messageItems[y]) == int:
            dictOutput["key_" + str(y)]['type'] = "Integer"
            dictOutput["key_" + str(y)]['tag'] = ""
            dictOutput["key_" + str(y)]['Description'] = ""
            dictOutput["key_" + str(y)]['Required'] = False
        elif type(messageItems[y]) == bytearray:
            dictOutput["key_" + str(y)]['type'] = "Array"
            dictOutput["key_" + str(y)]['tag'] = ""
            dictOutput["key_" + str(y)]['Description'] = ""
            dictOutput["key_" + str(y)]['Required'] = False

    return dictOutput



with open("schema_1.json", "w") as outfile:

    json.dump(SchemaSniffer(dataFile), outfile, indent=4)
print("Please check Output schema")


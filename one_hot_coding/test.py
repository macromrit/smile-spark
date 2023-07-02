# smiles are strings, to add on whene elements are read from a csv file, every row would be an array and every col would \
# be a string irrespective of its type at start.

# to get all (char's/fields) possible out of smiles generated and have them as keys of agent' smiles
# since everythings a string, join those with zero spaces and put them into a set
import csv


def generateFields(smiles_collection: list) -> list:
    """
    return Type -> set
    
    args:
        smiles_collection : list -> to obtain an iterable / list of smiles
        
    objective: 
        to take unique characters of pooling all strings/smiles together and
        retrieve a list containing unique chars used, which's sorted (based on ascii vals)
    """

    # try:
    if smiles_collection.count("(") == smiles_collection.count(")"):
        return sorted(set(''.join(smiles_collection)))
    #     else:
    #         raise ValueError("invalid parantheisis count!!!")
        
    # except:
    #     raise ValueError("invalid smiles collection!!!")
    


def generateHotCode(smiles: str, field_generated: list) -> list:
    """
    return Type -> list
    
    args:
        smiles : str -> represents the smiles fed to function call
        field_generated : list -> collection of ordered unique chars in smiles set, used for generating onehotcodes
    
    objective:
        when a string / smiles is fed to the function it contrives a new list and assign high(1) low(0) values
        to the list index corresponding to indexes of fields generated
    """
    
    # traverse through field_generated and check whether every char exists or not -> if exist 1 else 0
    try:
        return list(map(lambda x : int(x in smiles), field_generated))
    except:
        raise Exception("Bruh something happened!!!")

def readCsv(filename): # main part of processing
    # try:
    with open("media/csv_files/{}".format(filename), "r") as jammer:
        
        reader = list(csv.reader(jammer, delimiter=","))
        
        # casefolding headings in reader
        for i in range(len(reader[0])):
            reader[0][i] = reader[0][i].casefold()

        print(reader[0])
        
        # generating fields for the abv set
        fields = generateFields([i[reader[0].index("smiles")] for i in reader[1:]])

        # generating one-hot-codes for the abv date-set
        return [(val[reader[0].index("smiles")],      ''.join(map(str, generateHotCode(val[reader[0].index("smiles")],fields)))) for val in reader[1:]], fields

    # except:
    #     return "Invalid File type or no smile section",

if __name__ == '__main__':
    print(readCsv("test_dude.csv"))
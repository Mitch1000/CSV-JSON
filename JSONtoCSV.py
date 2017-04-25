from __future__ import print_function 
import os

def convertToCSV (jsonFile):

    if os.path.isfile(jsonFile + '.json'):
        
        if os.path.isfile(jsonFile +  '.csv'):
            os.remove(jsonFile + '.csv')
    
        f = open(jsonFile + '.csv', 'w')
                            
        with open(jsonFile + '.json') as json:
            data = json.readlines()
        
        data = [x.strip() for x in data] 
    
        init = False
        for obj in data:
            obj = obj.replace("\" :", "\":", 1)
            if obj.endswith(","):
                obj = "".join(obj.rsplit(",", 1)) 

            if obj.endswith("\""):
                obj = "".join(obj.rsplit("\"", 1)) 

            if obj.startswith("\""):
                obj = obj.replace("\"", "", 1) 

            obj = obj.replace("\":", ":", 1)

            obj = obj.replace(": \"", ":", 1)

            obj = obj.replace(":", ",", 1)

            if not any(c.isalpha() for c in obj) or obj.endswith("{"):
                obj = obj.replace("}", "")
                obj = obj.replace("{", "")
            print (obj, file=f)
        f.close()

convertToCSV('dictionary_FR')
convertToCSV('dictionary_EN')
print("Conversion from JSON to CSV is Complete.")

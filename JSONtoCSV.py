from __future__ import print_function 
import os

def convertToCSV (jsonFile):

    if os.path.isfile(jsonFile + '.json'):
        
        print('\n Converted ' + jsonFile + '.json from JSON to CSV \n')

        if os.path.isfile(jsonFile +  '.csv'):
            os.remove(jsonFile + '.csv')
    
        f = open(jsonFile + '.csv', 'w')
                            
        with open(jsonFile + '.json') as json:
            data = json.readlines()
        
        data = [x.strip() for x in data] 
    
        init = False
        for obj in data:
            if obj.endswith(','):
                obj = ''.join(obj.rsplit(',', 1)) 

            if obj.endswith('"') and ',' not in obj:
                obj = "".join(obj.rsplit('"', 1)) 

            if obj.startswith('"'):
                obj = obj.replace('"', '', 1) 

            obj = obj.replace('":', ':', 1)

            if ',' not in obj:
                obj = obj.replace(': "', ':', 1)

            obj = obj.replace(':', ',', 1)

            if not any(c.isalpha() for c in obj) or obj.endswith('{'):
                obj = obj.replace('}', '')
                obj = obj.replace('{', '')

            print (obj, file=f)
        f.close()
    else:
        print('\n No JSON file titled ' + jsonFile + '.json found. \n')

convertToCSV('dictionary_EN')
convertToCSV('dictionary_FR')

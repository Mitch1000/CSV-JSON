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
            if init:            
                obj = '{'
                init = True
            else:
                obj = obj.replace(":", ",")
                obj = obj.replace("\"", "")
                obj = obj.replace("},", "")
                obj = obj.replace("}", "")
                obj = obj.replace("{", "")
            print (obj)
            print (obj, file=f)
    f.close()

convertToCSV('dictionary_FR')
convertToCSV('dictionary_EN')

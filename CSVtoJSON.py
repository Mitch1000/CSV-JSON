from __future__ import print_function 
import os

def convertToJSON(csvFile):

    if os.path.isfile(csvFile + '.csv'):
        
        if os.path.isfile(csvFile + '.json'):
            os.remove(csvFile + '.json')
    
        f = open(csvFile + '.json', 'w')
                            
        with open(csvFile + '.csv') as csv:
            data = csv.readlines()
        
        data = [x.strip() for x in data] 

        init = False 
        indent = "" 
        nextindent = "" 
        for previous, current, nex in zip([None]+data[:-1], data, data[1:]+[None]):
           if init:
                currentindent = nextindent 

                if current.endswith(","):
                   current = current.replace(",", ": {")
                   nextindent = "  " + currentindent 

                current = current.replace(",", ":", 1)

                current = current.replace(":", "\":", 1)

                if current == "" and nex != "":
                    current = "},"

                if current == "":
                    current = "}"

                if nex == "":
                    nextindent = currentindent[2:]

                if "{" not in current and "}" not in current:    
                    current = current.replace(":", ": \"", 1)
                    current = current + '"'

                if "}" not in current: 
                    current = "\"" + current

                if str(nex) != "" and "{" not in str(current) and "}" not in str(current):    
                    current = current + ","

                current = currentindent + current
                print (current, file=f)
        
           else:
                current= '{'
                nextindent = "  " + indent
                print (current, file=f)
                init = True

        f.close()

convertToJSON('dictionary_FR')
convertToJSON('dictionary_EN')

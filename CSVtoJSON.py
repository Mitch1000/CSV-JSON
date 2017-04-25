from __future__ import print_function 
import os

def convertToJSON(csvFile):

    if os.path.isfile(csvFile + '.json'):
        
        if os.path.isfile('tmp' + '.json'):
            os.remove('tmp' + '.json')
    
        f = open('tmp' + '.json', 'w')
                            
        with open(csvFile + '.csv') as csv:
            data = csv.readlines()
        
        data = [x.strip() for x in data] 

        init = False 
        indent = "" 
        for previous, current, nex in zip([None]+data[:-1], data, data[1:]+[None]):
           if init:
                if current.endswith(","):
                   current = current.replace(",", ": {")
                   indent = "  "  + indent 

                current = current.replace(",", ":")

                current = current.replace(":", "\":")

                if current == "":
                    current = "},"

                if "{" not in current and "}" not in current:    
                    current = current.replace(": ", ": \"")
                    current = current + '"'

                if "}" not in current: 
                    current = "\"" + current

                if str(nex) != "" and "{" not in str(current) and "}" not in str(current):    
                    current = current + ","

                current = indent + current
                print (current, file=f)
        
           else:
                print('previous:' + str(previous) + '   ' + 'current:' + str(current) + '  ' +  'next:' + str(nex))
                current= '{'
                print (current, file=f)
                init = True

        f.close()

convertToJSON('dictionary_FR')
convertToJSON('dictionary_EN')

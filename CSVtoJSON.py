from __future__ import print_function
import os

def convertToJSON(csvFile):

    if os.path.isfile(csvFile + '.csv'):

        print("\n Converted " + csvFile + ".csv from CSV to JSON \n")

        if os.path.isfile(csvFile + '.json'):
            os.remove(csvFile + '.json')

        f = open(csvFile + '.json', 'w')

        with open(csvFile + '.csv') as csv:
            data = csv.readlines()

        data = [x.replace('\n', '') for x in data]

        nextindent = '  '
        print ('{', file=f)
        for previous, current, nex in zip([None]+data[:-1], data, data[1:]+[None]):
            currentindent = nextindent

            if current.endswith(', ') and current != '' and current != ',':
                 current = current.replace(', ', ': {')
                 nextindent = '  ' + currentindent

            if current != '' and current != ',':
                current = current.replace(',', ':', 1)

            current = current.replace(':', '":', 1)


            if current == '' or current == ',' and nex != '' and nex != ',' and nex != None:
                current = '},'

            if current == '' or current == ',':
                current = '}'

            if nex == '' or nex == ',':
                nextindent = currentindent[2:]

            if (not current.endswith('{')
            and not current.endswith('}')
            and not current.endswith('},')
            and not current.endswith('"')):
                current = current.replace(':', ': "', 1)
                current = current + '"'

            if current.endswith('}}'):
                current = current.replace(':', ': "', 1)
                current = current + '"'

            if (str(nex) != '' and str(nex) != ','
            and not current.endswith('{')
            and not current.endswith('}')
            and not current.endswith('},')):
                current = current + ','

            if (not current.endswith('}')
                and not current.endswith('},')
                ):
                current = '"' + current

            current = current.replace('\""', '\"')

            current = current.replace('":"', '": "')

            current = currentindent + current
            print (current, file=f)

        f.close()

    else:
        print('\n No CSV file titled ' + csvFile + '.csv found. \n')

convertToJSON('dictionary_EN')
convertToJSON('dictionary_FR')

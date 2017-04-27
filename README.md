# CSV-JSON Converter

## Instructions

####Install python 2.7 from <a sref="https://www.python.org/downloads/">here</a>

#### If using Windows add Python to your enviroment variables by following <a sref="http://stackoverflow.com/a/4855685">these</a> instructions.

#### Download CSV-JSON 

#### Unzip CSV-JSON 

#### Move the .json file you wish to convert (titled dictionary_EN.json or dictionary_FR.json) to the CSV-JSON folder.

#### In your Shell environment (such as Windows Power Shell on Windows) navigate to the CSV-JSON folder and type the following command to create a .csv file:  

              python JSONtoCSV.py

#### Import the csv file using excel following these instructions. 

For Excel 2013:
  Open Blank Workbook.
  Go to DATA tab.
  Click button From Text in the General External Data section.
  Select your CSV file.
  Select "delimited"
  Select "Other" under delimters
  Input <h4>~</h4> in the "Other" field.

#### Once you are done making your changes to the file Export the file using the following instructions: 

For Excel 2013:
  Click the FILE tab.
  Cick Export.
  Click Change File Type.
  Select CSV (Comma delited).
  Click Save As. 
  Save the file as dictionary_EN.csv or dictionary_FR.csv in the CSV-JSON folder.

#### In your Shell environment (such as Windows Power Shell on Windows) navigate to the CSV-JSON folder and type the following command to create a.json file:  

              python CSVtoJSON.py


## Notes: 
####Any files in the CSV-JSON folder will be replaced so it is best to make copies of your files before moving them to the CSV-JSON folder.
####Before exporting the .csv file in excel the excel file must be in the same format as the imported .csv file before any edits where made. 
####There must be no blank verbiage values.
####Before exporting the .csv file in excel only the first two columns in excel must contain content.

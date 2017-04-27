# CSV-JSON Converter

## Instructions

Install python 2.7 from [here](https://www.python.org/downloads/). 

If using Windows add Python to your enviroment variables by following [these](http://stackoverflow.com/a/4855685) instructions.

[Download](https://github.com/Mitch1000/CSV-JSON/archive/master.zip) CSV-JSON.

Unzip CSV-JSON. 

Move the .json file you wish to convert (titled dictionary_EN.json or dictionary_FR.json) to the CSV-JSON folder.

In your Shell environment (such as Windows Power Shell on Windows) navigate to the CSV-JSON folder and type the following command to create a .csv file:  

              python JSONtoCSV.py

Import the csv file using excel following these instructions. 

For Excel 2013:
  1. Open Blank Workbook.
  2. Go to DATA tab.
  3. Click button From Text in the General External Data section.
  4. Select your CSV file.
  5. Select "delimited".
  6. Select "Other" under delimters.
  7. Input ~ in the "Other" field.

Once you are done making your changes to the file Export the file using the following instructions: 

For Excel 2013:
  1. Click the FILE tab.
  2. Cick Export.
  3. Click Change File Type.
  4. Select CSV (Comma delimited).
  5. Click Save As. 
  6. Save the file as dictionary_EN.csv or dictionary_FR.csv in the CSV-JSON folder.

In your Shell environment (such as Windows Power Shell on Windows) navigate to the CSV-JSON folder and type the following command to create a.json file:  

              python CSVtoJSON.py


### Notes: 
1. Any files in the CSV-JSON folder will be replaced so it is best to make copies of your files before moving them to the CSV-JSON folder.
2. Before exporting the .csv file in excel the excel file must be in the same format as the imported .csv file before any edits were made. 
3. There must be no blank verbiage values.
4. Before exporting the .csv file in excel only the first two columns in excel must contain content.

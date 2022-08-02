import csv
import jsonlines
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonDict = {}

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.reader(csvf)
        next(csvReader)
        #row=next(csvReader)

        prevID=''      
        for row in csvReader:
            if row[6]=='S':
                label="SUPPORT"
            elif row[6]=='R':
                label="CONTRADICT"
            else:
                label="NEUTRAL"

            if prevID=='':
                jsonDict={"doc_id": int(row[0]), "title": row[4], "abstract": [row[6]]}
                prevID=row[0]
            elif row[0]==prevID:
                jsonDict["abstract"].append(row[6])
            else:
                print(jsonDict)
                #with open(jsonFilePath, 'a', encoding='utf-8') as jsonlf:
                #    jsonl_writer=jsonlines.Writer(jsonlf)
                #   jsonl_writer.write(jsonDict)
                prevID=row[0]
                jsonDict={"doc_id": int(row[0]), "title": row[4], "abstract": [row[6]]}

csvFilePath = r'CSVforCorpus.csv'
jsonFilePath = r'NewCorpus.jsonl'
csv_to_json(csvFilePath, jsonFilePath)
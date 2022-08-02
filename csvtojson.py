#THIS FILE CREATES GeneralizedData.jsonl, WHICH IS NEEDED BY MULTIVERS

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
            if row[7]=='S':
                label="SUPPORT"
            elif row[7]=='R':
                label="CONTRADICT"
            else:
                label="NEUTRAL"

            if prevID=='':
                jsonDict={"id": int(row[0]), "claim": row[1], "doc_ids": [int(row[0])], "evidence": {row[0]:[]}}
                prevID=row[0]
                if label=="SUPPORT" or label=="CONTRADICT":
                    jsonDict["evidence"][row[0]].append({"sentences": [int(row[5])], "label": label})
            elif row[0]==prevID:
                if label=="SUPPORT" or label=="CONTRADICT":
                    jsonDict["evidence"][row[0]].append({"sentences": [int(row[5])], "label": label})
            else:
                if jsonDict["evidence"][prevID]==[]:
                    jsonDict["evidence"].clear()
                print(jsonDict)
                with open(jsonFilePath, 'a', encoding='utf-8') as jsonlf:
                    # BE CAREFUL HERE!  IT IS APPENDING!  IF YOU RUN THIS FILE CHECK GENERALIZEDDATA.JSONL
                    jsonl_writer=jsonlines.Writer(jsonlf)
                    jsonl_writer.write(jsonDict)
                prevID=row[0]
                jsonDict={"id": int(row[0]), "claim": row[1], "doc_ids": [int(row[0])], "evidence": {row[0]:[]}}
                if label=="SUPPORT" or label=="CONTRADICT":
                    jsonDict["evidence"][row[0]].append({"sentences": [int(row[5])], "label": label})

  
                

csvFilePath = r'AnnotationsWithLabelsEthanLanders.csv'
jsonFilePath = r'GeneralizedData.jsonl'
csv_to_json(csvFilePath, jsonFilePath)

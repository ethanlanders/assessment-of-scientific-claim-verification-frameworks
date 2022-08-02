import csv
import nltk
import jsonlines

#  Whatever is outputted to Corpus.jsonl, append onto NewCorpus.jsonl

csvfile=open('CSVforCorpus.csv', 'w', encoding='utf8')
abstractwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

def csv_to_json(csvFilePath, jsonFilePath):
    claimidDict={}
    with open("AbstractsWithStructLabels.csv", encoding='utf-8') as csvf:
        csvReader = csv.reader(csvf)

        prevID=''      
        for row in csvReader:
            if prevID=='':
                claimidDict[int(row[0])]={"title": row[3], "abstract": [], "structured": bool(row[5])}
                prevID=row[0]
            else:
                prevID=row[0]
                claimidDict[int(row[0])]={"title": row[3], "abstract": [], "structured": bool(row[5])}

    with open("CorrectAnnotations.csv", encoding='utf-8') as csvf:
        csvReader = csv.reader(csvf)
        next(csvReader)   
        for row in csvReader:
            claimidDict[int(row[0])]["abstract"].append(row[5])
    print(claimidDict)                

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonlf:
        jsonl_writer=jsonlines.Writer(jsonlf)
        for key in claimidDict:
            line_dict = {}
            line_dict["doc_id"] = key
            line_dict.update(claimidDict[key])
            jsonl_writer.write(line_dict)

csvFilePath = r'AbstractsWithStructLabels.csv'
jsonFilePath = r'Corpus.jsonl'
csv_to_json(csvFilePath, jsonFilePath)
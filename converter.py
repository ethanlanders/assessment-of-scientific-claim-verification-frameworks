# This file goes from takes the abstract and tokenizes the sentences
import csv
import nltk

csvfile=open('AnnotationsNoLabels.csv', 'w', encoding='utf8')
abstractwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

claims=[]
with open("dataset.txt") as f:
    lines = f.readlines()
    for line in lines:
        if "Claim:  " in line: 
            claim=line[8:]
            claims.append(claim.rstrip())
  
with open('Abstracts.csv', newline='', encoding='utf8') as csvfile:
     abstractreader = csv.reader(csvfile)
     counter=0
     abstractwriter.writerow(['claimid', 'claim', 'doi', 'link', 'abstitle', 'abssentid', 'abssent', 'labels'])
     for row in abstractreader:
         claimid = int(row[0])
         DOI = row[1]
         link = row[2]
         title = row[3]
         abstract = row[4]
         sent_abstract = nltk.sent_tokenize(abstract)
         count=1
         for sentence in sent_abstract:
            abstractwriter.writerow([claimid, claims[counter], DOI, link, title, count, sentence, ' '])
            count=count+1  
         counter=counter+1
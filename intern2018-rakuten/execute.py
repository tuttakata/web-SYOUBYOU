import pymysql
import csv

connection = pymysql.connect(host = 'localhost',
                             db = 'sa',
                             user = 'root',
                             passwd = 'XpXSog7e',
                             charset = 'utf8',
                             cursorclass = pymysql.cursors.DictCursor)
cursor = connection.cursor()
f = open("test.csv", "r")
reader = csv.reader(f)
for row in reader:
	sql = "INSERT INTO SYOUBYOU (SYOUBYOU_NM,SYOUBYOU_KANA_NM,ICD10_1_NO,ICD10_2_NO) VALUES (%s,%s,%s,%s)"
	cursor.execute(sql,(row[0],row[1],row[2],row[3]))
f.close()
connection.commit()
cursor.close()
connection.close()

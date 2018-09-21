from flask import Flask,render_template, request
import pymysql

app = Flask(__name__)

#初期画面
@app.route('/')
def index():
	result_2=-1
	return render_template('index.html',result_2=result_2)

#検索結果表示画面
@app.route('/post', methods = ['POST'])
def send():

	if request.form['text']:
		title=request.form['text']#入力された文字
		result=db(title)
		result_1=result[0]#レコード
		result_2=result[1]#行数
		return render_template("index.html",title=title,result_1=result_1,result_2=result_2)
	#未入力時
	else :
		return render_template("index.html",result_2=-2)




#DB操作
def db(title):
	connection = pymysql.connect(host = 'localhost',
    	                         db = 'sa',
        	                     user = 'root',
            	                 passwd = 'XpXSog7e',
                	             charset = 'utf8')
	#命令文実行処理
	cursor = connection.cursor()
	sql = 'SELECT * FROM SYOUBYOU WHERE SYOUBYOU_NM LIKE "%{0}%" OR SYOUBYOU_KANA_NM LIKE "%{0}%" ORDER BY length(SYOUBYOU_NM),SYOUBYOU_KANA_NM;'.format(title)
	cursor.execute(sql)
	rows=cursor.fetchall()

	#行の数え上げ
	l=0
	for i in rows:
		l=l+1

	cursor.close()
	connection.close()

	#rows=取り出したレコード,l=レコードの行数
	return rows,l


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=7788)


from flask import Flask
from flask import render_template
from Search import Search

app = Flask(__name__,template_folder='../output')

@app.route('/')
def showResult():
    data = Search().getRankedResult()

    return render_template('search.html', data = Search().getRankedResult())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5102)
    #print('The result is',Search().getRankedResult())
    #print(Search().getRankedResult())
	#main()
	#print(type(main()))
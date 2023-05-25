from textblob import TextBlob 
from flask import Flask, render_template , request

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
  return render_template("index.html")


@app.route("/predict1", methods=['POST','GET'])
def pred1():
	if request.method=='POST':
            text = request.form['txt']
            blob = TextBlob(text)
            if blob.sentiment.polarity > 0:
                text_sentiment = "positive"
                tcolor = '#00ff00'
            elif blob.sentiment.polarity == 0:
                text_sentiment = "neutral"
                tcolor = 'white'
            else:
                text_sentiment = "negative"
                tcolor = 'red'
            return render_template('result1.html',msg=text, result=text_sentiment, rtext=tcolor)


if __name__ == '__main__':

    app.debug=True
    app.run(host='localhost', port='8080')


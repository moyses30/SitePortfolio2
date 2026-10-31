from flask import Flask , render_template ,url_for ,request ,flash ,redirect
from forms import EnviarEmail



app = Flask(__name__)
app.config['SECRET_KEY']= '6311cd5b4099931e9dc7624bc309610e'
@app.route('/')
def home():
    enviaremail = EnviarEmail()
    return render_template('home.html', enviaremail = enviaremail)



@app.route ('/sucesso')
def sucesso():

    return render_template('sucesso.html')

if __name__ == '__main__' :
    app.run(debug=True)

from flask import render_template , redirect , url_for ,request,flash
from siteportfoliotres import app, database
from siteportfoliotres.forms import EnviarEmail
from siteportfoliotres.models import EmailBancoDados


@app.route('/',  methods=['GET', 'POST'])
def home():
    enviaremail = EnviarEmail()

    if enviaremail.validate_on_submit():
        novo_email= EmailBancoDados(
            username = enviaremail.username.data,
            email = enviaremail.email.data,
            telefone = enviaremail.telefone.data,
            suamensagem = enviaremail.suamensagem.data
        )

        database.session.add(novo_email)
        database.session.commit ()
        print('Dados Salvos com sucesso!')

        return redirect(url_for('sucesso'))
    return render_template('home.html', enviaremail = enviaremail)



@app.route ('/sucesso')
def sucesso():

    return render_template('sucesso.html')
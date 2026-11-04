from flask_wtf import  FlaskForm
from wtforms import  StringField, SubmitField,IntegerField , TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length , Email




class EnviarEmail(FlaskForm) :
    username = StringField ('Nome Completo', validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    telefone = StringField ('Numero de telefone:', validators=[DataRequired(),Length(10 , 20)])
    suamensagem = StringField ('Deixe a sua mensagem')
    botao_enviar_email = SubmitField('Enviar')

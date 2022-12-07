# Objetivo: Criar uma API que disponibiliza a consulta, criação, edição e exclusão de livros.

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O senhor dos anéis - A sociedade do anel',
        'autor': 'J.R.R Tokien' 
    },
       
    {
         'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling' 
    },

    {
         'id': 3,
        'titulo': 'Hábitos Atômicos',
        'autor': 'James Clear' 
    }

]
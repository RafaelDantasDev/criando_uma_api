# Objetivo: Criar uma API que disponibiliza a consulta, criação, edição e exclusão de livros.

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O senhor dos anéis - A sociedade do anel'
    }
]
from flask import Flask, jsonify, request

api=Flask(__name__)

livros = [
    {
        'id': 1,
        'Título':'Battlefield 3',
        'Autor' : 'McNAB'
    },
    {
        'id': 2,
        'Título':'Harry Potter e a Pedra filosofal',
        'Autor': 'J.K Howling'
    },
    {
        'id': 3,
        'Título' : 'Garota Exemplar',
        'Autor' : 'Gillian Flynn'
    },
]
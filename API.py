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

#Consultar livros
@api.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar (id)
@api.route('/livros/<int:id>',methods=['GET'])
def consultar_livro_por_id(id):
    for livro in livros:
       if livro.get('id') == id:
            return jsonify(livro)

#Editar
@api.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado=request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


api.run(port=5000,host='localhost',debug=True)
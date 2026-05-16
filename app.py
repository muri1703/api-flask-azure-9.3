from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "Dom Casmurro"
    },
    {
        "id": 2,
        "titulo": "Berserk"
    }
]

# GET
@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)

# POST
@app.route("/livros", methods=["POST"])
def adicionar_livro():
    novo_livro = request.json
    livros.append(novo_livro)

    return jsonify({
        "mensagem": "Livro adicionado",
        "livro": novo_livro
    })

# PUT
@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    dados = request.json

    for livro in livros:
        if livro["id"] == id:
            livro["titulo"] = dados["titulo"]

            return jsonify({
                "mensagem": "Livro atualizado",
                "livro": livro
            })

    return jsonify({
        "erro": "Livro não encontrado"
    }), 404

# DELETE
@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):

    for livro in livros:
        if livro["id"] == id:
            livros.remove(livro)

            return jsonify({
                "mensagem": "Livro removido"
            })

    return jsonify({
        "erro": "Livro não encontrado"
    }), 404

if __name__ == "__main__":
    app.run()
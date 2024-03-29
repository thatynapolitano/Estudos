from flask import Flask, jsonify, request, Response

app = Flask(__name__) # intância o método Flask

@app.route("/", methods=["GET"]) # define o endpoint da página
@app.route("/homepage", methods=["GET"]) # define o endpoint da página
def homepage():
    return jsonify("essa é a homepage")

@app.route("/ada", methods=["GET"]) # define o endpoint da página
def pagina_ada():
    return jsonify("essa é a página ada")

# (simulando um banco de dados)
dados_alunos = [
    {"id": 1, "nome": "Renan", "idade": 34, "comida_favorita": "Nhoque"},
    {"id": 2, "nome": "Erick", "idade": 29, "comida_favorita": "Xis"},
]
# endpoint para retornar todos os dados 
@app.route("/alunos", methods=["GET"])
def retorna_alunos():
    return jsonify(dados_alunos)


# filtrando para retornar o id do aluno
@app.route("/aluno/<int:id>", methods=["GET"])
def retorna_aluno(id):
    if id is None: 
        return jsonify(dados_alunos)  # Quando nao ha nenhum id, retorna a lista de todos os alunos
    for aluno in dados_alunos:
        if aluno.get("id") == id:
            print(f"Encontrei o aluno do id {id}: {aluno}")
            return jsonify(aluno)
    return jsonify({"message": "Aluno nao encontrado"})   # tratamos quando o ID nao existe para a filtragem


# adicionar um aluno novo  
@app.route("/aluno", methods=["POST"])
def incluir_novo_aluno():
    novo_aluno = request.get_json()
    dados_alunos.append(novo_aluno) # é preciso checar antes do append se os dados que querem adicionar na API estao de acordo com o padrao e formato
    #neste ponto salvar os dados em um arquivo csv/banco de dados, pois toda vez que eu reinicio a API, eu perco os dados adicionados pelo POST
    return jsonify(dados_alunos)

# Alterar aluno no banco de dados
@app.route("/aluno/<int:id>", methods=["PUT"])
def alterar_aluno(id):
    aluno_alterado = request.get_json()
    for aluno in dados_alunos:
        if aluno.get("id") == id:
            aluno.update(aluno_alterado)
            print(f"\n\nDEBUG: {aluno}")
            return jsonify(aluno)

# Deleta aluno no banco de dados 
        
@app.route("/aluno/<int:id>", methods=["DELETE"])
def deleta_aluno(id):
    for aluno in dados_alunos: 
        if aluno.get("id") == id:
            dados_alunos.remove(aluno)
            print(f"\n\nDEBUG: {dados_alunos}")
            return jsonify(dados_alunos)


# Criamos um rota de csv para fazer download de um csv 
@app.route('/csv')
def csv():
    data = u'1,2,3\n4,5,6\n'
    bom = u'\ufeff'
    response = Response(bom + data, content_type='text/csv; charset=utf-16')
    return response

app.run(debug=True) # inicializa o servidor



from flask import Flask, request
from flask_restful import Resource, Api

from pessoa import retorna_pessoas, insere_pessoa

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return "Uhuuu"

class Pessoa(Resource):
    def get(self):
        pessoas = retorna_pessoas()
        return pessoas

    def post(self):
        pessoa = request.json
        insere_pessoa(pessoa)
        return  "Pessoas inseridas com sucesso!"



api.add_resource(HelloWorld, "/")
api.add_resource(Pessoa, "/pessoas")


if __name__ == "__main__":
    app.run(debug=True)

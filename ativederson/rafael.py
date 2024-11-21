from pydantic import BaseModel
class Usuario(BaseModel):
    nome:str
    idade:int
    sexo:str
Usuario = Usuario(nome= "Hugo", idade = 18, sexo = "masculino")
print(Usuario.nome)
print(Usuario.sexo)
print(Usuario.idade)


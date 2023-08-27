#Este exemplo usa um banco chamado code_example com usuário postgres e senha postgres.
import postgresql
db = postgresql.open(user = 'postgres', database = 'code_example',
port = 5432, password='postgres')

# Executando operações no banco de dados:
# Esta operação cria uma tabela pessoa no banco com os campos nome e idade. Ela deve ser executada apenas uma vez.
db.execute("CREATE TABLE pessoa (nome text PRIMARY KEY,
idade int)")

# Preparando uma query:
# Quando usamos a operação prepare temos como retorno uma função que será chamada com a mesma quantidade de argumentos que os definidos na String ($i).
INSERT:
save_person = db.prepare("INSERT INTO pessoa VALUES ($1, $2)")

#db.xact() é usado para representar uma transação. caso mais
#métodos save_person fossem chamados, só seriam gravado 
#no banco caso todos executassem corretamente.
with db.xact():
 save_person("Bruno Bastos", 23)

UPDATE:
increase_age = db.prepare("UPDATE pessoa SET idade = idade + 1 
WHERE nome = $1")

with db.xact():
 increase_age("Bruno Bastos")

SELECT:
get_person_by_name = db.prepare("SELECT * FROM pessoa 
WHERE nome = $1")
get_person_ordered_by_age = db.prepare("SELECT * FROM pessoa 
ORDER BY idade")

with db.xact():
 result = get_person_by_name("Bruno Bastos")

#temos que iterar sob o resultado mesmo que seja apenas uma linha
for row in result:
 print("Nome: ", row["nome"], "Idade: ", row["idade"])

#Insira mais alguns dados no banco para ver o funcionamento do método
with db.xact():
 result = get_person_ordered_by_age()

print("Registros ordenados por idade")
for row in result:
 print("Nome: ", row["nome"], "Idade: ", row["idade"])
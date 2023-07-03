Para download dos pacotes use:

pip install requirements.txt

Para executar o servidor use:

uvicorn main:app --reload

Na pasta config no arquivo database.py contém a URL de conexão com o banco de dados.

O servidor estará escutando a porta 8000

Para consultar a documentação da API, acesse http://127.0.0.1:8000/docs e para interomper a execução pressione «Ctrl»+«C».

Em http://127.0.0.1:8000/docs é possivel acessar os usuarios/admin, fazendo cadastro, modificar e deletar
Para fazer cadastro da skin é necessario um login/senha de um admin, na raridade é necessario usar ES = Edicao Selecionada, ED = Edicao Deluxe, EP = Edicao Premium, EU = Edicao Ultra, EX = Edicao Exclusiva, junto com seu valor, imagem e nome da skin.


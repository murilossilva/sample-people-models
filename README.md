# Aplicando conceitos de Models em uma Coleção

Esse projeto foi desenvolvido durante estudo sobre conceitos de models em Django. O intuito principal foi a geração de models através da população de uma tabela 
por meio de um arquivo csv, gerado gratuitamente pelo site [4devs](https://www.4devs.com.br/gerador_de_pessoas).
Além disso, também foram desenvolvidas algumas querys para a consulta dos dados.

<h2>Requirements</h2>

Após a realização do git clone do repositório é necessário, em seu terminal, ir até a raiz do projeto e executar o comando: 

`pip install requirements.txt` 

Ao executar o pip install será instalado os pacotes necessários para a execução correta do projeto e suas dependências.

Na sequência já podemos popular a tabela de pessoas com o comando `py manage.py load_people_data`, ele irá consumir os dados presentes no .csv
e transformará todas as pessoas em objetos Python.

Com a tabela populada já podemos seguir para a execução do projeto e suas queries.

<h2>Queries Executions</h2>

Ainda na raiz do projeto, podemos digitar `py manage.py shell` no próprio terminal, ele dará acesso ao iphyton, onde podemos fazer execuções no projeto dentro do próprio terminal.

Com o shell inicializado, para um melhor ambiente, sugiro importar o pacote pandas, para isso digitamos `import pandas as pd` 

Para facilitar o uso das queries, construi alguns métodos dentro da classe People que possibilitariam as mesmas. Listarei as queries prévias, lembrando que também é possível
realizar demais através do próprio terminal. Os comandos presentes dentro do projeto são:

`People.objects.alphabetical()` - esse comando retorna todas pessoas da tabela ordenadas alfabeticamente.

`People.objects.younger(n)` - essa query retorna as n pessoas mais jovens presentes na tabela. Onde n deve ser obrigatoriamente um número inteiro.

`People.objects.older(n)` - semelhante ao comando anterior, esse retorna as n pessoas mais velhas presentes na tabela.

`People.objects.mans()` - retorna o número de pessoas de sexo masculino na população da tabela.

`People.objects.womans()` - retorna o número de pessoas de sexo feminino na população da tabela.

`People.objects.search_name(blablabla)` - essa consulta retorna as informações de uma pessoa ou coleção de pessoas, que comecem com o mesmo nome ou parte dele. 
Por exemplo, no parâmetro blablabla, podemos passar b ou B, e a consulta retornará todas as pessoas da tabela que comecem com a letra B. A consulta é case insensitive, 
ou seja, não há problema em digitar de forma minúscula ou maiúscula, sempre retornará o mesmo resultado, desde que haja alguém na tabela que cumpra com o que foi digitado.

`People.objects.to_json(nome_completo_da_pessoa)` - por fim, temos o comando que retorna todas as informações, em formato json, presentes na tabela de uma única pessoa, para a execução correta
 é necessário digitar o nome completo da pessoa no parâmetro da consulta.
 
 **Obs.: Para a execução dos comandos é necessário que a tabela esteja devidamente populada, caso contrário não será possível, dado que o programa interpretará que não há ninguém
 na população**
 
<h2>Visualização no navegador</h2>

Além da visualização dos dados via terminal, o programa conta com uma visualização no navegador, onde é possível inserir novas pessoas também. 

Para realizar a visualização basta ir na pasta raiz do projeto e executar o comando `py manage.py runserver`. Em seu navegador, digite `localhost:8000` na barra de pesquisa.

Após isso você poderá visualizar uma interface, no menu de navegação superior tem a opção de listar as pessoas já existentes, assim como inserir novas pessoas. Caso você insera 
alguém e depois tente popular a tabela com os dados do arquivo csv, não será possível, pois o programa ainda não conta com essa opção. É algo a ser implementado no futuro. 
Entretanto, é totalmente possível inserir novas pessoas mesmo após popular a tabela, basta ir na opção Inserir Pessoas no navegador.
 
<h2>Outras infos</h2>
 
O projeto tem a possibilidade de realizar querys ainda mais complexas, para tanto é necessário realizá-las via terminal e conhecer a sintaxe e usos.
 
Instagram: https://www.instagram.com/original.mancha/

Linkedin: https://www.linkedin.com/in/murilossilva/

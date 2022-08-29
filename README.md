# 📍 sistema-de-vendas

<p>Este repositório é destinado ao sistema de vendas<p/>
<h3>tecnologias utilizadas</h3>
<ul>
  <li>Linguagem: Python</li>
  <li>Framework: Django rest framework</li>
  <li>Banco de dados: SqlLite</li>
</ul>


## Startando o sistema no seu pc:

* 1 - clone o repositório, utilizando o terminal, com o git previamente instalado no pc, digite o comando:

```
  git clone git@github.com:JoonMarion/sistema-vendas-POOII.git
```
or

```
 git clone https://github.com/JoonMarion/sistema-vendas-POOII.git
```

* 2 - em seguida entre na pasta que será criada no seu pc, através do comando:
```
  cd sistema-vendas-POOII
```

* 3 - após o passo 2, então com o python pré-instalado(3.10), instale o comando pip(windows):

```
  python get-pip.py
```
or
* 3.1 - instalação do comando pip no Linux:
```
 sudo apt install pip
```

* 4 - em seguida, rode o comando abaixo para gerar sua virtual env:
```
  python3 -m venv venv
```

* 5 - se estiver tudo certo, será gerado um arquivo venv no projeto, que será ignorado e não versionado, no seu terminal rode o comando abaixo para ativar sua venv (windows):

```
  venv/Scripts/Activate
```
or
* 5.1 - para ativar sua venv no linux, rode o comando abaixo:

```
  source venv/bin/Activate
```
* 6 - após ativada sua virtual env, irá aparecer o nome dela no seu terminal acima do seu command line, sem seguida rode o comando abaixo, para baixar as dependências do projeto:
```
  pip install -r requirements.txt
```

* 7 - Uma vez instalada as dependências, rode o comando abaixo para rodar o sistema:
```
  python manage.py runserver
```

<p> se tudo ocorrer bem, a api estará funcionando, você pode utilizar o postman para teste de verbos http ✔️ <p/>

:rotating_light::rotating_light::rotating_light:
<h3>Comandos importantes</h3>
<ul>
  <li>python manage.py makemigrations -> comando prepara as migrações para o banco de dados</li>
  <li>python manage.py migrate -> comando realiza as migrações para o banco de dados</li>
</ul>
:rotating_light::rotating_light::rotating_light:

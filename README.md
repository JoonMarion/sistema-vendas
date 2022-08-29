# 📍 sistema-de-vendas

<p>Este repositório é destinado a construção de uma api de noticias com django e django rest framework<p/>


## Startando a API no seu pc:

* 1 - clone o repositório, utilizando o terminal, com o git previamente instalado no pc, digite o comando:

```
  git clone https://github.com/igor-dantas/sistema-de-vendas.git
```

* 2 - em seguida entre na pasta que será criada no seu pc, através do comando:
```
  cd sistema-de-vendas
```
* 3 - após o passo 2, então rode o comando do docker, com o docker previamente instalado na máquina:

```
  docker-compose build
```

* 4 - em seguida, rode o comando:
```
  docker-compose up
```

* 5 - se estiver tudo certo, será gerado um link parecido com este, no seu terminal:

```
  http://0.0.0.0:8000
```
* 5.1 - substitua 0.0.0.0 por localhost, gerando o link:
```
http://localhost:8000
```
* 6 - 🛑 após a utilização da api, recomendo que rode o comando abaixo, afim de interromper e remover os containers:
```
  docker-compose down
```

<p> se tudo ocorrer bem, a api estará funcionando, você pode utilizar o postman para teste de verbos http ✔️ <p/>
# MobileChallenge
Este projeto é o resultado do Desafio Muxi Mobile-QA


## O desafio
Foi proposto o desenvolvimento de uma aplicação que acesse uma url utilizando Get e, a partir do Json obtido, realize as seguintes funcionalidades obrigatórias:

* Lista de frutas.
* Cada Item da lista deve exibir o nome da fruta e preço em dólar.
* Quando for selecionado um item da lista, deverá ser apresentada mais informações: O nome e preço em dólar e em real.
* O preço em real deverá ser calculado, sendo que 1 dólar corresponde a 3,5 reais.
* Testes no projeto

Podendo também apresentar as seguintes funcionalidades extras:

* Realizar o cálculo do preço em real assincronamente utilizando um método em c ou c++
* Framework para comunicação com API e testes
* README com explicações sobre o projeto, decisões tomadas, como gerar o programa e como rodar os testes

## Pré-requisitos
Para que o projeto funcione corretamente, os seguintes Softwares e módulos são necessários:
* Python 2.7
  * threading
  * os
  * requests
  * json
  * math
  * time
  * ctypes
  * unittest
* Compilador C++

### Detalhes
**unittest** é um framework de testes unitários para python. Ele foi utilizado para construir todos os testes encontrados no projeto.
**threading** é um módulo que auxilia na criação e gerenciamento de threads dentro de uma aplicação python. Ele foi utilizado para fazer com que as chamadas ao método em C, assim como o Get na url, fossem realizados assincronamente.
**ctypes** é um módulo que disponibiliza tipos de dado compatíveis com o C, possibilitando utilizar métodos escritos em C dentro da aplicação construída em Python.

## Estrutura
O projeto está divido em 3 principais arquivos. 
1. **fruitShop.py** é o script onde a aplicação foi desenvolvida. Deve ser executado para iniciar a aplicação.
2. **main.so** é o arquivo escrito em C++ que possui a função _valueExchanger(double value)_, responsável por converter o valor de dólar para real. Foi utilizado _extern "C"_ para possibilitar a utilização da função através do módulo ctypes.
3. **test_fruitShop.py**, script onde estão localizados todos os testes unitários responsável por validar o comportamento das funções descritas em **fruitShop.py**.

### Arquivos .bat
Na raiz do projeto existem os 2 seguintes arquivos:
1. **runPy.bat** que iniciará a aplicação.
2. **runTests.bat** que iniciará os testes.

Caso o caminho de instalação do python seja diferente do que está nesses arquivos, é necessário alterar para que funcionem corretamente.


# Compilador OWL

Este projeto implementa um compilador para processar arquivos de entrada e identificar tokens, palavras reservadas, tipos de dados, e outros elementos importantes, como classes, propriedades, namespaces, e mais. Ele foi desenvolvido com a biblioteca ply para Python, e exibe os resultados de forma amigável no terminal.

## 🚀 Começando
Para clonar o projeto, rode esse comando no terminal
```
git clone https://github.com/PedroPereiraJPPF/AnalisadorLexicoOWL2.git
```
### 🔧 Instalação
#### WINDOWS

É Necessario instalar o [Python](https://www.python.org/downloads/).
Após isso Digite: 
```
pip install -r requirements.txt
```

Esse comando serve para instalar todas as dependências do projeto

#### Linux
É Necessário instalar o [Python](https://www.python.org/downloads/).
No linux pode ser necessario ativar um ambiente de desenvolvimento virtual:
```
Digite no terminal: 
source ply-venv/bin/activate 
```
Isso serve para ativar o ambiente que já vem com o projeto
Após isso instale todas as dependências do projeto através do seguinte comando:
```
pip install -r requirements.txt
```
## 🖥️ Funcionamento
### Analisador Léxico

O analisador léxico produzido é capaz de reconhecer um grupo pré-definido de lexemas, dentre eles estão algumas palavras reservadas, caracteres especiais, nomes de classes, entre outros.  
O armazenamento dos lexemas e símbolos foi feito em um mapa, com o objetivo de organizar automaticamente os lexemas, eles estão organizados em ordem alfabética.  
O código se encontra separado em três partes, o arquivo main.jflex que contém as declarações de todas as regex e as instruções de como seguir ao encontrar cada caso delas, o arquivo Lexer.java que foi gerado automaticamente pelo JFlex a partir do main.jflex e contém todas as instruções para o java interpretar o arquivo .jflex, e o Main.java que chama os métodos do lexer, o executa e exibe os resultados.  
Há mais um arquivo, o input.txt, que é o arquivo que será lido e analisado pelo interpretador, mas ele não possui nenhuma particularidade além de ter de ser escrito em OWL 2 com Manchester Syntax para ser devidamente interpretado.

### Analisador Sintático
O Analisador Sintático se utiliza do analisador léxico para classificar as várias sentenças presentes em um código da linguagem analisada, nesse caso OWL2.
O analisador produzido confere a estrutura de seis classes da linguagem, classes primitivas e definidas, que podem ser acompanhadas de qualquer combinação de outras 4, classes aninhadas, enumeradas, cobertas e com axioma de fechamento.
### Funcionamento Prático
Basta entrar no arquivo `interface.py` e roda-lo com o VSCode.
![Print de como o terminal deve se parecer após rodar o arquivo](https://i.postimg.cc/WpFWpMFk/imagem-2025-01-16-220652175.png)


## 🛠️ Construído com
* [Python](https://www.python.org/downloads/) - Linguagem usada
* [PLY](https://ply.readthedocs.io/en/latest/index.html) - Bibliote principal
* [VSCode](https://code.visualstudio.com/download) - IDE utilizada
## ✒️ Autores

* **João Pedro Pereira Frutuoso** - *Desenvolvedor* - [Pedro](https://github.com/PedroPereiraJPPF)
* **Artur Segantini Guedes** - *Desenvolvedor* - [Artur](https://github.com/ARTSALT)

## 📄 Licença

Este projeto está sob a licença [MIT](https://mit-license.org).

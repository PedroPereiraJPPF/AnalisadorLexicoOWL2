# 📊 Analisador Léxico - Lexer Python

Este projeto implementa um analisador léxico (lexer) para processar arquivos de entrada e identificar tokens, palavras reservadas, tipos de dados, e outros elementos importantes, como classes, propriedades, namespaces, e mais. Ele foi desenvolvido com a biblioteca `ply` para Python, e exibe os resultados de forma amigável no terminal.

---

## 🚀 **Instruções de Instalação e Execução**

Siga os passos abaixo para instalar e executar o software no seu ambiente local.

### 1. **Clonando o Repositório**

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/analisador-lexico.git
cd analisador-lexico
2. Instalando Dependências
Certifique-se de ter o Python instalado na sua máquina. Caso não tenha, você pode baixar o Python aqui.

Instale as dependências do projeto usando o pip:

bash
Copiar código
pip install ply
3. Executando o Software
Para rodar o analisador léxico, basta fornecer o caminho do arquivo que você deseja analisar. O software vai processar o arquivo e exibir as tabelas de símbolos e erros lexicais encontrados.

Execute o seguinte comando:

bash
Copiar código
python interface.py
O programa solicitará que você forneça o caminho do arquivo de entrada.

📝 Como Usar
Após rodar o programa, o fluxo será o seguinte:

Entrada do Caminho do Arquivo: Você será solicitado a fornecer o caminho de um arquivo de texto que deseja analisar.

Exemplo:

javascript
Copiar código
Digite o caminho do arquivo para análise: /caminho/para/o/arquivo.txt
Análise Lexical: O software irá analisar o conteúdo do arquivo e identificará os seguintes componentes:

Palavras Reservadas: Como SOME, ALL, VALUE, etc.
Classes e Propriedades: Como nomes de classes e propriedades em seu código.
Datatypes e Cardinalidades: Tipos de dados e valores cardinais.
Erros Lexicais: Caso haja algum erro de sintaxe ou token inválido, será exibido um relatório com a linha e a coluna do erro.
Resultados: O programa exibirá duas seções principais no terminal:

Tabela de Símbolos: Mostrando os diferentes tipos de tokens encontrados no arquivo.
Erros Lexicais: Relatando qualquer erro encontrado durante a análise.
⚙️ Estrutura de Diretórios
A estrutura do projeto é a seguinte:

graphql
Copiar código
analisador-lexico/
├── lexer.py          # Contém o analisador léxico e a lógica de processamento.
├── interface.py      # Interface que exibe os resultados ao usuário.
├── README.md         # Este arquivo.
└── requirements.txt  # Arquivo com as dependências do projeto.
🛠️ Tecnologias Usadas
Este projeto utiliza as seguintes tecnologias:

Python 3.x: Linguagem de programação.
PLY (Python Lex-Yacc): Biblioteca para análise léxica.
Terminal/Console: Interface de linha de comando para interação com o usuário.
💡 Exemplo de Saída
Após processar o arquivo, a saída pode se parecer com isto:

Tabela de Símbolos:
markdown
Copiar código
=========================================
Tabela de Símbolos:
=========================================
Keywords:
------------------------------
    Lexema: some
        Ocorrências: 2
    Lexema: all
        Ocorrências: 1
    Lexema: value
        Ocorrências: 3

Classes:
------------------------------
    Lexema: ClassA
        Ocorrências: 5
    Lexema: ClassB
        Ocorrências: 2

Properties:
------------------------------
    Lexema: propertyX
        Ocorrências: 4
    Lexema: propertyY
        Ocorrências: 3
Erros Lexicais:
perl
Copiar código
=========================================
Erros Lexicos encontrados:
=========================================
Erro no caractere '!' na linha 5, coluna 12.
Erro no caractere '$' na linha 8, coluna 4.
🚧 Contribuindo
Se você quiser contribuir para este projeto, fique à vontade para fazer um Fork e enviar um Pull Request.

Para garantir a melhor qualidade do código, siga as boas práticas de programação e escreva testes, caso faça alterações significativas.

🔑 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

🧑‍💻 Contato
Autor: Pedro
Email: pedro.exemplo@dominio.com
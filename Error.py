class Error:
    def __init__(self, value, line, column):
        self.value = value 
        self.line = line
        self.column = column

    def __str__(self):
        return f"Erro no caractere '{self.value}' na linha {self.line}, coluna {self.column}."
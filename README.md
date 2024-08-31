# Tradutores

Ciência da Computação (Híbrido) - 2024/2

Trabalho realizado por:
- Eduarda Vargas dos Santos
- Guilherme Mathias Dörr
- Leonardo Ribeiro Agustoni Feilke

# Como rodar

## Instalar dependências:
```
  $ pip install antlr4-python3-runtime 
  OU 
  $ pip install -r requirements.txt
```

## Rodar o arquivo main.py
```
  $ python3 main.py 
```

## Digitar a expressão e visualizar o resultado. 
### Exemplos: 
```
> int a, b, c;
(declaration (intDecl int (identifierList a , b , c)) ;)

> char a[10], b;
(declaration (charDecl char a [10] , b) ;)

> float a123_, b123_, c123_;   
(declaration (floatDecl float (identifierList a123_ , b123_ , c123_)) ;)

> int a
line 1:5 missing ';' at '<EOF>'
(declaration (intDecl int (identifierList a)) <missing ';'>)

> int 1_;
line 1:4 token recognition error at: '1'
(declaration (intDecl int (identifierList _)) ;)

> int 1;
line 1:4 token recognition error at: '1'
line 1:5 missing IDENTIFIER at ';'
(declaration (intDecl int (identifierList <missing <INVALID>>)) ;)
```

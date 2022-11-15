# Laboratório de compiladores 

## Função Principal
```
:m:(){
    string hello :=: "Hello World";
    :p:(hello);
    . aqui vem o comentário de uma linha .
    ..
    aqui vem um comentário com varias linhas
    ..
}
```
## Operadores aritméticos, relacionais e lógicos
|Função|Simbolo|
|---|---|
and|:&&:
or|:\|\|:
Equal (assign value)|:=:
not|:!:
Equal comparison|:==:
addition|:+:
subtraction|:-:
multiplication|:*:
division|:/:
power|:^:
less than|:<:|
bigger than|:>:|
increment|:++:|
decrement|:--:|

## Tipos de variáveis

String  

Number  


## Declaração de variável 
```
Type name;
```
Type(Tipo da variável a ser declarada)
name(Nome atribuido a variável)

## Atribuição de valor à variável 
```
name :=: value;
Type name :=: value;
```
### Exemplos:
```
string foo :=: "bar";
string barbar :=: 'foo';
number index;
```
## Estrutura(s) de decisão 
|Operador|Simbolo|
|---|---|
|If|:cond:(){}|
|Else|:!cond:{}|
|Else if|:!cond:(){}|
```
# Exemplos
:cond:(foo :==: bar){
    # faz alguma coisa
}
:!cond:( foo :!::=: "" ){
    # faz outra coisa    
}
:!cond:{
    # default
}
```

## estrutura(s) de repetição
|*Tipo de Repetição*|*Simbolo*|*Exemplo*|
|---|---|---|
|for|:f:|```:f:(number i:=:0; i:<:10; i::+::){}```|
|while|:w:|```:w:(foo ::=:: bar){}```|


## declaração e uso de funções
### Declaração
```
:nomeDaFunçao:(string foo, number bar){

}
```

### Uso
```
number res :=: :nomeDaFunção:("Foo",1);
```

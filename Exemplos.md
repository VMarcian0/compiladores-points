## 1 - Calculo de média recebendo 3 notas com pesos diferentes

```
:m:(){
    number nota1 :=: -1;
    number nota2 :=: -1;
    number nota3 :=: -1;

    :w:(nota1 :<: 0 :||: nota1 :>: 10){
   		nota1 :=: :input:();
	}
    :w:(nota2 :>: 0 :||: nota2 :<: 10){
    	nota2 :=: :input:();
	}
    :w:(nota3 :>: 0 :||: nota3 :<: 10){
    	nota3 :=: :input:();
	}
 
    number média :=: (nota1:*:0.15):+:(nota2:*:0.3):+:(nota1:*:0.5)

    :print:(média)
}
```

## 2- Imprime os números menores do que um terço do número escolhido e maiores do que dois terços
```
:m:(){

	number check;
	check :=: :input:();

	:f:(number i:=:0; i:<:check; i:++:){
		:cond:(i :<: check:/:3 :||: i:>:(check:-:check:/:3)){
			:print:(i)
		}
	}
}
```


## 3- Retorna se é possível existir um triangulo com o tamanho dos três lados escolhidos
```
:m:(){

    number lado1 :=: :input:();
    number lado2 :=: :input:();
    number lado3 :=: :input:();

	:cond:(lado1 > lado2 :+: lado3){
		:print:(Não é um triângulo)
	}
	:!cond:(lado2 > lado1 :+: lado3){
		:print:(Não é um triângulo)
	}
	:!cond:(lado3 > lado1 :+: lado2){
		:print:(Não é um triângulo)
	}
	:!cond:{
		:print:("É um triângulo")
	}
}
```

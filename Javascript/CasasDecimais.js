// Como transformar um numero quebrado em 2 casas decimais e trocar ponto por virgula

let number = 397.343242342 
console.log(number.toFixed(2).replace(".",","))

// No exemplo acima, declaramos uma variável number com números com muitas casas decimais. Isso na primeira linha.
// Na segunda linha, aprendemos que um objeto de tipo numero pode ter uma funcionalidade (método) toFixed e replace. 
// O .toFixed e ao lado a quantidade, no caso 2, coloca o nosso numero apenas aparecendo com duas casas decimais.   
// E o .replace   acompanhado dessas strings . e , transforma o ponto do numero em virgula. 

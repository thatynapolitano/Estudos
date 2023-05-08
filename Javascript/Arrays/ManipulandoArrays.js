// Manipulando Arrays 

let techs = ["hmtl", "css", "js"] 
console.log(techs)

// adicionar um item no fim:
techs.push("nodejs")
console.log(techs)

// adicionar no comeco um item no array:
techs.unshift("sql")
console.log(techs)

// remover do fim:
techs.pop()
console.log(techs)

// remover do comeco:
techs.shift()
console.log(techs)

// pegar somente alguns elementos do array:
//console.log(techs.slice(1,3))

// No slice sao sempre 2 argumentos. Uso o slice fatiar uma parte do meu array, no caso quero apenas o elemento de posicao 1 do array ate o ultimo elemento. O segundo numero eh correpondente a quantidade de elementos, ate qual quantidade eu quero ir. Ou seja, nao confundir com posicionamento de elemento e sim o segundo numero eh quantidade de elementos. O slice nao faz mudancas no array.

// remover 1 ou mais itens em qualquer posicao do array:
//techs.splice(1,2)
//console.log(techs)

//O splice faz mudancas no array. No splice tambem sao sempre 2 argumentos. O primeiro argumento eu falo qual o index do array (o que eu quero tirar), no exemplo vai ser o CSS, que eh o 1. No segundo argumento eu digo quantos elementos eu quero tirar a partir do qual eu escolhi, no caso 2, que vai ser JS. No console vai ser impresso apenas HTML, por exemplo. 

// Quando eu nao sei a posicao do array (INDEX) que eu quero remover, entao para encontrar a posicao de um elemento no array: 

let index = techs.indexOf('css')
techs.splice(index, 1) // Se eu quiser remover  o CSS 
techs.splice(index, 2) // Se eu quiser remover o CSS e o proximo dele e por ai vai...
console.log(techs) 











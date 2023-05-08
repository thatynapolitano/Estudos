// Separe um texto que contem espaços em um novo array onde cada texto é uma posição do array. Depois disso, transforma o array em um texto e onde eram espaços, coloque _ 

let phrase = "Eu quero viver o Amor!" // Criamos um texto primeiro
let myArray = phrase.split(" ") // Depois separamos cada elemento do texto, ou seja cada letra do texto incluindo os espacos, em uma posicao do array. OBS: Caso eu queira retirar uma letra do texto, eu poderia colocar entre "" uma letra. No caso, se eu colocasse a letra O , sumiria todos os O's da minha frase.
console.log(myArray) // Aqui podemos ver o resultado disso
let phraseWithUnderscore = myArray.join("_") // Depois criamos a nossa frase com o undercore: _ . phraseWithUnderscore = myArray e adicionamos o metodo join, que adiciona todos os elementos de uma array em uma string separando cada elemento pelo separador de string especificado que no caso eh o underscore: _   OBS: Caso eu quisesse alterar o underscore para espaco, ou virgula, ou qualquer outro elemento eu posso. As letras serao separadas por um elemento diferente.
console.log(phraseWithUnderscore) // Pronto, temos o que foi pedido o exercicio, ate essa linha.


// Se eu quisesse brincar mais um pouco eu poderia adicionar um metodo para a minha variavel de string. Que no caso abaixo eh o toUpperCase, deixando todas as minhas letras maiusculas.

console.log(phraseWithUnderscore.toUpperCase()) 
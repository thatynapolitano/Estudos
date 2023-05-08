// Como verificar se o texto contem a palavra amor 

let phrase = "Eu quero viver o amor!" 
console.log(phrase.includes("amor"))

// Para encontrar palavras em frases existe um método chamado includes. 
// Entao primeiramente eu crio uma frase. E depois eu imprimo a frase com o método includes e dentro () coloco a palavra que eu quero saber se existe na frase, que no caso abaixo é a palavra “amor”.  O console.log vai imprimir TRUE. 

// Porém o método includes só vai funcionar quando a palavra que queres saber se existe, for igual a da frase. Então precisa incluir palavras em caixa alta ou não, caso exista. 


console.log(phrase.includes("Amor")) // Nesse exemplo, vai aparecer FALSE. Pois a palavra “Amor” não existe, apenas “amor” com a primeira letra em minúscula. Amor com a primeira letra maiúscula não existe na frase.

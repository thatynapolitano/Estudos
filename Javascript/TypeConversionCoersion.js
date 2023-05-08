console.log('9' + 5) // Printa 95. O js faz uma type coersion para forcosamente nao haver erro na nossa aplicacao. Ou seja, transforma a string 9 em number e faz a concatenacao dos numeros. 

console.log(Number('9') + 5) // Printa 14. Consegui fazer a soma dos numeros fazendo type conversion. Ou seja, uma conversao de dados feita /manualmente e nao pelo JS. Assim tenho o resultado esperado. 

// Essa é a diferença entra type coersion e type conversion (typecasting). A primeira é uma conversão de tipos de dados em outro tipo de dado feita pelo JS e a outra é uma conversão feita manualmente pelo DEV.
 




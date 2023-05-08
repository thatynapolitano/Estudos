// Como contar quantos caracteres tem uma palavra e quantos digitos tem um numero

let word = "Paralelepipedo" 
console.log(word.length) // Para saber qual o número de caracteres tem em uma palavra. No caso da palavra paralelepípedo temos 14 caracteres. Eles serão contados quando usarmos word.lenght , juntamente do console.log sera printado a quantidade de caracteres. 

let number = 1234
console.log(String(number).length) // Mas number não lê Length, apenas string. Por isso não vai funcionar e aparecerá no console Undefined. Para então saber quantos dígitos possui um numero, é preciso converte-lo antes para string. 
// E aí sim podemos colocar o .length , pois o number já foi transformado em string. 

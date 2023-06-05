/* Celsius em fahrenheit

Crie uma funcao que receba uma string em celsius ou fahrenheit e faca a transformacao de uma unidade para outra
 
C = (F - 32) * 5/9

F = C * 9/5 + 32 

*/ 

let fahrenheit = 34
let celsius = (fahrenheit - 32) * 5/9

function graus (fahrenheit) {
    return celsius 
}

console.log(graus()); 
 
// Outro jeito 

function transformDegree(degree) {
    const celsiusExists = degree.toUpperCase().includes("C")
    const fahrenheitExists = degree.toUpperCase().includes("F")

    if(!celsiusExists && !fahrenheitExists) {
        throw new Error("Grau nao identificado")
    }
}

try {
    transformDegree("50F")
    transformDegree("50Z")
} catch (error) {
    console.log(error.message)
}


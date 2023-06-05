/* Celsius em fahrenheit

Crie uma funcao que receba uma string em celsius ou fahrenheit e faca a transformacao de uma unidade para outra
 
C = (F - 32) * 5/9

F = C * 9/5 + 32 

*/ 

function transformDegree(degree) {
    const celsiusExists = degree.toUpperCase().includes("C")
    const fahrenheitExists = degree.toUpperCase().includes("F")

    if(!celsiusExists && !fahrenheitExists) {
        throw new Error("Grau nao identificado")
    }

    // fluxo ideal, F para C
    let updatedDegree = Number(degree.toUpperCase.replace("F", ""));  
    let formula = (fahrenheit) => (fahrenheit - 32) * 5/9
    let degreeSign = "C"
    
    if(celsiusExists) {
        updatedDegree = Number(degree.toUpperCase.replace("C", ""));  
        let formula = (celsius) => celsius * 9/5 + 32
        let degreeSign = "F"
    }

    return formula(updatedDegree) + degreeSign

}

try {
    console.log(transformDegree("50C"))
    transformDegree("50Z")
} catch (error) {
    console.log(error.message)
}

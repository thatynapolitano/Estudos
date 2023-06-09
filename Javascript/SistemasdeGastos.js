/*  Crie um objeto que possuirá 2 propriedades, ambas do tipo array:
* receitas: [] 
* despesas: []
Agora, crie uma função que irá calcular o total de receitas e 
despesas e irá mostrar uma mensagem se a família está com 
saldo positivo ou negativo, seguido do valor do saldo. 
*/


let family = { 
    incomes: [3999, 3589, 259.43, 360.45], 
    expenses: [320, 128.45, 152.30, 1450.00]
} 

function sum(array){
    let total = 0;
    
    for(let value of array) { 
        total += value 
    }

    return total 


}

function calculateBalance() {
    const calculateIncomes = sum(family.incomes)
    const calculateExpenses = sum(family.expenses)

    const total = calculateIncomes - calculateExpenses  

    const itsOk = total >= 0

    let balanceText = "negativo"

    if (itsOk) {
        balanceText = "positivo"
    }

    console.log(`Seu saldo é ${balanceText}: R$${total.toFixed(2)}`)

}

calculateBalance()


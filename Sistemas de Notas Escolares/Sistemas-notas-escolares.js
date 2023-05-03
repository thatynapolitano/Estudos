/* 

DESAFIO: Crie um algoritmo que transforme as notas do sistema numerico para sistema de notas em caracteres tipo A B C

excelente: de 90 para cima - A
otimo: entre 80 a 89 - B 
bom: entre 70 a 79 - C 
razoavel: entre 60 a 69 - D 
ruim: menor que 60 - F 

*/

let grade = 39


if(grade >= 90 && grade <= 100) {
    console.log('A')
} else if(grade <= 89 && grade >= 80) {
    console.log('B')
} else if(grade <= 79 && grade >= 70) {
    console.log('C')
} else if(grade <= 69 && grade >= 60) {
    console.log('D') 
} else if (grade <= 60 && grade >= 0) {
    console.log('F')
} else {
    console.log('Não existe')
}
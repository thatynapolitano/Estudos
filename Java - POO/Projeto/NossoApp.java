package Projeto;

import Classes.Aluno; // Posso colocar as minhas classes em package diferente aqui então o package será importado
import Classes.Vendedor;

public class NossoApp {
    public static void main(String[] args) {

        Vendedor vendedor01 = new Vendedor();
        vendedor01.nome = "Arthur";
        vendedor01.sortearIdade();
        vendedor01.imprimirNome();

        Vendedor vendedor02 = new Vendedor();
        vendedor02.nome = "Sarah";
        vendedor02.sortearIdade();
        vendedor02.imprimirNome();

        Aluno aluno01 = new Aluno();
        aluno01.nome = "Antonio";
        aluno01.imprimirNome();
        aluno01.matricula = 28723892;
        aluno01.imprimirMatricula();
        aluno01.curso = "Análise e Desenvolvimento de Sistemas";
        aluno01.imprimirCurso();
        aluno01.ativo = false;
        aluno01.imprimirAtivo();
        aluno01.endereco = "Avenida das Américas 3434";
        aluno01.imprimirEndereço(); 
        aluno01.periodo = 1;
        aluno01.imprimirPeriodo();

        Aluno aluno02 = new Aluno();
        aluno02.nome = "Paula";
        aluno02.imprimirNome();
        aluno02.matricula = 38927242;
        aluno02.imprimirMatricula();
        aluno02.curso = "Ciência da Computação"; 
        aluno02.imprimirCurso();
        aluno02.ativo = true; 
        aluno02.imprimirAtivo();  
        aluno02.endereco = "Rua das Pitangas, 648";
        aluno02.imprimirEndereço(); 
        aluno02.periodo = 8;
        aluno02.imprimirPeriodo();
    }
}

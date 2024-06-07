package Projeto;

import java.util.Random;

public class Aluno {
    public String nome;
    public int matricula; 
    public String curso;
    public Boolean ativo; 
    
    public void imprimirNome() {  // Aqui temos a funcao que dentro de uma classe torna-se seu metodo - funcao = comportamento = metodo
        System.out.println("O nome do aluno é " + nome);
    }

    public void imprimirMatricula() {  
        System.out.println("Sua matricula é " + matricula);
    }

    public void imprimirCurso() {
        System.out.println("Seu curso é " + curso);
    }

    public void imprimirAtivo() {
        System.out.println(ativo);
    }


}

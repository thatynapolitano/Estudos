package Classes;

import java.util.Random;

import javax.swing.JOptionPane;

public class Aluno {
    public String nome;
    public int matricula; 
    public String curso;
    public Boolean ativo; 
    public String endereco;
    public int periodo; 

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
        System.out.println("Status da matrícula: " + ativo);
    }

    public void imprimirEndereço() {
        System.out.println("Endereço: " + endereco);
    }   

    public void imprimirPeriodo () {
        System.out.println("Periodo atual: " + periodo);
    } 
}
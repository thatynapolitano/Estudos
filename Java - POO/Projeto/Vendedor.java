package Projeto;

import java.util.Random;

public class Vendedor {
    public String nome;  // Atributo nome  -> Para criacao de um atributo precisa ter a Visibilidade, o tipo do Atributo(atributo=variavel) e o Nome
    public int idade;

    public void imprimirNome() {  // Aqui temos a funcao que dentro de uma classe torna-se seu metodo 
        System.out.println("Meu nome é " + nome + " e tenho " + idade);
    }

    public void sortearIdade() {
        Random sorteador = new Random();
        idade = sorteador.nextInt();
    }

}

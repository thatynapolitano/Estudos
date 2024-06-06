// Java é uma linguagem de programação orientada a objetos desenvolvida na década de 90 por uma equipe de programadores chefiada por James Gosling, na empresa Sun Microsystems, que em 2008 foi adquirido pela empresa Oracle Corporation.


// Primeiro Hello World em Java 
// Toda classe começa com nome Maiusculo (Main)  - uma classe pode ser public (outras classes do sistema podem ter acesso a ela), private (Só quem está dentro da classe consegue acessa-la)


public class Main 
{
	public static void main(String[] args) { // todo nome de metodo começa com letra minuscula.. (main) 
		System.out.println("Hello World!");

        int idade = 29;
        float dinheiro = 16.90f;  // quando é float precisa colocar f no final do numero 
        String nome = "Thatiana";

        System.out.println(idade);
        System.out.println(dinheiro);
        System.out.println(nome);
	}
}
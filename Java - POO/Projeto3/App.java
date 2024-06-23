package Projeto3;

import javax.swing.JOptionPane;

public class App {
    public static void main(String[] args) {
        
        // Declarar variável inteira 
        //int x = 10; 
        // Como criar array e acessar a posição
        // int [] arrayDeInteiros = {15, 8, 9999, -512};

        // System.out.println(arrayDeInteiros[1]);

        Comida x = new Comida();
        x.nome = "Arroz";
        x.regiao = "Brasil";
        x.preco = 7.5f; 

        Comida[] arrayComidas = {new Comida(), new Comida()};
        arrayComidas[0].nome = "Dolly Guaraná";
        arrayComidas[0].regiao = "Brasil";
        arrayComidas[0].preco = 20f;

        arrayComidas[1].nome = "Farofa";
        arrayComidas[1].regiao = "Colômbia";
        arrayComidas[1].preco = 10f; // grama

        String saida = arrayComidas[0].nome + " (" + arrayComidas[0].regiao + ") R$ " + 
        arrayComidas[0].preco;

        JOptionPane.showMessageDialog(null, saida);

        String saida2 = arrayComidas[1].nome + " (" + arrayComidas[1].regiao + ") R$ " + 
        arrayComidas[1].preco;

        JOptionPane.showMessageDialog(null, saida2);

        // Para facilitar a nossa vida, podemos utilizar uma estrutura de repetição para passar pelos elementos do array

        for (int i = 0; i < arrayComidas.length; i ++) {
            String saida3 = arrayComidas[i].nome + " (" + arrayComidas[i].regiao + ") R$ " + 
            arrayComidas[i].preco;
    
            JOptionPane.showMessageDialog(null, saida3);
        }
    }
}

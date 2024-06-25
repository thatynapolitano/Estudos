package Projeto3;

import javax.swing.JOptionPane;

public class App {
    public static void main(String[] args) {
        
        // Declarar variável inteira 
        //int x = 10; 
        // Como criar array e acessar a posição
        // int [] arrayDeInteiros = {15, 8, 9999, -512};

        // System.out.println(arrayDeInteiros[1]);

        // Outra forma de construtor 
        Comida x = new Comida();
        x.nome = "Arroz";
        x.regiao = "Brasil";
        x.preco = 7.5f;  
        
        // Outra forma de construtor 
        Comida[] arrayComidas = {
            new Comida ("Dolly Guaraná", "Brasil", 20f),
            new Comida ("Farofa", "Colombia", 10f)
        };
    
        // Para adicionar informações no construtor 
        arrayComidas[0].nome = "Dolly Guaraná";
        arrayComidas[0].regiao = "Brasil";
        arrayComidas[0].preco = 20f;

        arrayComidas[1].nome = "Farofa";
        arrayComidas[1].regiao = "Colômbia";
        arrayComidas[1].preco = 10f;

        for (int i = 0; i < arrayComidas.length; i++) {
            JOptionPane.showMessageDialog(null, arrayComidas[i].getDados());

            float desconto = Float.parseFloat(JOptionPane.showInputDialog("Digite o valor do desconto"));

            JOptionPane.showMessageDialog(null, arrayComidas[i].getDadosComDesconto(desconto));
        }
    }
}

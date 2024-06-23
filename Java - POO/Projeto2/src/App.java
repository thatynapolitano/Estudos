package Projeto2.src;

import java.text.NumberFormat;
import java.util.Locale;
import javax.swing.JOptionPane;

public class App {
    public static void main(String[] args) {

        Carro meuPrimeiroCarro = new Carro();
        meuPrimeiroCarro.modelo = "Nissan Kicks"; // para pedir para o usuario colocar o valor depois do = colocar: JOptionPane.showInputDialog("Digite o modelo do carro: "); 
        meuPrimeiroCarro.marca = "Nissan"; // JOptionPane.showInputDialog("Digite a marca do carro: ");
        meuPrimeiroCarro.ano = 2018;
        meuPrimeiroCarro.preco = 120.000f; // Float.parseFloat(JOptionPane.showInputDialog("Digite o preço do carro: ")
        String apresentacao01 = meuPrimeiroCarro.modelo + " " + meuPrimeiroCarro.preco;
        
        Carro segundoCarro = new Carro();
        segundoCarro.modelo = "Ecosport";
        segundoCarro.marca = "Fusca";
        segundoCarro.ano = 2012; 
        segundoCarro.preco = 140.000f;
        String apresentacao02 = segundoCarro.modelo + " " + segundoCarro.preco;

        Carro terceiroCarro = new Carro();
        terceiroCarro.modelo = "Fusca";
        terceiroCarro.marca = "Fusca";
        terceiroCarro.ano = 1970;
        terceiroCarro.preco = 90.000f;
        String apresentacao03 = terceiroCarro.modelo + " " + terceiroCarro.preco;

        Carro [] arrayDeCarros = new Carro[3];
        arrayDeCarros[0] = meuPrimeiroCarro;
        arrayDeCarros[1] = segundoCarro;
        arrayDeCarros[2] = terceiroCarro;

        for (int i = 0; i < arrayDeCarros.length; i++) {

            String saida = arrayDeCarros[i].modelo + " R$" + arrayDeCarros[i].preco;

            JOptionPane.showMessageDialog(null, saida);
        }

        // Para formatar o preço do carro para R$ 
        Locale locale = new Locale("pt", "BR"); 
        NumberFormat formatadorDeNumeros = NumberFormat.getCurrencyInstance(locale);
        String precoFormatado = formatadorDeNumeros.format(meuPrimeiroCarro.preco);

        JOptionPane.showMessageDialog(null, precoFormatado); // Só aceita 1 argumento além do null.
        JOptionPane.showMessageDialog(null, apresentacao01);
        JOptionPane.showMessageDialog(null, apresentacao02);
        JOptionPane.showMessageDialog(null, apresentacao03); 
    }
}

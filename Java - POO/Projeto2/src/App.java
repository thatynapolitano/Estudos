package Projeto2.src;

import java.text.NumberFormat;
import java.util.Locale;
import javax.swing.JOptionPane;

import Classes.Vendedor;

public class App {
    public static void main(String[] args) {

        Carro meuPrimeiroCarro = new Carro();
        meuPrimeiroCarro.modelo = "Nissan Kicks";
        meuPrimeiroCarro.marca = "Nissan"; 
        meuPrimeiroCarro.ano = 2018;
        meuPrimeiroCarro.preco = 120.000f;

        
        Carro segundoCarro = new Carro();
        segundoCarro.modelo = "Ecosport";
        segundoCarro.marca = "Fusca";
        segundoCarro.ano = 2012; 

        Carro terceiroCarro = new Carro();
        terceiroCarro.modelo = "Fusca";
        terceiroCarro.marca = "Fusca";
        terceiroCarro.ano = 1970;

        Locale locale = new Locale("pt", "BR"); 
        NumberFormat formatadorDeNumeros = NumberFormat.getCurrencyInstance(locale);
        String precoFormatado = formatadorDeNumeros.format(meuPrimeiroCarro.preco);

        JOptionPane.showMessageDialog(null, precoFormatado); // Só aceita 1 argumento além do null.
    }
}

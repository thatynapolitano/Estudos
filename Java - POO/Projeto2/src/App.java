package Projeto2.src;

import javax.swing.JOptionPane;

import Classes.Vendedor;

public class App {
    public static void main(String[] args) {

        Carro meuPrimeiroCarro = new Carro();
        meuPrimeiroCarro.modelo = "Nissan Kicks";
        meuPrimeiroCarro.marca = "Nissan"; 
        meuPrimeiroCarro.ano = 2018;
        
        Carro segundoCarro = new Carro();
        segundoCarro.modelo = "Ecosport";
        segundoCarro.marca = "Fusca";
        segundoCarro.ano = 2012; 

        Carro terceiroCarro = new Carro();
        terceiroCarro.modelo = "Fusca";
        terceiroCarro.marca = "Fusca";
        terceiroCarro.ano = 1970;

        JOptionPane.showMessageDialog(null, meuPrimeiroCarro.modelo);
    }
}

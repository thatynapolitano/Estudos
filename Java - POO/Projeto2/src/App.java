package Projeto2.src;

import javax.swing.JOptionPane;

import Classes.Vendedor;

public class App {
    public static void main(String[] args) {

        Carro meuPrimeiroCarro = new Carro();
        meuPrimeiroCarro.modelo = "Nissan Kicks";
        meuPrimeiroCarro.marca = "Nissan"; 
        
        Carro segundoCarro = new Carro();
        segundoCarro.modelo = "Ecosport";
        segundoCarro.marca = "Fusca";

        JOptionPane.showMessageDialog(null, meuPrimeiroCarro.modelo);
    }
}

package Projeto4;

import javax.swing.JOptionPane;

public class App {
    public static void main(String[] args) {
        
        Veiculo [] veiculos = new Veiculo [2];
        veiculos[0] = new Veiculo("Corcel", "Ford", 1976, 9000); // Essa linha e a linha debaixo refere-se ao método construtor com parametros e definições de tipo de parametros
        veiculos[1] = new Veiculo("Cerato", "Kia", 2014, 49900);
        veiculos[2].modelo = "Santa Fé"; // A partir dessa linha o registro referece ao método construtor Veiculo() vazio. 
        veiculos[2].fabricante = "Hyundai";
        veiculos[2].ano = 2008;
        veiculos[2].valor = 40000;

        for (int i = 0; i < veiculos.length; i++) {
            JOptionPane.showMessageDialog(null,veiculos[i].getDados());
        } 
    } 
}
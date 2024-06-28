package Projeto4;

import javax.swing.JOptionPane;

public class CarroPasseio extends Veiculo{
    public CarroPasseio(String modelo, String fabricante, int ano, int valor){
        super(modelo, fabricante, ano, valor); // Serve para chegar no construtor da Classe pai Veículo
        setQuantidadedeRodas();
        
    }

    public CarroPasseio() {
        setQuantidadedeRodas();
    }

    public void setQuantidadedeRodas() {
        quantidadedeRodas = 4;
}

} 
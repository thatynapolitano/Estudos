
package Projeto4;


public class Veiculo {
    public String modelo;
    public String fabricante;
    public int ano;
    public int valor;
    public int quantidadedeRodas; 

    public Veiculo(String modelo, String fabricante, int ano, int valor) {
        super(); // Invoca o método construtor da classe pai dessa classe que estamos escrevendo
        this.modelo = modelo;
        this.fabricante = fabricante;
        this.ano = ano;
        this.valor = valor;
    }

    public Veiculo() {
        
    }

    public String getDados() {
        String dados = modelo + ", " + fabricante +
        ", " + ano + ", no valor de " + valor;
        return dados;
    }
}

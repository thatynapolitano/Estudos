package Projeto3;

public class Comida {
    public String nome;
    public String regiao;
    public float preco;

    public float getPrecoComDesconto(float desconto){
        float valorComDesconto = preco * (1 - desconto);
        return valorComDesconto;
    }

    // Com esse método consigo retornar os dados
    public String getDados() {
        return nome + " (" + regiao + ") R$ " + preco; 
    }
    
    public String getDadosComDesconto(float desconto) {
        return nome + " (" + regiao + ") R$ " + getPrecoComDesconto(desconto); 
    }
    
}

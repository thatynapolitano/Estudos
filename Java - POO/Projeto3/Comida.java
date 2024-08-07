package Projeto3;

import java.util.Date;

// receita de variável: visibilidade, tipo, nome 
public class Comida {
    public String nome;
    public String regiao;
    public float preco;
    public Date dataRegistro;

    // receita do construtor: visibilidade, tipo*(parametros)

    public Comida(String nome, String regiao, float preco) { 
        this.nome = nome;    // quando usa o this significa que refere-se ao atributo da classe e não do parametro. Aqui quer dizer que o atributo da classe sero igual do paramtro.
        this.regiao = regiao;
        this.preco = preco;
        dataRegistro = new Date();
    }

    public Comida(){
        
    }

    // receita de método: visibilidade, retorno, nome (parametros)
    public float getPrecoComDesconto(float desconto){
        float valorComDesconto = preco - preco * desconto;
        return valorComDesconto;
    }

    // Com esse método consigo retornar os dados
    public String getDados() {
        return nome + " (" + regiao + ") R$ " + preco +
        "/ registrado em " + dataRegistro; 
    }
    
    public String getDadosComDesconto(float desconto) {
        return nome + " (" + regiao + ") R$ " + getPrecoComDesconto(desconto); 
    }
    
}

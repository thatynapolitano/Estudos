
# Data Warehouse
![alt text](/assets/image-68.png) 

Um data warehouse, ou armazém de dados, é um sistema de armazenamento de dados que reúne e organiza grandes quantidades de dados de diversas fontes. Os dados podem ser estruturados, como tabelas de banco de dados e planilhas do Excel, ou semiestruturados, como páginas da Web e arquivos XML. <p>

Os data warehouses são utilizados para: Gerar relatórios e análises, Tomar decisões de negócios informadas, Monitorar a performance dos negócios, Extrair insights dos dados. 
Os data warehouses podem consolidar dados de várias fontes, como transações em ponto de venda, gestão de relacionamento e automação de marketing. Eles são projetados para oferecer uma visão de longo prazo dos dados, permitindo a análise de mudanças ao longo do tempo. <p>

Algumas vantagens dos data warehouses são:
- Permitir a análise de grandes quantidades de dados
- Criar consistência entre dados de fontes diferentes
- Realizar consultas rapidamente
- Fornecer uma taxa de transferência de dados elevada 

## OLAP

- Termo usado para descrever a análise de dados complexos do Data Warehouse.
- As ferramentas OLAP utilizam computação distribuída para análises que exigem mais armazenamento e poder de processamento do que pode estar localizado um desktop individual.

OLAP é a sigla para Processamento Analítico Online, uma tecnologia que organiza e analisa grandes bancos de dados empresariais: 

<p>O OLAP é usado para suportar business intelligence 
Os bancos de dados OLAP são divididos em cubos, que são organizados para facilitar a recuperação e análise de dados 
O OLAP permite executar consultas analíticas complexas sem prejudicar os sistemas transacionais 

<p>Os bancos de dados OLAP são otimizados para cargas de trabalho com leitura intensa e pouca gravação.

<p>Os gestores podem usar as aplicações OLAP para fazer análises comparativas e facilitar a tomada de decisões.

<p>O DOLAP (OLAP Desktop) é um sistema OLAP que permite transferir os dados de um SQL server para o desktop do usuário. Ele é mais fácil de implantar e tem um custo menor, mas é mais limitado do que outros sistemas. 

## Mineração de Dados 

Mineração de dados é como brincar de encontrar tesouros escondidos em uma caixa cheia de brinquedos. Imagine que você tem uma caixa enorme com muitos brinquedos diferentes, e você quer encontrar só os carrinhos vermelhos. Você começa a procurar e separar os carrinhos que têm a cor que você quer.

Na mineração de dados, a "caixa" é um lugar cheio de informações (como números, textos ou até fotos). E os "carrinhos vermelhos" são as informações mais importantes ou interessantes que as pessoas querem achar. A gente usa computadores e programas para ajudar a encontrar esses "tesouros escondidos" rapidinho, porque às vezes tem muita, muuuita informação para olhar! 🕵️‍♀️✨ 

Na mineração de dados, muitas vezes usamos inteligência artificial (IA) para ajudar a encontrar padrões ou informações importantes. Isso funciona como se a IA fosse um ajudante superinteligente que consegue analisar montes de dados e descobrir coisas que as pessoas, sozinhas, levariam muito tempo para encontrar.

Por exemplo:

Classificação: A IA pode organizar os dados em grupos, como separar frutas em "maçãs" e "bananas".
Previsão: Com base no que aconteceu no passado, a IA pode dizer o que provavelmente vai acontecer no futuro, como prever se vai chover ou fazer sol.
Detecção de padrões: A IA pode descobrir coisas escondidas, como encontrar clientes que compram sempre no mesmo dia do mês.
Os algoritmos de IA, como aprendizado de máquina (machine learning), tornam a mineração de dados mais rápida, precisa e eficiente, ajudando empresas e pesquisadores a tomar decisões melhores.

## Modelagem de Dados para Data Warehouse 

![alt text](/assets/image-69.png) 

## Projeto de Data Warehouse

![alt text](/assets/image-70.png)

- Os Data Warehouses existem para facilitar as consultas complexas. 
- Com o uso intenso de dados frequentes, precisam oferecer suporte à consulta com mais eficiência do que os Bancos de Dados transacionais.
- O componente de acesso ao Data Warehouse tem suporte para:
    - Funcionalidade de planilha avançada; 
    - Processamento de consulta eficiente; 
    - Consultas estruturadas;
    - Consultas ocasionais;
    - Mineração de dados;
    - Visões materializadas. 
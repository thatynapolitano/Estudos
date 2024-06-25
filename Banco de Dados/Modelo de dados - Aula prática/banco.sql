-- Inserindo nova receita 

INSERT INTO UnidadeMedida (id_unidade_medida, nome_medida) VALUES (5, 'Colher');

INSERT INTO ingrediente (id_ingrediente, nome_ingrediente) VALUES (2, 'Vinagre'); 

INSERT INTO passo (id_passo, verbo) VALUES (2, 'Misturar');

INSERT INTO acaoespecifica (id_passo, id_ingrediente, quantidade, id_unidade_medida) VALUES (2, 2, 4, 5);

INSERT INTO prato (id_prato, nome_prato, descricao) VALUES (1, 'Requeijão', 'Requeijão do Mohamed Indi');
INSERT INTO receita (id_receita, id_prato) VALUES (1,1);

SELECT * FROM receita;



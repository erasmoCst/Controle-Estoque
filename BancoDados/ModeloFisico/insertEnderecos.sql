
-- ENDERECOS --
-- São Paulo
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('01200000', 'Rua Augusta', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Paulo'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('03000000', 'Avenida Paulista', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Paulo'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('05400000', 'Rua Oscar Freire', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Paulo'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('04500000', 'Avenida Ibirapuera', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Paulo'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('01000000', 'Rua da Consolação', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Paulo'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('08000000', 'Avenida Morumbi', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Paulo'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('07000000', 'Rua 25 de Março', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Paulo'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('04000000', 'Avenida Faria Lima', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Paulo'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('01100000', 'Rua Bela Cintra', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Paulo'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('02000000', 'Avenida São João', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Paulo'));


-- Rio de Janeiro
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('20000000', 'Rua da Lapa', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio de Janeiro'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('20200000', 'Avenida Copacabana', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio de Janeiro'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('20500000', 'Rua Ipanema', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio de Janeiro'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('20700000', 'Avenida Tijuca', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio de Janeiro'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('21000000', 'Rua Barra da Tijuca', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio de Janeiro'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('21300000', 'Avenida Leblon', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio de Janeiro'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('21500000', 'Rua São Conrado', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio de Janeiro'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('21700000', 'Avenida Recreio dos Bandeirantes', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio de Janeiro'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('22000000', 'Rua Botafogo', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio de Janeiro'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('23000000', 'Avenida Santa Cruz', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio de Janeiro'));


-- Brasília
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('70000000', 'Rua da Esplanada', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Brasília'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('70200000', 'Avenida dos Ministérios', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Brasília'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('70300000', 'Rua da Asa Sul', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Brasília'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('70400000', 'Avenida W3 Sul', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Brasília'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('70500000', 'Rua da Asa Norte', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Brasília'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('70600000', 'Avenida L2 Sul', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Brasília'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('70700000', 'Rua da L4 Sul', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Brasília'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('70800000', 'Avenida L2 Norte', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Brasília'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('70900000', 'Rua da L4 Norte', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Brasília'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('71000000', 'Avenida do Lago', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Brasília'));


-- Salvador
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('40000000', 'Rua da Barra', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Salvador'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('40100000', 'Avenida Ondina', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Salvador'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('40200000', 'Rua do Farol', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Salvador'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('40300000', 'Avenida Barroquinha', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Salvador'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('40400000', 'Rua da Praia', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Salvador'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('40500000', 'Avenida Amaralina', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Salvador'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('40600000', 'Rua Pituba', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Salvador'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('40700000', 'Avenida São Cristóvão', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Salvador'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('40800000', 'Rua Itapuã', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Salvador'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('40900000', 'Avenida Bonfim', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Salvador'));


-- Curitiba
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('80000000', 'Rua 24 Horas', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Curitiba'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('80100000', 'Avenida das Flores', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Curitiba'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('80200000', 'Rua das Araucárias', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Curitiba'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('80300000', 'Avenida Manoel Ribas', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Curitiba'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('80400000', 'Rua Visconde de Guarapuava', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Curitiba'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('80500000', 'Avenida João Gualberto', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Curitiba'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('80600000', 'Rua XV de Novembro', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Curitiba'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('80700000', 'Avenida Cândido de Abreu', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Curitiba'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('80800000', 'Rua Mateus Leme', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Curitiba'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('80900000', 'Avenida Iguaçu', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Curitiba'));


-- Fortaleza
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('60000000', 'Rua Dragão do Mar', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Fortaleza'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('60100000', 'Avenida Beira Mar', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Fortaleza'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('60200000', 'Rua Monsenhor Tabosa', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Fortaleza'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('60300000', 'Avenida LesteOeste', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Fortaleza'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('60400000', 'Rua José Avelino', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Fortaleza'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('60500000', 'Avenida Washington Soares', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Fortaleza'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('60600000', 'Rua Padre Valdevino', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Fortaleza'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('60700000', 'Avenida Oliveira Paiva', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Fortaleza'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('60800000', 'Rua 24 de Maio', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Fortaleza'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('60900000', 'Avenida Godofredo Maciel', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Fortaleza'));


-- Belo Horizonte
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('30000000', 'Rua da Liberdade', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belo Horizonte'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('30100000', 'Avenida do Contorno', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belo Horizonte'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('30200000', 'Rua São Paulo', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belo Horizonte'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('30300000', 'Avenida Amazonas', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belo Horizonte'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('30400000', 'Rua Rio de Janeiro', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belo Horizonte'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('30500000', 'Avenida Afonso Pena', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belo Horizonte'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('30600000', 'Rua Padre Eustáquio', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belo Horizonte'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('30700000', 'Avenida Cristiano Machado', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belo Horizonte'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('30800000', 'Rua Padre Pedro Pinto', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belo Horizonte'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('30900000', 'Avenida Barão Homem de Melo', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belo Horizonte'));


-- Manaus
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69000000', 'Rua do Comércio', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Manaus'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69100000', 'Avenida Eduardo Ribeiro', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Manaus'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69200000', 'Rua dos Andradas', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Manaus'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69300000', 'Avenida Constantino Nery', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Manaus'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69400000', 'Rua Itacoatiara', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Manaus'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69500000', 'Avenida Djalma Batista', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Manaus'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69600000', 'Rua Ferreira Pena', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Manaus'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69700000', 'Avenida Japurá', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Manaus'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69800000', 'Rua Barão de São Domingos', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Manaus'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69900000', 'Avenida Noel Nutels', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Manaus'));


-- Recife
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('50000000', 'Rua da Aurora', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Recife'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('50100000', 'Avenida Boa Viagem', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Recife'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('50200000', 'Rua dos Navegantes', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Recife'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('50300000', 'Avenida Conde da Boa Vista', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Recife'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('50400000', 'Rua da Hora', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Recife'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('50500000', 'Avenida Abdias de Carvalho', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Recife'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('50600000', 'Rua da Soledade', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Recife'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('50700000', 'Avenida Agamenon Magalhães', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Recife'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('50800000', 'Rua do Futuro', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Recife'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('50900000', 'Avenida Rosa e Silva', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Recife'));


-- Porto Alegre
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('90000000', 'Rua da Praia', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Alegre'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('90100000', 'Avenida Beira Rio', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Alegre'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('90200000', 'Rua dos Andradas', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Alegre'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('90300000', 'Avenida Ipiranga', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Alegre'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('90400000', 'Rua Ramiro Barcelos', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Alegre'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('90500000', 'Avenida Cristóvão Colombo', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Alegre'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('90600000', 'Rua Mostardeiro', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Alegre'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('90700000', 'Avenida Plínio Brasil Milano', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Alegre'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('90800000', 'Rua General Lima e Silva', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Alegre'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('90900000', 'Avenida Benjamin Constant', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Alegre'));


-- Belém
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('66000000', 'Avenida Presidente Vargas', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belém'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('66100000', 'Rua dos Mundurucus', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belém'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('66200000', 'Travessa Quintino Bocaiúva', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belém'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('66300000', 'Avenida Nazaré', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belém'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('66400000', 'Rua João Balbi', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belém'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('66500000', 'Avenida Almirante Barroso', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belém'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('66600000', 'Travessa Rui Barbosa', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belém'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('66700000', 'Avenida Pedro Álvares Cabral', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belém'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('66800000', 'Passagem São Benedito', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belém'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('66900000', 'Travessa Mauriti', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Belém'));


-- Boa Vista
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69300000', 'Rua Ajuricaba', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Boa Vista'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69310000', 'Avenida Ville Roy', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Boa Vista'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69320000', 'Rua Bento Brasil', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Boa Vista'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69330000', 'Avenida Capitão Júlio Bezerra', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Boa Vista'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69340000', 'Rua Major Feliciano', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Boa Vista'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69350000', 'Avenida Glaycon de Paiva', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Boa Vista'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69360000', 'Rua Capitão Ene Garcez', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Boa Vista'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69370000', 'Avenida Venezuela', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Boa Vista'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69380000', 'Rua General Penha Brasil', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Boa Vista'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69390000', 'Avenida dos Imigrantes', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Boa Vista'));


-- Campo Grande
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('79000000', 'Rua 14 de Julho', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Campo Grande'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('79100000', 'Avenida Afonso Pena', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Campo Grande'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('79200000', 'Rua dos Estados', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Campo Grande'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('79300000', 'Avenida Mato Grosso', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Campo Grande'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('79400000', 'Rua Ceará', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Campo Grande'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('79500000', 'Avenida Zahran', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Campo Grande'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('79600000', 'Rua Brilhante', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Campo Grande'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('79700000', 'Avenida Gury Marques', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Campo Grande'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('79800000', 'Rua dos Andradas', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Campo Grande'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('79900000', 'Avenida Bandeirantes', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Campo Grande'));


-- Florianópolis
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('88000000', 'Avenida Beira Mar Norte', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Florianópolis'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('88100000', 'Rua Bocaiúva', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Florianópolis'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('88200000', 'Avenida Hercílio Luz', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Florianópolis'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('88300000', 'Rua Felipe Schmidt', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Florianópolis'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('88400000', 'Avenida Mauro Ramos', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Florianópolis'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('88500000', 'Rua Santos Dumont', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Florianópolis'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('88600000', 'Avenida Osmar Cunha', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Florianópolis'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('88700000', 'Rua Altamiro Guimarães', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Florianópolis'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('88800000', 'Avenida Madre Benvenuta', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Florianópolis'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('88900000', 'Rua João Pinto', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Florianópolis'));


-- Goiânia
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('74000000', 'Avenida Anhanguera', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Goiânia'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('74100000', 'Rua 3', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Goiânia'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('74200000', 'Avenida T-9', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Goiânia'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('74300000', 'Rua 4', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Goiânia'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('74400000', 'Avenida 85', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Goiânia'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('74500000', 'Rua 9', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Goiânia'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('74600000', 'Avenida Mutirão', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Goiânia'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('74700000', 'Rua 22', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Goiânia'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('74800000', 'Avenida Independência', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Goiânia'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('74900000', 'Rua 5', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Goiânia'));


-- João Pessoa
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('58000000', 'Avenida Epitácio Pessoa', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'João Pessoa'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('58100000', 'Rua Treze de Maio', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'João Pessoa'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('58200000', 'Avenida Presidente Epitácio Pessoa', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'João Pessoa'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('58300000', 'Rua Visconde de Pelotas', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'João Pessoa'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('58400000', 'Avenida João Machado', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'João Pessoa'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('58500000', 'Rua Miguel Couto', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'João Pessoa'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('58600000', 'Avenida General Osório', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'João Pessoa'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('58700000', 'Rua Duque de Caxias', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'João Pessoa'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('58800000', 'Avenida Almirante Tamandaré', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'João Pessoa'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('58900000', 'Rua Desembargador Souto Maior', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'João Pessoa'));


-- Macapá
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('68900000', 'Avenida FAB', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Macapá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('68901000', 'Travessa 13 de Setembro', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Macapá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('68902000', 'Rua Leopoldo Machado', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Macapá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('68903000', 'Avenida Diógenes Silva', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Macapá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('68904000', 'Rua Eliezer Levy', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Macapá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('68905000', 'Avenida Mendonça Júnior', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Macapá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('68906000', 'Rua Claudomiro de Moraes', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Macapá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('68907000', 'Avenida Padre Júlio Maria Lombaerd', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Macapá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('68908000', 'Rua Adilson José Pinto Pereira', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Macapá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('68909000', 'Avenida Cônego Domingos Maltês', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Macapá'));


-- Maceió
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('57000000', 'Avenida da Paz', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Maceió'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('57100000', 'Rua Silvério Jorge', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Maceió'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('57200000', 'Avenida Governador Lamenha Filho', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Maceió'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('57300000', 'Rua Engenheiro Demócrito Sarmento Barroca', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Maceió'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('57400000', 'Avenida Rotary', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Maceió'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('57500000', 'Rua Hélio Pradines', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Maceió'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('57600000', 'Avenida Muniz Falcão', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Maceió'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('57700000', 'Rua Comendador Palmeira', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Maceió'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('57800000', 'Avenida Desembargador Valente de Lima', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Maceió'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('57900000', 'Rua Engenheiro Otávio Cabral', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Maceió'));


-- Natal
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('59000000', 'Avenida Prudente de Morais', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Natal'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('59100000', 'Rua Seridó', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Natal'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('59200000', 'Avenida Senador Salgado Filho', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Natal'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('59300000', 'Rua Jundiaí', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Natal'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('59400000', 'Avenida Campos Sales', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Natal'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('59500000', 'Rua Apodi', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Natal'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('59600000', 'Avenida Senador Duarte Filho', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Natal'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('59700000', 'Rua Mossoró', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Natal'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('59800000', 'Avenida Miguel Castro', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Natal'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('59900000', 'Rua Mossoró', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Natal'));


-- Porto Velho
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('76800000', 'Avenida Farquar', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Velho'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('76801000', 'Rua Euclides da Cunha', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Velho'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('76802000', 'Avenida Jorge Teixeira', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Velho'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('76803000', 'Rua José Bonifácio', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Velho'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('76804000', 'Avenida 7 de Setembro', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Velho'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('76805000', 'Rua Marechal Deodoro', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Velho'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('76806000', 'Avenida Carlos Gomes', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Velho'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('76807000', 'Rua Rogério Weber', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Velho'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('76808000', 'Avenida Rio Madeira', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Velho'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('76809000', 'Rua Doutor Oswaldo', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Porto Velho'));


-- Rio Branco
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69900000', 'Avenida Brasil', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio Branco'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69901000', 'Travessa Guaporé', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio Branco'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69902000', 'Rua José de Melo', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio Branco'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69903000', 'Avenida Ceará', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio Branco'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69904000', 'Rua Marechal Deodoro', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio Branco'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69905000', 'Avenida Nações Unidas', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio Branco'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69906000', 'Rua Maranhão', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio Branco'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69907000', 'Avenida Getúlio Vargas', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio Branco'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69908000', 'Rua Bahia', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio Branco'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('69909000', 'Avenida Ceará', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Rio Branco'));


-- São Luís
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('65000000', 'Avenida Beira-Mar', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Luís'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('65100000', 'Rua de Santaninha', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Luís'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('65200000', 'Avenida Getúlio Vargas', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Luís'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('65300000', 'Rua do Sol', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Luís'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('65400000', 'Avenida Beira-Rio', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Luís'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('65500000', 'Rua dos Afogados', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Luís'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('65600000', 'Avenida do Farol', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Luís'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('65700000', 'Rua de Santana', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Luís'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('65800000', 'Avenida São Marçal', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Luís'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('65900000', 'Rua dos Afogados', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'São Luís'));


-- Teresina
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('64000000', 'Avenida Frei Serafim', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Teresina'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('64100000', 'Rua Coelho Rodrigues', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Teresina'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('64200000', 'Avenida Miguel Rosa', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Teresina'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('64300000', 'Rua Climatizada', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Teresina'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('64400000', 'Avenida dos Ipês', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Teresina'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('64500000', 'Rua Firmino Filho', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Teresina'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('64600000', 'Avenida Raul Lopes', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Teresina'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('64700000', 'Rua Pedra do Corisco', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Teresina'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('64800000', 'Avenida Dom Severino', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Teresina'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('64900000', 'Rua Desembargador Pires de Castro', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Teresina'));


-- Vitória
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('29000000', 'Avenida Jerônimo Monteiro', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Vitória'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('29100000', 'Rua José Teixeira', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Vitória'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('29200000', 'Avenida Nossa Senhora dos Navegantes', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Vitória'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('29300000', 'Rua João da Cruz', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Vitória'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('29400000', 'Avenida Dante Michelini', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Vitória'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('29500000', 'Rua Desembargador Ferreira Coelho', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Vitória'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('29600000', 'Avenida Adalberto Simão Nader', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Vitória'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('29700000', 'Rua Manoel Gonçalves Carneiro', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Vitória'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('29800000', 'Avenida Dante Michelini', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Vitória'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('29900000', 'Rua Aristóbulo Barbosa Leão', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Vitória'));


-- Cuiabá
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78000000', 'Avenida Isaac Póvoas', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Cuiabá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78100000', 'Rua Barão de Melgaço', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Cuiabá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78200000', 'Avenida Historiador Rubens de Mendonça', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Cuiabá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78300000', 'Rua dos Parecis', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Cuiabá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78400000', 'Avenida Fernando Corrêa da Costa', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Cuiabá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78500000', 'Rua Barão de Melgaço', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Cuiabá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78600000', 'Avenida das Torres', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Cuiabá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78700000', 'Rua Comandante Costa', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Cuiabá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78800000', 'Avenida Tenente Coronel Duarte', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Cuiabá'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78900000', 'Rua General Valadão', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Cuiabá'));


-- Aracaju
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78930000', 'Avenida Beira Mar', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Aracaju'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78931000', 'Rua Vila Cristina', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Aracaju'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78932000', 'Avenida Barão de Maruim', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Aracaju'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78933000', 'Rua Pacatuba', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Aracaju'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78934000', 'Avenida Desembargador Maynard', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Aracaju'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78935000', 'Rua José do Prado Franco', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Aracaju'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78936000', 'Avenida Augusto Franco', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Aracaju'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78937000', 'Rua Vila Cristina', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Aracaju'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78938000', 'Avenida Beira Mar', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Aracaju'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78939000', 'Rua Itabaianinha', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Aracaju'));


-- Palmas
INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78970000', 'Avenida Teotônio Segurado', '123', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Palmas'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78971000', 'Quadra 301 Norte', '456', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Palmas'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78972000', 'Quadra 401 Sul', '789', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Palmas'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78973000', 'Quadra 605 Sul', '555', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Palmas'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78974000', 'Quadra 306 Sul', '321', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Palmas'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78975000', 'Quadra 309 Sul', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Palmas'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78976000', 'Quadra 1106 Sul', '111', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Palmas'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78977000', 'Quadra 606 Sul', '222', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Palmas'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78978000', 'Quadra 1003 Sul', '777', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Palmas'));

INSERT INTO CTL_ESTOQUE.endereco (nr_cep, nm_logradouro, nr_logradouro, cd_municipio)
VALUES ('78979000', 'Quadra 906 Sul', '888', (SELECT cd_municipio FROM CTL_ESTOQUE.municipio WHERE nm_municipio = 'Palmas'));

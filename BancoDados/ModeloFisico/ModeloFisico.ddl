-- Gerado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   em:        2024-03-16 15:50:56 BRT
--   site:      Oracle Database 21c
--   tipo:      Oracle Database 21c



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE cliente (
    cd_cliente    NUMBER(7) NOT NULL,
    nr_cpf        CHAR(11 CHAR) NOT NULL,
    dt_nascimento DATE,
    tp_genero     CHAR(1) NOT NULL
);

CREATE UNIQUE INDEX cliente_cd_idx ON
    cliente (
        cd_cliente
    ASC );

CREATE UNIQUE INDEX cliente_cpf_idx ON
    cliente (
        nr_cpf
    ASC );

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( cd_cliente );

ALTER TABLE cliente ADD CONSTRAINT cliente_cpf_un UNIQUE ( nr_cpf );

CREATE TABLE endereco (
    cd_endereco    NUMBER(7) NOT NULL,
    nr_cep         CHAR(8 CHAR) NOT NULL,
    nm_logradouro  VARCHAR2(50 CHAR) NOT NULL,
    nr_logradouro  VARCHAR2(5 CHAR) NOT NULL,
    cd_municipio   SMALLINT NOT NULL,
    nm_bairro      VARCHAR2(25 CHAR) NOT NULL,
    ds_complemento VARCHAR2(100 CHAR)
);

CREATE UNIQUE INDEX endereco_cd_idx ON
    endereco (
        cd_endereco
    ASC );

ALTER TABLE endereco ADD CONSTRAINT endereco_pk PRIMARY KEY ( cd_endereco );

CREATE TABLE estoque (
    cd_estoque    SMALLINT NOT NULL,
    nr_rua        SMALLINT NOT NULL,
    nr_prateleira SMALLINT NOT NULL,
    nr_sequencia  CHAR(1 CHAR) NOT NULL
);

CREATE UNIQUE INDEX estoque_cd_idx ON
    estoque (
        cd_estoque
    ASC );

ALTER TABLE estoque ADD CONSTRAINT estoque_pk PRIMARY KEY ( cd_estoque );

CREATE TABLE fornecedor (
    cd_fornecedor  NUMBER(7) NOT NULL,
    nr_cnpj        CHAR(14 CHAR) NOT NULL,
    nm_razaosocial VARCHAR2(100 CHAR) NOT NULL
);

CREATE UNIQUE INDEX fornecedor_cd_idx ON
    fornecedor (
        cd_fornecedor
    ASC );

CREATE UNIQUE INDEX fornecedor_cnpj_idx ON
    fornecedor (
        nr_cnpj
    ASC );

ALTER TABLE fornecedor ADD CONSTRAINT fornecedor_pk PRIMARY KEY ( cd_fornecedor );

ALTER TABLE fornecedor ADD CONSTRAINT fornecedor_cnpj_un UNIQUE ( nr_cnpj );

ALTER TABLE fornecedor ADD CONSTRAINT fornecedor_razsoc_un UNIQUE ( nm_razaosocial );

CREATE TABLE municipio (
    cd_municipio SMALLINT NOT NULL,
    nm_municipio VARCHAR2(50) NOT NULL,
    nm_estado    VARCHAR2(50 CHAR) NOT NULL,
    nm_pais      VARCHAR2(50 CHAR) NOT NULL
);

CREATE UNIQUE INDEX municipio_cd_idx ON
    municipio (
        cd_municipio
    ASC );

ALTER TABLE municipio ADD CONSTRAINT municipio_pk PRIMARY KEY ( cd_municipio );

CREATE TABLE pedido (
    cd_pedido  NUMBER(7) NOT NULL,
    cd_pessoa  NUMBER(7) NOT NULL,
    tp_pedido  CHAR(1 CHAR) NOT NULL,
    dt_pedido  DATE DEFAULT sysdate NOT NULL,
    dt_entrega DATE
);

CREATE UNIQUE INDEX pedido_cd_idx ON
    pedido (
        cd_pedido
    ASC );

ALTER TABLE pedido ADD CONSTRAINT pedido_pk PRIMARY KEY ( cd_pedido );

CREATE TABLE pessoa (
    cd_pessoa   NUMBER(7) NOT NULL,
    nm_pessoa   VARCHAR2(50 CHAR) NOT NULL,
    cd_endereco NUMBER(7) NOT NULL,
    nr_telefone VARCHAR2(15 CHAR) NOT NULL,
    nm_email    VARCHAR2(50 CHAR) NOT NULL
);

CREATE UNIQUE INDEX pessoa_cd_idx ON
    pessoa (
        cd_pessoa
    ASC );

ALTER TABLE pessoa ADD CONSTRAINT pessoa_pk PRIMARY KEY ( cd_pessoa );

CREATE TABLE produto (
    cd_produto          SMALLINT NOT NULL,
    nm_produto          VARCHAR2(50 CHAR) NOT NULL,
    ds_produto          VARCHAR2(500 CHAR),
    tp_embalagemproduto CHAR(1 CHAR) NOT NULL
);

CREATE UNIQUE INDEX produto_cd_idx ON
    produto (
        cd_produto
    ASC );

ALTER TABLE produto ADD CONSTRAINT produto_pk PRIMARY KEY ( cd_produto );

CREATE TABLE produto_estoque (
    cd_produto        SMALLINT NOT NULL,
    cd_estoque        SMALLINT NOT NULL,
    nr_lote           VARCHAR2(10 CHAR) NOT NULL,
    qt_produtoestoque NUMBER(7, 2) NOT NULL,
    dt_validade       DATE NOT NULL,
    dt_produtoestoque DATE NOT NULL
);

ALTER TABLE produto_estoque ADD CONSTRAINT produto_estoque_pk PRIMARY KEY ( cd_estoque,
                                                                            cd_produto );

CREATE TABLE produto_fonecedor (
    cd_produto    SMALLINT NOT NULL,
    cd_fornecedor NUMBER(7) NOT NULL,
    vl_produto    NUMBER(7, 2)
);

ALTER TABLE produto_fonecedor ADD CONSTRAINT produto_fonecedor_pk PRIMARY KEY ( cd_fornecedor,
                                                                                cd_produto );

CREATE TABLE produto_pedido (
    cd_pedido  NUMBER(7) NOT NULL,
    cd_produto SMALLINT NOT NULL,
    qt_produto NUMBER(7, 2) NOT NULL
);

ALTER TABLE produto_pedido ADD CONSTRAINT produto_pedido_pk PRIMARY KEY ( cd_pedido );

CREATE TABLE transacao (
    cd_transacao NUMBER(7) NOT NULL,
    cd_estoque   SMALLINT NOT NULL,
    cd_produto   SMALLINT NOT NULL,
    cd_pedido    NUMBER(7) NOT NULL,
    tp_transacao CHAR(1 CHAR) NOT NULL,
    qt_produto   NUMBER(7, 2) NOT NULL,
    dt_transacao DATE DEFAULT sysdate NOT NULL
);

ALTER TABLE transacao ADD CONSTRAINT transacao_pk PRIMARY KEY ( cd_transacao );

ALTER TABLE cliente
    ADD CONSTRAINT cliente_pessoa_fk FOREIGN KEY ( cd_cliente )
        REFERENCES pessoa ( cd_pessoa );

ALTER TABLE endereco
    ADD CONSTRAINT endereco_municipio_fk FOREIGN KEY ( cd_municipio )
        REFERENCES municipio ( cd_municipio );

ALTER TABLE fornecedor
    ADD CONSTRAINT fornecedor_pessoa_fk FOREIGN KEY ( cd_fornecedor )
        REFERENCES pessoa ( cd_pessoa );

ALTER TABLE pedido
    ADD CONSTRAINT pedido_pessoa_fk FOREIGN KEY ( cd_pessoa )
        REFERENCES pessoa ( cd_pessoa );

ALTER TABLE pessoa
    ADD CONSTRAINT pessoa_endereco_fk FOREIGN KEY ( cd_endereco )
        REFERENCES endereco ( cd_endereco );

ALTER TABLE produto_fonecedor
    ADD CONSTRAINT prod_forn_forn_fk FOREIGN KEY ( cd_fornecedor )
        REFERENCES fornecedor ( cd_fornecedor );

ALTER TABLE produto_fonecedor
    ADD CONSTRAINT prod_forn_prod_fk FOREIGN KEY ( cd_produto )
        REFERENCES produto ( cd_produto );

ALTER TABLE produto_estoque
    ADD CONSTRAINT produto_estoque_estoque_fk FOREIGN KEY ( cd_estoque )
        REFERENCES estoque ( cd_estoque );

ALTER TABLE produto_estoque
    ADD CONSTRAINT produto_estoque_produto_fk FOREIGN KEY ( cd_produto )
        REFERENCES produto ( cd_produto );

ALTER TABLE produto_pedido
    ADD CONSTRAINT produto_pedido_pedido_fk FOREIGN KEY ( cd_pedido )
        REFERENCES pedido ( cd_pedido );

ALTER TABLE produto_pedido
    ADD CONSTRAINT produto_pedido_produto_fk FOREIGN KEY ( cd_produto )
        REFERENCES produto ( cd_produto );

ALTER TABLE transacao
    ADD CONSTRAINT transacao_pedido_fk FOREIGN KEY ( cd_pedido )
        REFERENCES pedido ( cd_pedido );

ALTER TABLE transacao
    ADD CONSTRAINT transacao_produto_estoque_fk FOREIGN KEY ( cd_estoque,
                                                              cd_produto )
        REFERENCES produto_estoque ( cd_estoque,
                                     cd_produto );

CREATE SEQUENCE cliente_cd_cliente_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER cliente_cd_cliente_trg BEFORE
    INSERT ON cliente
    FOR EACH ROW
    WHEN ( new.cd_cliente IS NULL )
BEGIN
    :new.cd_cliente := cliente_cd_cliente_seq.nextval;
END;
/

CREATE SEQUENCE endereco_cd_endereco_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER endereco_cd_endereco_trg BEFORE
    INSERT ON endereco
    FOR EACH ROW
    WHEN ( new.cd_endereco IS NULL )
BEGIN
    :new.cd_endereco := endereco_cd_endereco_seq.nextval;
END;
/

CREATE SEQUENCE estoque_cd_estoque_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER estoque_cd_estoque_trg BEFORE
    INSERT ON estoque
    FOR EACH ROW
    WHEN ( new.cd_estoque IS NULL )
BEGIN
    :new.cd_estoque := estoque_cd_estoque_seq.nextval;
END;
/

CREATE SEQUENCE fornecedor_cd_fornecedor_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER fornecedor_cd_fornecedor_trg BEFORE
    INSERT ON fornecedor
    FOR EACH ROW
    WHEN ( new.cd_fornecedor IS NULL )
BEGIN
    :new.cd_fornecedor := fornecedor_cd_fornecedor_seq.nextval;
END;
/

CREATE SEQUENCE municipio_cd_municipio_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER municipio_cd_municipio_trg BEFORE
    INSERT ON municipio
    FOR EACH ROW
    WHEN ( new.cd_municipio IS NULL )
BEGIN
    :new.cd_municipio := municipio_cd_municipio_seq.nextval;
END;
/

CREATE SEQUENCE pedido_cd_pedido_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER pedido_cd_pedido_trg BEFORE
    INSERT ON pedido
    FOR EACH ROW
    WHEN ( new.cd_pedido IS NULL )
BEGIN
    :new.cd_pedido := pedido_cd_pedido_seq.nextval;
END;
/

CREATE SEQUENCE pessoa_cd_pessoa_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER pessoa_cd_pessoa_trg BEFORE
    INSERT ON pessoa
    FOR EACH ROW
    WHEN ( new.cd_pessoa IS NULL )
BEGIN
    :new.cd_pessoa := pessoa_cd_pessoa_seq.nextval;
END;
/

CREATE SEQUENCE produto_cd_produto_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER produto_cd_produto_trg BEFORE
    INSERT ON produto
    FOR EACH ROW
    WHEN ( new.cd_produto IS NULL )
BEGIN
    :new.cd_produto := produto_cd_produto_seq.nextval;
END;
/

CREATE SEQUENCE transacao_cd_transacao_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER transacao_cd_transacao_trg BEFORE
    INSERT ON transacao
    FOR EACH ROW
    WHEN ( new.cd_transacao IS NULL )
BEGIN
    :new.cd_transacao := transacao_cd_transacao_seq.nextval;
END;
/



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            12
-- CREATE INDEX                            10
-- ALTER TABLE                             28
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           9
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          9
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0


CREATE TABLE CTL_ESTOQUE.endereco (
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

ALTER TABLE CTL_ESTOQUE.endereco ADD CONSTRAINT endereco_pk PRIMARY KEY ( cd_endereco );

CREATE TABLE CTL_ESTOQUE.estoque (
    cd_estoque    SMALLINT NOT NULL,
    nr_rua        SMALLINT NOT NULL,
    nr_prateleira SMALLINT NOT NULL,
    nr_sequencia  CHAR(1 CHAR) NOT NULL
);

CREATE UNIQUE INDEX estoque_cd_idx ON
    estoque (
        cd_estoque
    ASC );

ALTER TABLE CTL_ESTOQUE.estoque ADD CONSTRAINT estoque_pk PRIMARY KEY ( cd_estoque );

CREATE TABLE CTL_ESTOQUE.municipio (
    cd_municipio SMALLINT NOT NULL,
    nm_municipio VARCHAR2(50) NOT NULL,
    nm_estado    VARCHAR2(50 CHAR) NOT NULL,
    nm_pais      VARCHAR2(50 CHAR) NOT NULL
);

CREATE UNIQUE INDEX municipio_cd_idx ON
    municipio (
        cd_municipio
    ASC );

ALTER TABLE CTL_ESTOQUE.municipio ADD CONSTRAINT municipio_pk PRIMARY KEY ( cd_municipio );

CREATE TABLE CTL_ESTOQUE.pedido (
    cd_pedido  		   NUMBER(7) NOT NULL,
    cd_pessoa 		   NUMBER(7) NOT NULL,
    dt_pedido  		   DATE DEFAULT sysdate NOT NULL,
    dt_entregaprevista DATE
);

CREATE UNIQUE INDEX pedido_cd_idx ON
    CTL_ESTOQUE.pedido  (
        cd_pedido
    ASC );

ALTER TABLE CTL_ESTOQUE.pedido ADD CONSTRAINT pedido_pk PRIMARY KEY ( cd_pedido );

CREATE TABLE CTL_ESTOQUE.pessoa (
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

ALTER TABLE CTL_ESTOQUE.pessoa ADD CONSTRAINT pessoa_pk PRIMARY KEY ( cd_pessoa );

CREATE TABLE CTL_ESTOQUE.pessoa_fisica (
    cd_pessoa     NUMBER(7) NOT NULL,
    nr_cpf        CHAR(11 CHAR) NOT NULL,
    dt_nascimento DATE NOT NULL,
    tp_genero     CHAR(1) NOT NULL
);

CREATE UNIQUE INDEX cliente_cd_idx ON
    CTL_ESTOQUE.pessoa_fisica (
        cd_pessoa
    ASC );

CREATE UNIQUE INDEX cliente_cpf_idx ON
    CTL_ESTOQUE.pessoa_fisica (
        nr_cpf
    ASC );

ALTER TABLE CTL_ESTOQUE.pessoa_fisica ADD CONSTRAINT cliente_pk PRIMARY KEY ( cd_pessoa );

ALTER TABLE CTL_ESTOQUE.pessoa_fisica ADD CONSTRAINT cliente_cpf_un UNIQUE ( nr_cpf );

CREATE TABLE CTL_ESTOQUE.pessoa_juridica (
    cd_pessoa      NUMBER(7) NOT NULL,
    nr_cnpj        CHAR(14 CHAR) NOT NULL,
    nm_razaosocial VARCHAR2(100 CHAR) NOT NULL
);

CREATE UNIQUE INDEX fornecedor_cd_idx ON
    CTL_ESTOQUE.pessoa_juridica (
        cd_pessoa
    ASC );

CREATE UNIQUE INDEX fornecedor_cnpj_idx ON
    CTL_ESTOQUE.pessoa_juridica (
        nr_cnpj
    ASC );

ALTER TABLE CTL_ESTOQUE.pessoa_juridica ADD CONSTRAINT fornecedor_pk PRIMARY KEY ( cd_pessoa );

ALTER TABLE CTL_ESTOQUE.pessoa_juridica ADD CONSTRAINT fornecedor_cnpj_un UNIQUE ( nr_cnpj );

ALTER TABLE CTL_ESTOQUE.pessoa_juridica ADD CONSTRAINT fornecedor_razsoc_un UNIQUE ( nm_razaosocial );

CREATE TABLE CTL_ESTOQUE.produto (
    cd_produto          SMALLINT NOT NULL,
    nm_produto          VARCHAR2(50 CHAR) NOT NULL,
    ds_produto          VARCHAR2(500 CHAR),
    tp_embalagemproduto CHAR(1 CHAR) NOT NULL,
    vl_produto          NUMBER(7, 2) NOT NULL
);

CREATE UNIQUE INDEX produto_cd_idx ON
    produto (
        cd_produto
    ASC );

ALTER TABLE CTL_ESTOQUE.produto ADD CONSTRAINT produto_pk PRIMARY KEY ( cd_produto );

CREATE TABLE CTL_ESTOQUE.produto_estoque (
    cd_produto        SMALLINT NOT NULL,
    cd_estoque        SMALLINT NOT NULL,
    nr_lote           VARCHAR2(10 CHAR) NOT NULL,
    qt_produtoestoque NUMBER(7, 2) NOT NULL,
    dt_validade       DATE NOT NULL,
    dt_produtoestoque DATE NOT NULL
);

ALTER TABLE CTL_ESTOQUE.produto_estoque ADD CONSTRAINT produto_estoque_pk PRIMARY KEY ( cd_estoque, cd_produto );

CREATE TABLE CTL_ESTOQUE.produto_pedido (
    cd_pedido       NUMBER(7) NOT NULL,
    cd_produto      SMALLINT NOT NULL,
    qt_produto      NUMBER(7, 2) NOT NULL
);

ALTER TABLE CTL_ESTOQUE.produto_pedido ADD CONSTRAINT produto_pedido_pk PRIMARY KEY ( cd_pedido, cd_produto );

ALTER TABLE CTL_ESTOQUE.pessoa_fisica
    ADD CONSTRAINT cliente_pessoa_fk FOREIGN KEY ( cd_pessoa )
        REFERENCES CTL_ESTOQUE.pessoa ( cd_pessoa );

ALTER TABLE CTL_ESTOQUE.endereco
    ADD CONSTRAINT endereco_municipio_fk FOREIGN KEY ( cd_municipio )
        REFERENCES CTL_ESTOQUE.municipio ( cd_municipio );

ALTER TABLE CTL_ESTOQUE.pessoa_juridica
    ADD CONSTRAINT fornecedor_pessoa_fk FOREIGN KEY ( cd_pessoa )
        REFERENCES CTL_ESTOQUE.pessoa ( cd_pessoa );

ALTER TABLE CTL_ESTOQUE.pedido
    ADD CONSTRAINT pedido_pessoa_fk FOREIGN KEY ( cd_pessoa )
        REFERENCES CTL_ESTOQUE.pessoa ( cd_pessoa );

ALTER TABLE CTL_ESTOQUE.pessoa
    ADD CONSTRAINT pessoa_endereco_fk FOREIGN KEY ( cd_endereco )
        REFERENCES CTL_ESTOQUE.endereco ( cd_endereco );

ALTER TABLE CTL_ESTOQUE.produto_estoque
    ADD CONSTRAINT produto_estoque_estoque_fk FOREIGN KEY ( cd_estoque )
        REFERENCES CTL_ESTOQUE.estoque ( cd_estoque );

ALTER TABLE CTL_ESTOQUE.produto_estoque
    ADD CONSTRAINT produto_estoque_produto_fk FOREIGN KEY ( cd_produto )
        REFERENCES CTL_ESTOQUE.produto ( cd_produto );

ALTER TABLE CTL_ESTOQUE.produto_pedido
    ADD CONSTRAINT produto_pedido_pedido_fk FOREIGN KEY ( cd_pedido )
        REFERENCES CTL_ESTOQUE.pedido ( cd_pedido );

ALTER TABLE CTL_ESTOQUE.produto_pedido
    ADD CONSTRAINT produto_pedido_produto_fk FOREIGN KEY ( cd_produto )
        REFERENCES CTL_ESTOQUE.produto ( cd_produto );


DROP SEQUENCE CTL_ESTOQUE.sq_cd_endereco;
CREATE SEQUENCE CTL_ESTOQUE.sq_cd_endereco START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_endereco BEFORE
    INSERT ON CTL_ESTOQUE.endereco
    FOR EACH ROW
    WHEN ( new.cd_endereco IS NULL )
BEGIN
    :new.cd_endereco := CTL_ESTOQUE.sq_cd_endereco.nextval;
END;
/

CREATE SEQUENCE CTL_ESTOQUE.sq_cd_estoque START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_estoque BEFORE
    INSERT ON CTL_ESTOQUE.estoque
    FOR EACH ROW
    WHEN ( new.cd_estoque IS NULL )
BEGIN
    :new.cd_estoque := CTL_ESTOQUE.sq_cd_estoque.nextval;
END;
/

CREATE SEQUENCE CTL_ESTOQUE.sq_cd_municipio START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_municipio BEFORE
    INSERT ON CTL_ESTOQUE.municipio
    FOR EACH ROW
    WHEN ( new.cd_municipio IS NULL )
BEGIN
    :new.cd_municipio := CTL_ESTOQUE.sq_cd_municipio.nextval;
END;
/

CREATE SEQUENCE CTL_ESTOQUE.sq_cd_pedido START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_pedido BEFORE
    INSERT ON CTL_ESTOQUE.pedido
    FOR EACH ROW
    WHEN ( new.cd_pedido IS NULL )
BEGIN
    :new.cd_pedido := CTL_ESTOQUE.sq_cd_pedido.nextval;
END;
/

CREATE SEQUENCE CTL_ESTOQUE.sq_cd_pessoa START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_pessoa BEFORE
    INSERT ON CTL_ESTOQUE.pessoa
    FOR EACH ROW
    WHEN ( new.cd_pessoa IS NULL )
BEGIN
    :new.cd_pessoa := CTL_ESTOQUE.sq_cd_pessoa.nextval;
END;
/
--
CREATE SEQUENCE CTL_ESTOQUE.sq_cd_pessoa_fisica START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_pessoa_fisica BEFORE
    INSERT ON CTL_ESTOQUE.pessoa_fisica
    FOR EACH ROW
    WHEN ( new.cd_pessoa IS NULL )
BEGIN
    :new.cd_pessoa := CTL_ESTOQUE.sq_cd_pessoa_fisica.nextval;
END;
/

CREATE SEQUENCE CTL_ESTOQUE.sq_cd_pessoa_juridica START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_pessoa_juridica BEFORE
    INSERT ON CTL_ESTOQUE.pessoa_juridica
    FOR EACH ROW
    WHEN ( new.cd_pessoa IS NULL )
BEGIN
    :new.cd_pessoa := CTL_ESTOQUE.sq_cd_pessoa_juridica.nextval;
END;
/

CREATE SEQUENCE CTL_ESTOQUE.sq_cd_produto START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER CTL_ESTOQUE.trg_cd_produto BEFORE
	INSERT ON CTL_ESTOQUE.produto
	FOR EACH ROW
	WHEN ( new.cd_produto IS NULL )
BEGIN
	:new.cd_produto := CTL_ESTOQUE.sq_cd_produto.nextval;
END;
/
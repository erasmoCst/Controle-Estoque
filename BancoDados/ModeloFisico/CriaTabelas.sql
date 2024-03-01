CREATE TABLE CTL_ESTOQUE.cliente (
    cd_cliente    NUMBER(7) NOT NULL,
    nr_cpf        CHAR(11 CHAR) NOT NULL,
    dt_nascimento DATE,
    tp_genero     CHAR(1) NOT NULL
);

CREATE UNIQUE INDEX CTL_ESTOQUE.cliente_cd_idx ON
    CTL_ESTOQUE.cliente (
        cd_cliente
    ASC );

CREATE UNIQUE INDEX CTL_ESTOQUE.cliente_cpf_idx ON
    CTL_ESTOQUE.cliente (
        nr_cpf
    ASC );

ALTER TABLE CTL_ESTOQUE.cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( cd_cliente );

ALTER TABLE CTL_ESTOQUE.cliente ADD CONSTRAINT cliente_cpf_un UNIQUE ( nr_cpf );

CREATE TABLE CTL_ESTOQUE.endereco (
    cd_endereco   NUMBER(7) NOT NULL,
    nr_cep        CHAR(8 CHAR) NOT NULL,
    nm_logradouro VARCHAR2(50 CHAR) NOT NULL,
    nr_logradouro VARCHAR2(5 CHAR) NOT NULL,
    cd_municipio  SMALLINT NOT NULL
);

CREATE UNIQUE INDEX CTL_ESTOQUE.endereco_cd_idx ON
    CTL_ESTOQUE.endereco (
        cd_endereco
    ASC );

ALTER TABLE CTL_ESTOQUE.endereco ADD CONSTRAINT endereco_pk PRIMARY KEY ( cd_endereco );

CREATE TABLE CTL_ESTOQUE.estoque (
    cd_estoque    SMALLINT NOT NULL,
    nr_rua        SMALLINT NOT NULL,
    nr_prateleita SMALLINT NOT NULL,
    nr_sequencia  CHAR(1 CHAR) NOT NULL
);

CREATE UNIQUE INDEX CTL_ESTOQUE.estoque_cd_idx ON
    CTL_ESTOQUE.estoque (
        cd_estoque
    ASC );

ALTER TABLE CTL_ESTOQUE.estoque ADD CONSTRAINT estoque_pk PRIMARY KEY ( cd_estoque );

CREATE TABLE CTL_ESTOQUE.fornecedor (
    cd_fornecedor  NUMBER(7) NOT NULL,
    nr_cnpj        CHAR(14 CHAR) NOT NULL,
    nm_razaosocial VARCHAR2(100 CHAR) NOT NULL
);

CREATE UNIQUE INDEX CTL_ESTOQUE.fornecedor_cd_idx ON
    CTL_ESTOQUE.fornecedor (
        cd_fornecedor
    ASC );

CREATE UNIQUE INDEX CTL_ESTOQUE.fornecedor_cnpj_idx ON
    CTL_ESTOQUE.fornecedor (
        nr_cnpj
    ASC );

ALTER TABLE CTL_ESTOQUE.fornecedor ADD CONSTRAINT fornecedor_pk PRIMARY KEY ( cd_fornecedor );

ALTER TABLE CTL_ESTOQUE.fornecedor ADD CONSTRAINT fornecedor_cnpj_un UNIQUE ( nr_cnpj );

ALTER TABLE CTL_ESTOQUE.fornecedor ADD CONSTRAINT fornecedor_razsoc_un UNIQUE ( nm_razaosocial );

CREATE TABLE CTL_ESTOQUE.municipio (
    cd_municipio SMALLINT NOT NULL,
    nm_municipio VARCHAR2(50) NOT NULL,
    nm_estado    VARCHAR2(50 CHAR) NOT NULL,
    nm_pais      VARCHAR2(50 CHAR) NOT NULL
);

CREATE UNIQUE INDEX CTL_ESTOQUE.municipio_cd_idx ON
    CTL_ESTOQUE.municipio (
        cd_municipio
    ASC );

ALTER TABLE CTL_ESTOQUE.municipio ADD CONSTRAINT municipio_pk PRIMARY KEY ( cd_municipio );

CREATE TABLE CTL_ESTOQUE.pedido (
    cd_pedido  NUMBER(7) NOT NULL,
    cd_pessoa  NUMBER(7) NOT NULL,
    tp_pedido  CHAR(1 CHAR) NOT NULL,
    dt_pedido  DATE DEFAULT sysdate NOT NULL,
    dt_entrega DATE
);

CREATE UNIQUE INDEX CTL_ESTOQUE.pedido_cd_idx ON
    CTL_ESTOQUE.pedido (
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

CREATE UNIQUE INDEX CTL_ESTOQUE.pessoa_cd_idx ON
   CTL_ESTOQUE.pessoa (
        cd_pessoa
    ASC );

ALTER TABLE CTL_ESTOQUE.pessoa ADD CONSTRAINT pessoa_pk PRIMARY KEY ( cd_pessoa );

CREATE TABLE CTL_ESTOQUE.produto (
    cd_produto          SMALLINT NOT NULL,
    nm_produto          VARCHAR2(50 CHAR) NOT NULL,
    ds_produto          VARCHAR2(500 CHAR),
    tp_embalagemproduto CHAR(1 CHAR) NOT NULL
);

CREATE UNIQUE INDEX CTL_ESTOQUE.produto_cd_idx ON
    CTL_ESTOQUE.produto (
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

ALTER TABLE CTL_ESTOQUE.produto_estoque ADD CONSTRAINT produto_estoque_pk PRIMARY KEY ( cd_estoque,
                                                                            cd_produto );

CREATE TABLE CTL_ESTOQUE.produto_fonecedor (
    cd_produto    SMALLINT NOT NULL,
    cd_fornecedor NUMBER(7) NOT NULL,
    vl_produto    NUMBER(7, 2)
);

ALTER TABLE CTL_ESTOQUE.produto_fonecedor ADD CONSTRAINT produto_fonecedor_pk PRIMARY KEY ( cd_fornecedor,
                                                                                cd_produto );

CREATE TABLE CTL_ESTOQUE.produto_pedido (
    cd_pedido  NUMBER(7) NOT NULL,
    cd_produto SMALLINT NOT NULL,
    qt_produto NUMBER(7, 2) NOT NULL
);

ALTER TABLE CTL_ESTOQUE.produto_pedido ADD CONSTRAINT produto_pedido_pk PRIMARY KEY ( cd_pedido );

CREATE TABLE CTL_ESTOQUE.transacao (
    cd_transacao NUMBER(7) NOT NULL,
    cd_estoque   SMALLINT NOT NULL,
    cd_produto   SMALLINT NOT NULL,
    cd_pedido    NUMBER(7) NOT NULL,
    tp_transacao CHAR(1 CHAR) NOT NULL,
    qt_produto   NUMBER(7, 2) NOT NULL,
    dt_transacao DATE DEFAULT sysdate NOT NULL
);

ALTER TABLE CTL_ESTOQUE.transacao ADD CONSTRAINT transacao_pk PRIMARY KEY ( cd_transacao );

ALTER TABLE CTL_ESTOQUE.cliente
    ADD CONSTRAINT cliente_pessoa_fk FOREIGN KEY ( cd_cliente )
        REFERENCES CTL_ESTOQUE.pessoa ( cd_pessoa );

ALTER TABLE CTL_ESTOQUE.endereco
    ADD CONSTRAINT endereco_municipio_fk FOREIGN KEY ( cd_municipio )
        REFERENCES CTL_ESTOQUE.municipio ( cd_municipio );

ALTER TABLE CTL_ESTOQUE.fornecedor
    ADD CONSTRAINT fornecedor_pessoa_fk FOREIGN KEY ( cd_fornecedor )
        REFERENCES CTL_ESTOQUE.pessoa ( cd_pessoa );

ALTER TABLE CTL_ESTOQUE.pedido
    ADD CONSTRAINT pedido_pessoa_fk FOREIGN KEY ( cd_pessoa )
        REFERENCES CTL_ESTOQUE.pessoa ( cd_pessoa );

ALTER TABLE CTL_ESTOQUE.pessoa
    ADD CONSTRAINT pessoa_endereco_fk FOREIGN KEY ( cd_endereco )
        REFERENCES CTL_ESTOQUE.endereco ( cd_endereco );

ALTER TABLE CTL_ESTOQUE.produto_fonecedor
    ADD CONSTRAINT prod_forn_forn_fk FOREIGN KEY ( cd_fornecedor )
        REFERENCES CTL_ESTOQUE.fornecedor ( cd_fornecedor );

ALTER TABLE CTL_ESTOQUE.produto_fonecedor
    ADD CONSTRAINT prod_forn_prod_fk FOREIGN KEY ( cd_produto )
        REFERENCES CTL_ESTOQUE.produto ( cd_produto );

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

ALTER TABLE CTL_ESTOQUE.transacao
    ADD CONSTRAINT transacao_pedido_fk FOREIGN KEY ( cd_pedido )
        REFERENCES CTL_ESTOQUE.pedido ( cd_pedido );

ALTER TABLE CTL_ESTOQUE.transacao
    ADD CONSTRAINT transacao_produto_estoque_fk FOREIGN KEY ( cd_estoque,
                                                              cd_produto )
        REFERENCES CTL_ESTOQUE.produto_estoque ( cd_estoque,
                                     cd_produto );

CREATE SEQUENCE ctl_estoque.sq_cd_municipio START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_municipio BEFORE
    INSERT ON ctl_estoque.municipio
    FOR EACH ROW
    WHEN ( new.cd_municipio IS NULL )
BEGIN
    :new.cd_municipio := ctl_estoque.sq_cd_municipio.nextval;
END;

CREATE SEQUENCE ctl_estoque.sq_cd_endereco START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_endereco BEFORE
    INSERT ON ctl_estoque.endereco
    FOR EACH ROW
    WHEN ( new.cd_endereco IS NULL )
BEGIN
    :new.cd_endereco := ctl_estoque.sq_cd_endereco.nextval;
END;

 SEQUENCE ctl_estoque.sq_cd_pessoa START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_pessoa BEFORE
    INSERT ON ctl_estoque.pessoa
    FOR EACH ROW
    WHEN ( new.cd_pessoa IS NULL )
BEGIN
    :new.cd_pessoa := ctl_estoque.sq_cd_pessoa.nextval;
END;

CREATE SEQUENCE ctl_estoque.sq_cd_pedido START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_pedido BEFORE
    INSERT ON ctl_estoque.pedido
    FOR EACH ROW
    WHEN ( new.cd_pedido IS NULL )
BEGIN
    :new.cd_pedido := ctl_estoque.sq_cd_pedido.nextval;
END;

CREATE SEQUENCE ctl_estoque.sq_cd_estoque START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_estoque BEFORE
    INSERT ON ctl_estoque.estoque
    FOR EACH ROW
    WHEN ( new.cd_estoque IS NULL )
BEGIN
    :new.cd_estoque := ctl_estoque.sq_.nextval;
END;

CREATE SEQUENCE ctl_estoque.sq_cd_produto START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_produto BEFORE
    INSERT ON ctl_estoque.produto
    FOR EACH ROW
    WHEN ( new.cd_produto IS NULL )
BEGIN
    :new.cd_produto := ctl_estoque.sq_cd_produto.nextval;
END;


CREATE SEQUENCE ctl_estoque.sq_cd_transacao START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctl_estoque.trg_cd_transacao BEFORE
    INSERT ON ctl_estoque.transacao
    FOR EACH ROW
    WHEN ( new.cd_transacao IS NULL )
BEGIN
    :new.cd_transacao := ctl_estoque.sq_cd_transacao.nextval;
END;

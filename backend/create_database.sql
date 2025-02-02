create database buscamao;

use buscamao;

CREATE TABLE Usuario (
	Usuario_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Email VARCHAR(255) NOT NULL,
    Senha VARCHAR(255) NOT NULL,
    Nome_usuario VARCHAR(255) NOT NULL,
    Administrador TINYINT(1) NOT NULL DEFAULT 0,
    Feirante TINYINT(1) NOT NULL DEFAULT 0,
    Identificador VARCHAR(255) NOT NULL,
    Foto_perfil MEDIUMBLOB,
    UNIQUE (Email)
);

CREATE TABLE Loja (
    Loja_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    FK_usuario_id INTEGER NOT NULL,
    Localizacao VARCHAR(255) NOT NULL,
    Nome_loja VARCHAR(255) NOT NULL,
    Categoria VARCHAR(255) NOT NULL,
    Descricao_loja TEXT,
    FOREIGN KEY (FK_usuario_id) REFERENCES Usuario(Usuario_id) ON DELETE CASCADE
);

CREATE TABLE Avaliacao_loja (
    Avaliacao_id INTEGER NOT NULL,
    FK_usuario_id INTEGER NOT NULL,
    FK_loja_id INTEGER NOT NULL,
    Nota INT NOT NULL,
    Comentario TEXT,
    FOREIGN KEY (FK_usuario_id) REFERENCES Usuario(Usuario_id) ON DELETE CASCADE,
    FOREIGN KEY (FK_loja_id) REFERENCES Loja(Loja_id) ON DELETE CASCADE
)

CREATE TABLE Produto (
    Produto_id  INTEGER NOT NULL,
    Nome_produto VARCHAR(255) NOT NULL,
    Categoria_produto VARCHAR(255) NOT NULL,
);

CREATE TABLE Avaliacao_produto (
    Avaliacao_id INTEGER NOT NULL,
    FK_usuario_id INTEGER NOT NULL,
    FK_produto_id INTEGER NOT NULL,
    Nota INT NOT NULL,
    Comentario TEXT,
    FOREIGN KEY (FK_usuario_id) REFERENCES Usuario(Usuario_id) ON DELETE CASCADE,
    FOREIGN KEY (FK_produto_id) REFERENCES Produto(Produto_id) ON DELETE CASCADE
)

CREATE TABLE Loja_produto (
    Loja_id INTEGER NOT NULL,
    Produto_id INTEGER NOT NULL,
    Preco DECIMAL(10,2) NOT NULL,
    Descricao_produto TEXT NOT NULL,
    Foto_produto MEDIUMBLOB,
    PRIMARY KEY (Loja_id, Produto_id),
    FOREIGN KEY (Loja_id) REFERENCES Loja(Loja_id) ON DELETE CASCADE,
    FOREIGN KEY (Produto_id) REFERENCES Produto(Produto_id) ON DELETE CASCADE
)

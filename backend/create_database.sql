DROP DATABASE IF EXISTS buscamao;

CREATE DATABASE IF NOT EXISTS buscamao;

USE buscamao;

CREATE TABLE IF NOT EXISTS Usuario (
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

CREATE TABLE IF NOT EXISTS Loja (
    Loja_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Feirante_id INTEGER,
    Localizacao VARCHAR(255) NOT NULL,
    Nome VARCHAR(255) NOT NULL,
    Categoria VARCHAR(255) NOT NULL,
    Descricao TEXT,
    FOREIGN KEY (Feirante_id)
        REFERENCES Usuario (Usuario_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Avaliacao_loja (
    Avaliacao_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Usuario_id INTEGER NOT NULL,
    Loja_id INTEGER NOT NULL,
    Nota INT NOT NULL,
    Comentario TEXT,
    PRIMARY KEY (Usuario_id , Loja_id),
    FOREIGN KEY (Usuario_id)
        REFERENCES Usuario (Usuario_id)
        ON DELETE CASCADE,
    FOREIGN KEY (Loja_id)
        REFERENCES Loja (Loja_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Produto (
    Produto_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Categoria VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Avaliacao_produto (
    Avaliacao_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Usuario_id INTEGER NOT NULL,
    Produto_id INTEGER NOT NULL,
    Nota INT NOT NULL,
    Comentario TEXT,
	PRIMARY KEY (Usuario_id , Produto_id),
    FOREIGN KEY (Usuario_id)
        REFERENCES Usuario (Usuario_id)
        ON DELETE CASCADE,
    FOREIGN KEY (Produto_id)
        REFERENCES Produto (Produto_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Loja_produto (
    Loja_id INTEGER NOT NULL,
    Produto_id INTEGER NOT NULL,
    Preco DECIMAL(10 , 2 ) NOT NULL,
    Descricao_produto TEXT NOT NULL,
    Foto_produto MEDIUMBLOB,
    PRIMARY KEY (Loja_id , Produto_id),
    FOREIGN KEY (Loja_id)
        REFERENCES Loja (Loja_id)
        ON DELETE CASCADE,
    FOREIGN KEY (Produto_id)
        REFERENCES Produto (Produto_id)
        ON DELETE CASCADE
);
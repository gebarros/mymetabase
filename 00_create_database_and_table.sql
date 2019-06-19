
CREATE DATABASE IF NOT EXISTS metabase;

USE metabase;

CREATE TABLE IF NOT EXISTS n_eleitores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    state_code CHAR(10) NOT NULL,
    city  VARCHAR(100) NOT NULL,
    n_eleitores2010 int,
    n_eleitores2012 int,
    n_eleitores2014 int,
    n_eleitores2016 int,
    n_eleitores2018 int
)

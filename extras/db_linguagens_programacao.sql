CREATE TABLE Usuario (
  id INTEGER UNSIGNED  NOT NULL   AUTO_INCREMENT,
  login VARCHAR  NULL  ,
  senha VARCHAR  NULL  ,
  nome VARCHAR  NULL  ,
  documento VARCHAR  NULL  ,
  tipo INTEGER UNSIGNED  NULL    ,
PRIMARY KEY(id));



CREATE TABLE Paciente (
  idPaciente INTEGER UNSIGNED  NOT NULL   AUTO_INCREMENT,
  nome VARCHAR  NULL  ,
  documento VARCHAR  NULL  ,
  dt_nascimento DATE  NULL  ,
  dt_entrada DATE  NULL    ,
PRIMARY KEY(idPaciente));



CREATE TABLE Medico (
  especializacao VARCHAR  NOT NULL   AUTO_INCREMENT,
  Usuario_id INTEGER UNSIGNED  NOT NULL    ,
PRIMARY KEY(especializacao)  ,
INDEX Medico_FKIndex1(Usuario_id),
  FOREIGN KEY(Usuario_id)
    REFERENCES Usuario(id)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION);



CREATE TABLE Administrador (
  Usuario_id INTEGER UNSIGNED  NOT NULL    ,
INDEX Administrador_FKIndex1(Usuario_id),
  FOREIGN KEY(Usuario_id)
    REFERENCES Usuario(id)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION);



CREATE TABLE Atendente (
  Usuario_id INTEGER UNSIGNED  NOT NULL    ,
INDEX Atendente_FKIndex1(Usuario_id),
  FOREIGN KEY(Usuario_id)
    REFERENCES Usuario(id)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION);



CREATE TABLE Auxiliar (
  funcao VARCHAR  NOT NULL   AUTO_INCREMENT,
  Usuario_id INTEGER UNSIGNED  NOT NULL    ,
PRIMARY KEY(funcao)  ,
INDEX Auxiliar_FKIndex1(Usuario_id),
  FOREIGN KEY(Usuario_id)
    REFERENCES Usuario(id)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION);



CREATE TABLE Consulta (
  idConsulta INTEGER UNSIGNED  NOT NULL   AUTO_INCREMENT,
  Paciente_idPaciente INTEGER UNSIGNED  NOT NULL  ,
  Usuario_id INTEGER UNSIGNED  NOT NULL  ,
  dt_registro DATE  NULL  ,
  dt_consulta DATE  NULL  ,
  valor FLOAT  NULL    ,
PRIMARY KEY(idConsulta)  ,
INDEX Consulta_FKIndex1(Usuario_id)  ,
INDEX Consulta_FKIndex2(Usuario_id)  ,
INDEX Consulta_FKIndex3(Paciente_idPaciente),
  FOREIGN KEY(Usuario_id)
    REFERENCES Usuario(id)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Usuario_id)
    REFERENCES Usuario(id)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Paciente_idPaciente)
    REFERENCES Paciente(idPaciente)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION);



CREATE TABLE Auxiliares_Consulta (
  idAuxiliares_Consulta INTEGER UNSIGNED  NOT NULL   AUTO_INCREMENT,
  Consulta_idConsulta INTEGER UNSIGNED  NOT NULL  ,
  Usuario_id INTEGER UNSIGNED  NOT NULL    ,
PRIMARY KEY(idAuxiliares_Consulta)  ,
INDEX Auxiliares_Consulta_FKIndex1(Usuario_id)  ,
INDEX Auxiliares_Consulta_FKIndex2(Consulta_idConsulta),
  FOREIGN KEY(Usuario_id)
    REFERENCES Usuario(id)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION,
  FOREIGN KEY(Consulta_idConsulta)
    REFERENCES Consulta(idConsulta)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION);





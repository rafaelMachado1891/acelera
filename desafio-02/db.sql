DROP TABLE IF EXISTS matriculas;
DROP TABLE IF EXISTS disciplinas;
DROP TABLE IF EXISTS cursos;
DROP TABLE IF EXISTS alunos;

CREATE TABLE alunos(
    matricula SERIAL PRIMARY KEY, 
    nome varchar(50) NOT NULL
);

CREATE TABLE cursos(
    curso CHAR(3) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE disciplinas(
    sigla CHAR(3) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    curso CHAR(3),
    CONSTRAINT fk_disciplina_curso FOREIGN KEY (curso) REFERENCES cursos(curso)
);

CREATE TABLE matriculas(
    matricula INT,
    curso CHAR(3), 
    disciplina CHAR(3),
    periodo_letivo INT,
    PRIMARY KEY (matricula, disciplina, periodo_letivo),
    CONSTRAINT fk_matricula_aluno FOREIGN KEY (matricula) REFERENCES alunos(matricula),
    CONSTRAINT fk_matricula_curso FOREIGN KEY (curso) REFERENCES cursos(curso),
    CONSTRAINT fk_matricula_materia FOREIGN KEY (disciplina) REFERENCES disciplinas(sigla)
);

INSERT INTO alunos(nome) VALUES
    ('Davi'), ('Sophia'), ('Rafael'),
    ('Ismael'), ('Igor'), ('Cristiane'),
    ('Vitoria'), ('Samuel'), ('Ana')
;

INSERT INTO cursos(curso, nome) VALUES
    ('eng', 'engenharia'),
    ('adm', 'administracao'),
    ('cot', 'contabilidade'),
    ('dir', 'direito'),
    ('dsa', 'data science')
;

INSERT  INTO disciplinas(sigla, nome, curso) VALUES
    ('cal', 'calculo 1', 'eng'),
    ('tga', 'teoria geral da administracao', 'adm'),
    ('con', 'controladoria', 'cot'),
    ('dit', 'direito tributario', 'dir'),
    ('eta', 'estatistica aplicada', 'dsa')
;

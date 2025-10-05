# 🚀 Desafio nº 2 do programa acelara jornada de dados!!! 

---

## 📑 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- 🐳 [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- 🧰 Git (para clonar o repositório)

---

## 🔧 Como rodar o projeto com Docker

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/rafaelMachado1891/acelera.git

```

### 2️⃣ Acessar o diretório desafio-02

``` bash
cd desafio-02

```
### 3️⃣ Subir o container com Docker

```
docker compose up -d
```
### Store procedure
```
CREATE OR REPLACE PROCEDURE public.sp_matricula_aluno(
	IN p_nome_do_aluno character varying,
	IN p_nome_do_curso character varying
)
LANGUAGE 'plpgsql'
AS $$

DECLARE
	p_matricula INT;
	p_curso CHAR(3);
	p_disciplina CHAR(3);
	p_periodo_letivo_ano INT;
	p_periodo_letivo_semestre INT;
	p_periodo_letivo INT;
BEGIN

	p_periodo_letivo_ano := EXTRACT(YEAR FROM CURRENT_DATE);
	p_periodo_letivo_semestre := CASE 
		WHEN EXTRACT(MONTH FROM CURRENT_DATE) <= 6 THEN 1
		ELSE 2
	END;
	p_periodo_letivo := (p_periodo_letivo_ano * 10) + p_periodo_letivo_semestre;
	
	SELECT matricula INTO p_matricula
	FROM alunos
	WHERE nome = p_nome_do_aluno;

	IF p_matricula IS NULL THEN
		RAISE EXCEPTION 'Aluno % não encontrado', p_aluno;
	END IF;	

	SELECT  curso INTO p_curso
	FROM cursos
	WHERE nome = p_nome_do_curso;

	IF p_curso IS NULL THEN
		RAISE EXCEPTION 'Curso % não encontrado', p_nome_do_curso;
	END IF;

	FOR p_disciplina IN 
		SELECT sigla
		FROM disciplinas 
		WHERE curso = p_curso
	LOOP
		INSERT INTO matriculas(matricula, curso, disciplina, periodo_letivo)
		VALUES(p_matricula, p_curso, p_disciplina, p_periodo_letivo);
	END LOOP;

	RAISE NOTICE 'Aluno % matriculado no curso % - disciplina % - período %.',
        p_nome_do_aluno, p_nome_do_curso, p_disciplina, p_periodo_letivo;
		

END
$$;


DROP TABLE IF EXISTS tb_email;
CREATE TABLE tb_email(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_user TEXT NOT NULL, 
    to_user TEXT NOT NULL, 
    day INT NOT NULL
);
INSERT INTO tb_email(from_user, to_user, day)
VALUES
        ('ana', 'bruno', 1),
        ('ana', 'carlos', 1),
        ('bruno', 'daniela',1),
        ('carlos', 'ana', 2),
        ('ana', 'daniela', 2),
        ('bruno', 'carlos', 2),
        ('ana', 'erica', 3),
        ('carlos', 'ana', 3),
        ('flavio', 'erica', 4);
WITH emails_enviados AS (
SELECT 
    from_user,
    COUNT(*) AS email_enviados
FROM tb_email 
GROUP BY from_user
),
ranking_emails AS (
SELECT
    from_user,
    email_enviados,
    RANK() OVER(ORDER BY email_enviados DESC) AS ranking,
    DENSE_RANK() OVER(ORDER BY email_enviados DESC) AS dense_ranking,
    ROW_NUMBER() OVER(ORDER BY email_enviados DESC) AS row_number

FROM emails_enviados
)
SELECT * FROM ranking_emails;
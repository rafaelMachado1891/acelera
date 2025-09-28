SELECT 
    from_user,
    COUNT(*) AS email_enviados
FROM tb_email 
GROUP BY from_user

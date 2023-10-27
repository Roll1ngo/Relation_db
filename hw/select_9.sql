SELECT st.fullname , dis.name 
FROM grades gd
JOIN disciplines dis ON dis.id = gd.discipline_id
JOIN students st ON st.id = gd.student_id
WHERE st.id = 20
GROUP BY dis.name
ORDER BY dis.name 
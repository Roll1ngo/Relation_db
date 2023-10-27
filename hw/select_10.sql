SELECT st.fullname , dis.name ,t.fullname
FROM grades gd
JOIN disciplines dis ON dis.id = gd.discipline_id
JOIN students st ON st.id = gd.student_id
JOIN teachers t ON t.id = dis.teacher_id 
WHERE t.id = 4 and st.id = 23
GROUP BY t.fullname 
ORDER BY dis.name ;
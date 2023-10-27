SELECT gr.name , dis.name, gd.grade
FROM grades gd
JOIN disciplines dis ON dis.id = gd.discipline_id
JOIN students st ON st.id = gd.student_id
JOIN groups gr ON st.group_id  = gr.id 
WHERE dis.id = 6 and gr.id = 2
GROUP BY dis.name;
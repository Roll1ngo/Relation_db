SELECT g.name , dis.name, ROUND(AVG(gr.grade),2) as average_grade
FROM grades gr
JOIN disciplines dis ON dis.id = gr.discipline_id
JOIN students st ON st.id = gr.student_id
JOIN groups g ON st.group_id  = g.id 
WHERE dis.id = 6
GROUP BY dis.name
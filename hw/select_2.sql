SELECT st.fullname,dis.name, ROUND(AVG(gr.grade),2) as average_grade
FROM grades gr
JOIN students st ON st.id = gr.student_id
JOIN disciplines dis ON dis.id = gr.discipline_id 
WHERE dis.id = 1
GROUP BY dis.name
ORDER BY average_grade DESC;
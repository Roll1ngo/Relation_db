SELECT t.fullname , dis.name, ROUND(AVG(g.grade),2) as average_grade
FROM disciplines dis
JOIN teachers t ON t.id = dis.teacher_id 
JOIN grades g ON dis.id  = g.discipline_id 
WHERE t.id  = 2
ORDER BY t.fullname;
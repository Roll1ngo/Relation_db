SELECT  ROUND(AVG(gr.grade),2) as average_grade
FROM grades gr
ORDER BY average_grade ASC;
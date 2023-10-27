import sqlite3
from pprint import pprint as print

                #Знайти 5 студентів із найбільшим середнім балом з усіх предметів
select_1 = '''
SELECT s.fullname, ROUND(AVG(g.grade),2) AS average_grade
FROM  grades g
LEFT JOIN students s ON s.id = g.student_id
GROUP BY s.fullname
ORDER BY average_grade DESC
LIMIT 5;'''
                #Знайти студента із найвищим середнім балом з певного предмета
select_2 ='''
SELECT st.fullname,dis.name, ROUND(AVG(gr.grade),2) as average_grade
FROM grades gr
JOIN students st ON st.id = gr.student_id
JOIN disciplines dis ON dis.id = gr.discipline_id 
WHERE dis.id = 1
GROUP BY dis.name
ORDER BY average_grade DESC;
'''
#Знайти середній бал у групах з певного предмета

select_3 = '''
SELECT g.name , dis.name, ROUND(AVG(gr.grade),2) as average_grade
FROM grades gr
JOIN disciplines dis ON dis.id = gr.discipline_id
JOIN students st ON st.id = gr.student_id
JOIN groups g ON st.group_id  = g.id 
WHERE dis.id = 6
GROUP BY dis.name

'''
                #Знайти середній бал на потоці (по всій таблиці оцінок).
select_4 = '''
SELECT  ROUND(AVG(gr.grade),2) as average_grade
FROM grades gr
ORDER BY average_grade ASC;
'''
                #Знайти які курси читає певний викладач
select_5 = '''
SELECT dis.name, t.fullname
FROM  disciplines dis
LEFT JOIN teachers t  ON dis.teacher_id  = t.id
WHERE t.id =4
ORDER BY dis.name;'''

#Знайти список студентів у певній групі.
select_6 = '''
SELECT st.fullname, gr.name
FROM students st
JOIN groups gr ON st.group_id  = gr.id
WHERE gr.id = 2
ORDER BY gr.name;
'''
#Знайти оцінки студентів у окремій групі з певного предмета.
select_7 = '''
SELECT gr.name , dis.name, gd.grade
FROM grades gd
JOIN disciplines dis ON dis.id = gd.discipline_id
JOIN students st ON st.id = gd.student_id
JOIN groups gr ON st.group_id  = gr.id 
WHERE dis.id = 6 and gr.id = 2
GROUP BY dis.name;
;'''
        #Знайти середній бал, який ставить певний викладач зі своїх предметів.
select_8 = '''
SELECT t.fullname , dis.name, ROUND(AVG(g.grade),2) as average_grade
FROM disciplines dis
JOIN teachers t ON t.id = dis.teacher_id 
JOIN grades g ON dis.id  = g.discipline_id 
WHERE t.id  = 2
ORDER BY t.fullname;
'''
    #Знайти список курсів, які відвідує студент.
select_9 = '''
SELECT st.fullname , dis.name 
FROM grades gd
JOIN disciplines dis ON dis.id = gd.discipline_id
JOIN students st ON st.id = gd.student_id
WHERE st.id = 20
GROUP BY dis.name
ORDER BY dis.name 
;'''
    #Список курсів, які певному студенту читає певний викладач
select_10 = '''
SELECT st.fullname , dis.name ,t.fullname
FROM grades gd
JOIN disciplines dis ON dis.id = gd.discipline_id
JOIN students st ON st.id = gd.student_id
JOIN teachers t ON t.id = dis.teacher_id 
WHERE t.id = 4 and st.id = 23
GROUP BY t.fullname 
ORDER BY dis.name ;
'''


if __name__ == '__main__':
    connect = sqlite3.connect('hw_db.sqlite')
    cur = connect.cursor()
    cur.executescript(select_5)
    connect.commit()
    print(cur.fetchall())
    cur.close()
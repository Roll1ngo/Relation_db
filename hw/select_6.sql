SELECT st.fullname, gr.name
FROM students st
JOIN groups gr ON st.group_id  = gr.id
WHERE gr.id = 2
ORDER BY gr.name;
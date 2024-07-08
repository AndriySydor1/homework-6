WITH LastClass AS (
    SELECT student_id, MAX(date) AS last_date
    FROM grades
    WHERE subject_id = ?
    GROUP BY student_id
)
SELECT students.name AS student_name, grades.grade, grades.date
FROM grades
JOIN LastClass ON grades.student_id = LastClass.student_id AND grades.date = LastClass.last_date
JOIN students ON grades.student_id = students.id
WHERE students.group_id = ? AND grades.subject_id = ?;

  
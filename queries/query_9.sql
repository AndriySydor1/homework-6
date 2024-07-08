SELECT subjects.name AS subject_name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.student_id = ?
GROUP BY subjects.id;


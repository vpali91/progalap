student_scores ={
    "Pali":92,
    "Zoli":45,
    "Brigi":65,
    "Sanyi":71
}
student_grades = {}
#90<jeles
#80<jó
#70<közepes
#50 < elégséges
#51>elégtelen

for key in student_scores.keys():
    if student_scores[key]>90:
        student_grades[key] = "Jeles"
    elif student_scores[key]>80:
        student_grades[key] = "Jó"
    elif student_scores[key]>70:
        student_grades[key] = "Közepes"
    elif student_scores[key]>50:
        student_grades[key] = "Elégséges"
    elif student_scores[key]<51:
        student_grades[key] = "Elégtelen"

print(student_grades)



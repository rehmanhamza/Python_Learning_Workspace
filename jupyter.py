total_marks=float(500)

maths=98
english=85
urdu=82
physics=92
chemistry=87

obtained_marks=float(maths+english+urdu+physics+chemistry)
percentage=obtained_marks/total_marks*100

grade=""
if percentage >= 90 and percentage < 100:
    grade="A+"
elif percentage >= 80 and percentage < 90:
    grade="A"
elif percentage >= 70 and percentage < 80:
    grade="B"
elif percentage >= 60 and percentage < 70:
    grade="C"
else:
    grade="FAIL"

print "Grade =", grade
print "Percentage =", percentage
print "Obtained Marks", obtained_marks, "out of", total_marks 
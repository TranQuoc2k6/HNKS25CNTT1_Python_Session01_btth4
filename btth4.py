student_name = input("Nhập họ tên sinh viên: ")
student_age = input("Nhập Tuổi: ")
average_score = input("Nhập điểm trung bình: ")

student_age = int(student_age)
average_score = float(average_score)

bonus_score = average_score + 0.5

print()
print()
print(f"Tên sinh viên: {student_name}")
print(f"Tuổi: {student_age}")
print(f"Điểm trung bình: {average_score}")
print(f"Điểm sau thưởng: {bonus_score}")


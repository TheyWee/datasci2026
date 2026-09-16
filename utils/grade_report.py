import pandas as pd

# --- СТУДЕНТ ЗАПОВНЮЄ СВОЇ ДАНІ НАПОЧАТКУ АБО ТУТ ---
STUDENT_NAME = "Андрій Ковальчук"
# STUDENT_ID = "2-Б"
# --------------------------------------------------

# 1. Отримуємо бали
try:
    results_obj = grader.check_all()
    total = results_obj.total
    possible = results_obj.possible
except:
    total, possible = 0, 0 # Якщо тести не запускалися

# 2. Формуємо структуру таблиці
data = {
    "Student Name": [STUDENT_NAME],
    #"Student ID": [STUDENT_ID],
    "Total Score": [total],
    "Max Possible": [possible]
}

# 3. Перетворюємо в DataFrame та зберігаємо в CSV
df = pd.DataFrame(data)
df.to_csv("my_grades.csv", index=False, encoding="utf-8-sig")

print("Оцінки успішно збережено у файл 'my_grades.csv'!")


import pandas as pd

# 1. Запускаємо перевірку та отримуємо об'єкт результатів
results_obj = grader.check_all()

# 2. ЗБЕРЕЖЕННЯ ДЕТАЛЬНОГО ТЕКСТОВОГО ЗВІТУ (ЛОГУ ПОМИЛОК)
# Метод str() автоматично витягує весь той детальний текст із "Test case failed", "Expected", "Got" та NameError
detailed_log = str(results_obj)

with open("grading_report.txt", "w", encoding="utf-8") as text_file:
    text_file.write(detailed_log)

# 3. ЗБЕРЕЖЕННЯ БАЛІВ У ТАБЛИЦЮ CSV
# Витягуємо загальний бал, максимум, а також бали за кожне окреме питання
grades_data = {
    "Question": [],
    "Score": [],
    "Possible": []
}

# Заповнюємо бали за кожне питання окремо (наприклад, q3_1_2, q3_3_1)
for q_name, q_res in results_obj.tests.items():
    grades_data["Question"].append(q_name)
    grades_data["Score"].append(q_res.score)
    grades_data["Possible"].append(q_res.possible)

# Додаємо фінальний рядок із загальним підсумком
grades_data["Question"].append("TOTAL")
grades_data["Score"].append(results_obj.total)
grades_data["Possible"].append(results_obj.possible)

# Експортуємо в CSV
df = pd.DataFrame(grades_data)
df.to_csv("student_grades.csv", index=False, encoding="utf-8-sig")

print("Успішно згенеровано два файли:")
print("1. 'student_grades.csv' — таблиця з балами.")
print("2. 'grading_report.txt' — детальний текстовий лог усіх помилок.")

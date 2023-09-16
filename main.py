import pandas as pd
data = pd.read_excel('lab_pi_101.xlsx')

# кол-во оценок (3, 4, 5) в столбце "Сокращенная оценка"
total_marks = sum(data["Сокращенная оценка"].value_counts().loc[[3, 4, 5]])

# кол-во оценок (3, 4, 5) группц ПИ101
pi101_marks = sum(data[data["Группа"] == "ПИ101"]["Сокращенная оценка"].value_counts().loc[[3, 4, 5]])

# кол-во уникальных личных номеров студентов
total_num_stud = data["Личный номер студента"].nunique()

# кол-во уникальных личных номеров студентов группы ПИ101
pi101_num_stud = data[data["Группа"] == "ПИ101"]["Личный номер студента"].unique()
# Вывод полученных элементов через запятую
pi101_num_stud_str = ', '.join(map(str, pi101_num_stud))

# Используемые формы контроля:
form_control = data["Уровень контроля"].unique()
form_control_str = ', '.join(map(str, form_control))

# Года:
years = data[data["Группа"] == "ПИ101"]["Год"].unique()
years_str = ', '.join(map(str, years))

print(" В исходном датасете содержалось ", total_marks, " оценок, из них ", pi101_marks, "оценок относятся к группе ПИ101.", '\n',"В датасете находятся оценки ", total_num_stud, "студентов,  со следующими личными номерами (по ПИ101):",pi101_num_stud_str,'\n', "Используемые формы контроля:", form_control_str,'\n', "Данные представлены по следующим учебным годам:", years_str )
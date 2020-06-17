'''
Создать базу данных студентов.У студента есть факультет, группа, оценки, номер студенческого билета. Написать программу,
с двумя ролями: Администратор, Пользователь. Администратор может добавлять, изменять существующих студентов.
Пользователь может получать список отличников,список всех студентов,искать студентов по по номеру студенческого,получать
полную информацию о конкретном студенте (включая оценки, факультет)
'''

import sqlite3

class Dbopen:

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        return self.conn

    def __exit__(self, exc_class, exc, traceback):
        self.conn.commit()
        self.conn.close()
        return True

class Students():

    def __init__(self, cardID):
        self.cardID = cardID

    def best_students(self):
        with Dbopen('test.db') as userlist:
            query = userlist.cursor()
            info = query.execute(
                "SELECT name, surname from USER_DICT_FILE "
                "INNER JOIN GRADES ON GRADES.student_card = USER_DICT_FILE.cardID"
                " where marks = 5")
            print(info.fetchall())

    def students(self):
        with Dbopen('test.db') as userlist:
            cursor = userlist.cursor()
            res = cursor.execute("SELECT * from USER_DICT_FILE")
            print(res.fetchall())

    def search_student(self, cardID):
        catalogue = (cardID ,)
        with Dbopen('test.db') as userlist:
            query = userlist.cursor()
            info = query.execute("SELECT 'name', 'surname' from USER_DICT_FILE where 'cardID' = ?", catalogue)
            print(info.fetchall())

    def show_info(self, cardID):
        catalogue = (cardID,)
        with Dbopen('test.db') as userlist:
            query = userlist.cursor()
            query.execute(
                "SELECT * from USER_DICT_FILE INNER JOIN GRADES ON GRADES.cardID = "
                "USER_DICT_FILE.cardID INNER JOIN 'faculty' ON "
                "FACULTY.id = USER_DICT_FILE.faculty WHERE 'cardID' = ?",
                catalogue)
            print(query.fetchall())

class Administrator():
    def __init__(self ,admin_key):
        self.admin_key = admin_key

    def add_new_student(self, name, surname, faculty, group, cardID):

        with Dbopen('test.db') as userlist:
            query = userlist.cursor()
            query.execute(
                "INSERT INTO USER_DICT_FILE "
                "( 'name', 'surname', 'faculty', 'group', 'cardID') "
                "VALUES (%s, %s, %s, %s)", [name,
                                         surname,
                                         faculty,
                                         group,
                                         cardID])

    def update_student(self,param ,value, cardID):
        with Dbopen('test.db') as userlist:
            query = userlist.cursor()
            query.execute(f"UPDATE USER_DICT_FILE SET {param} = {value} WHERE 'cardID' = {cardID}")


some_student = Students(1)
some_student.search_student(1)
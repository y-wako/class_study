class Person:
    def __init__(self, name, age): #コンストラクタで名前と年齢を初期化
        self.name = name
        self.age = age
    
    def birthday(self): #年齢を１歳増やすメソッド
        self.age += 1
        print(f"🎂 {self.name} さん、お誕生日おめでとう！年齢: {self.age}")

class Student(Person): #Personクラスを継承
    def __init__(self, name, age, student_id):
        super().__init__(name, age) #親クラスのコンストラクタを呼び出し
        self.student_id = student_id
    def get_student_id(self): #学生番号を返すメソッド
        return f"🎓 学生番号: {self.student_id}"

p1 = Person("Alics", 25)
p1.birthday()

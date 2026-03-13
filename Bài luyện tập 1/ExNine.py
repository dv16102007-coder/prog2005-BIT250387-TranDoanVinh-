def bai_tap9 ():
  class Student:
      def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
      def display(self):
        print("Sinh viên", self.ten, "có điểm là", self.diem)
  sv1 = Student ("A",10)
  sv2 = Student ("B",8)

  sv1.display()
  sv2.display()

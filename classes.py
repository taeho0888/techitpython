
class Student:

    # 생성자 함수, class가 선언되면 자동으로 실행됨
    def __init__(self, name, major, is_graduated):  # 어떤 파라미터를 쓸 건지
        self.name = name
        self.major = major
        self.is_graduated = is_graduated

    # 메서드
    def study(self):
        print(f"{self.name} 학생은 공부 중 입니다.")
        # 생성자에서 정의된 name을 self.name으로 불러올 수 있다


# 인스턴스 - 실체화된 사물
student_1 = Student('윤태호', '경영학과', False)  # Self를 제외한 인자를 넣어주어 선언한다

'''
print(student_1)
<__main__.Student object at 0x1051973d0>

print(student_1.major)
경영학과
'''

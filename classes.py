
class Student:

    # 생성자 함수, class가 선언되면 자동으로 실행됨
    def __init__(self, name, major, is_graduated):  # 어떤 파라미터를 쓸 건지
        self.name = name
        self.major = major
        self.is_graduated = is_graduated
        # self.is_graduated = False 같은 걸로도 세팅 가능, 생성자 파라미터에서 빼야함

    # 메소드
    def study(self):
        print(f"{self.name} 학생은 공부 중 입니다.")
        # 생성자에서 정의된 name을 self.name으로 불러올 수 있다

    # 생성자에서 생성된 값을 수정하는 함수
    def edit_major(self, new_major):
        self.major = new_major
        print(f"전공이 {self.major}로 변경되었습니다.")


# 인스턴스 - 실체화된 사물
student_1 = Student('윤태호', '경영학과', False)  # Self를 제외한 인자를 넣어주어 선언한다


# print(student_1)
# <__main__.Student object at 0x1051973d0>

# print(student_1.major)
# 경영학과

# student_1.study()
# 윤태호 학생은 공부 중 입니다.


# 인스턴스 값 수정 방법
student_1.major = '융합소프트웨어'

# print(student_1.major)
# 융합소프트웨어

# 근데 이렇게 수정하는 것은 바람직하지 않음
# 클래스 내부에 값을 수정하는 함수를 작성하고 사용하는 것이 좋음


student_1.edit_major('컴퓨터공학')


# 상속
class Foreign_student(Student):
    # 이렇게 상속받는 순간 Student 클래스에 정의된 모든 내용을 가져오게 된다

    def __init__(self, name, major, is_graduated, country):
        # 부모 클래스에 있는 __init__을 쓸 수 있는 코드
        super().__init__(name, major, is_graduated)

        # 새로운 인자를 받는 코드
        self.country = country

    # 메소드 오버라이딩
    def study(self):
        print(f"{self.name} is studying.")


foreign_student_1 = Foreign_student('김멋사', '컴퓨터공학과', True, '한국')

# print(foreign_student_1.country)
# 한국
# foreign_student_1.study()
# 김멋사 is studying.

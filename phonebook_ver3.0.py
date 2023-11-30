class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        if not self.is_valid_number(number):
            return "유효하지 않은 전화번호 형식입니다."
        if name in self.contacts and self.contacts[name] == number:
            return "중복된 연락처입니다."
        self.contacts[name] = number
        return "연락처 추가됨"

    def is_valid_number(self, number):
        # 간단한 전화번호 유효성 검사: 숫자와 하이픈만 포함되어 있는지 확인
        return all(char.isdigit() or char == '-' for char in number)

    def view_contacts(self):
        if not self.contacts:
            print("저장된 번호가 없습니다.")
            return
        for name, number in self.contacts.items():
            print(f"{name}: {number}")

    def search_contact(self, name):
        return self.contacts.get(name, "찾을 수 없음")

    def update_contact(self, name, number):
        if name not in self.contacts:
            return "연락처를 찾을 수 없음"
        if not self.is_valid_number(number):
            return "유효하지 않은 전화번호 형식입니다."
        self.contacts[name] = number
        return "업데이트됨"

    def delete_contact(self, name):
        if name not in self.contacts:
            return "연락처를 찾을 수 없음"
        del self.contacts[name]
        return "삭제됨"

    def run(self):
        while True:
            print("\n전화번호부 옵션:")
            print("1. 연락처 추가")
            print("2. 모든 연락처 보기")
            print("3. 연락처 검색")
            print("4. 연락처 업데이트")
            print("5. 연락처 삭제")
            print("6. 종료")
            choice = input("옵션을 선택하세요: ")

            try:
                if choice == "1":
                    name = input("이름을 입력하세요: ")
                    number = input("전화번호를 입력하세요: ")
                    print(self.add_contact(name, number))
                elif choice == "2":
                    self.view_contacts()
                elif choice == "3":
                    name = input("검색할 이름을 입력하세요: ")
                    print(f"{name}: {self.search_contact(name)}")
                elif choice == "4":
                    name = input("업데이트할 이름을 입력하세요: ")
                    number = input("새 전화번호를 입력하세요: ")
                    print(self.update_contact(name, number))
                elif choice == "5":
                    name = input("삭제할 이름을 입력하세요: ")
                    print(self.delete_contact(name))
                elif choice == "6":
                    print("전화번호부를 종료합니다...")
                    break
                else:
                    print("잘못된 선택입니다. 다시 시도하세요.")
            except Exception as e:
                print(f"오류 발생: {e}")

# To run the program, create an instance of Phonebook and call the run method.
# phonebook = Phonebook()
# phonebook.run()

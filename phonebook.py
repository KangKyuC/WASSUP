def add_contact(contacts, name, number):
    for existing_name, existing_number in contacts.items():
        if existing_name == name and existing_number == number:
            return "중복된 연락처입니다."
    contacts[name] = number
    return "연락처 추가됨"

def view_contacts(contacts):
    if not contacts:
        print("저장된 번호가 없습니다.")
        return
    for name, number in contacts.items():
        print(f"{name}: {number}")

def search_contact(contacts, name):
    return contacts.get(name, "찾을 수 없음")

def update_contact(contacts, name, number):
    if name not in contacts:
        return "연락처를 찾을 수 없음"
    contacts[name] = number
    return "업데이트됨"

def delete_contact(contacts, name):
    if name not in contacts:
        return "연락처를 찾을 수 없음"
    del contacts[name]
    return "삭제됨"

def phonebook():
    contacts = {}
    while True:
        print("\n전화번호부 옵션:")
        print("1. 연락처 추가")
        print("2. 모든 연락처 보기")
        print("3. 연락처 검색")
        print("4. 연락처 업데이트")
        print("5. 연락처 삭제")
        print("6. 종료")
        choice = input("옵션을 선택하세요: ")

        if choice == "1":
            name = input("이름을 입력하세요: ")
            number = input("전화번호를 입력하세요: ")
            print(add_contact(contacts, name, number))
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            name = input("검색할 이름을 입력하세요: ")
            print(f"{name}: {search_contact(contacts, name)}")
        elif choice == "4":
            name = input("업데이트할 이름을 입력하세요: ")
            number = input("새 전화번호를 입력하세요: ")
            print(update_contact(contacts, name, number))
        elif choice == "5":
            name = input("삭제할 이름을 입력하세요: ")
            print(delete_contact(contacts, name))
        elif choice == "6":
            print("전화번호부를 종료합니다...")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

phonebook()

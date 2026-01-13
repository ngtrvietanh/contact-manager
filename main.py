import json
import os
import re   # <-- thêm import regex

DATA_FILE = "data/contacts.json"

# --- HÀM LOAD & SAVE DỮ LIỆU ---
def load_contacts():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


# --- HIỂN THỊ MENU ---
def display_menu():
    print("\n--- MENU DANH BẠ ---")
    print("1. Thêm liên hệ")
    print("2. Xem danh bạ")
    print("3. Tìm kiếm liên hệ")
    print("4. Xóa liên hệ")
    print("5. Thoát")


# --- VALIDATION ---
def validate_phone(phone):
    return phone.isdigit() and 9 <= len(phone) <= 11

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


# --- THÊM LIÊN HỆ ---
def add_contact(contacts):
    print("\n--- THÊM LIÊN HỆ MỚI ---")

    name = input("Nhập tên: ")

    # Validate phone
    while True:
        phone = input("Nhập số điện thoại: ")
        if validate_phone(phone):
            break
        print("❌ Số điện thoại không hợp lệ! (Chỉ số, 9–11 chữ số)")

    # Validate email
    while True:
        email = input("Nhập email: ")
        if validate_email(email):
            break
        print("❌ Email không hợp lệ! (Ví dụ: abc@gmail.com)")

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"✔️ Đã thêm liên hệ '{name}' thành công.")


# --- XEM DANH BẠ ---
def view_contacts(contacts):
    print("\n--- DANH BẠ HIỆN TẠI ---")
    if not contacts:
        print("Danh bạ trống!")
        return

    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")


# --- TÌM KIẾM LIÊN HỆ ---
def search_contact(contacts):
    keyword = input("\nNhập từ khóa cần tìm: ").lower()
    print("\n--- KẾT QUẢ TÌM KIẾM ---")

    results = [
        c for c in contacts
        if keyword in c["name"].lower()
        or keyword in c["phone"]
        or keyword in c["email"].lower()
    ]

    if not results:
        print("Không tìm thấy liên hệ phù hợp.")
        return

    for idx, contact in enumerate(results, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")


# --- XÓA LIÊN HỆ ---
def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    index = int(input("\nNhập số thứ tự liên hệ muốn xóa: ")) - 1

    if 0 <= index < len(contacts):
        deleted = contacts.pop(index)
        save_contacts(contacts)
        print(f"Đã xóa liên hệ: {deleted['name']}")
    else:
        print("Số thứ tự không hợp lệ.")


# --- MAIN PROGRAM ---
def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")


if __name__ == "__main__":
    main()

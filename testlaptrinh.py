import random
import os
import time
import sys

# =========================
#Tài Xỉu Tạo Bởi Công Hậu
# =========================

balance = 1000000
history = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def roll_dice():
    return random.randint(1,6), random.randint(1,6), random.randint(1,6)

# 🎲 Hiệu ứng xúc xắc quay
def dice_animation():
    print("Đang lắc xúc xắc...")
    for i in range(15):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        print(f"\r🎲 {d1} - {d2} - {d3}", end="")
        sys.stdout.flush()
        time.sleep(0.15)
    print()

def show_menu():
    print("====== GAME TÀI XỈU ======")
    print("1. Chơi")
    print("2. Xem lịch sử")
    print("3. Thoát")
    print("==========================")

while True:
    clear()
    print(f"💰 SỐ DƯ CỦA BẠN: {balance:,} VND")
    show_menu()

    choice = input("Chọn: ")

    if choice == "1":

        if balance <= 0:
            print("❌ Bạn đã hết tiền!")
            input("Nhấn Enter để tiếp tục...")
            continue

        try:
            bet = int(input("Nhập số tiền cược: "))
        except:
            print("❌ Nhập sai định dạng!")
            input("Enter để tiếp tục...")
            continue

        if bet > balance or bet <= 0:
            print("❌ Số tiền cược không hợp lệ!")
            input("Enter để tiếp tục...")
            continue

        user_choice = input("Chọn Tài hoặc Xỉu (t/x): ").lower()

        if user_choice not in ["t", "x"]:
            print("❌ Lựa chọn không hợp lệ!")
            input("Enter để tiếp tục...")
            continue

        # 🎲 Chạy hiệu ứng
        dice_animation()

        # 🎯 Kết quả thật
        d1, d2, d3 = roll_dice()
        total = d1 + d2 + d3

        print(f"Kết quả cuối: 🎲 {d1} - {d2} - {d3}")
        print(f"Tổng: {total}")

        # Xác định tài xỉu
        if 11 <= total <= 17:
            result = "t"
            result_text = "TÀI"
        elif 4 <= total <= 10:
            result = "x"
            result_text = "XỈU"
        else:
            result = "house"
            result_text = "BỘ BA - NHÀ CÁI THẮNG"

        print("👉 Kết quả là:", result_text)

        if result == user_choice:
            win = bet
            balance += win
            print(f"🎉 Bạn thắng {win} VND!")
            history.append(f"Thắng +{win}")
        else:
            balance -= bet
            print(f"💀 Bạn thua {bet} VND!")
            history.append(f"Thua -{bet}")

        input("Nhấn Enter để tiếp tục...")

    elif choice == "2":
        print("===== 📜 LỊCH SỬ =====")
        for i, h in enumerate(history, 1):
            print(f"Ván {i}: {h}")
        input("Nhấn Enter để tiếp tục...")

    elif choice == "3":
        print("Cảm ơn bạn đã chơi!")
        break

    else:
        print("❌ Lựa chọn không hợp lệ!")
        input("Nhấn Enter để tiếp tục...")

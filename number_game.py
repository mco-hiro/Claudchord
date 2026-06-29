import random

def main():
    print("=== 数当てゲーム ===")
    print("1〜100の数を当ててください！")
    print()

    answer = random.randint(1, 100)
    tries = 0

    while True:
        guess_input = input("あなたの予想: ")

        if not guess_input.isdigit():
            print("数字を入力してください。")
            continue

        guess = int(guess_input)
        tries += 1

        if guess < answer:
            print("もっと大きい数です！")
        elif guess > answer:
            print("もっと小さい数です！")
        else:
            print(f"正解！ {tries}回で当たりました！")
            break

if __name__ == "__main__":
    main()

def count_letters(filename):
    # 初始化字母计数的字典
    letter_count = {}

    try:
        # 打开文件
        with open(filename, 'r', encoding='utf-8') as file:
            # 逐行读取文件内容
            for line in file:
                # 遍历每个字符
                for char in line:
                    # 如果是字母，则统计次数（不区分大小写）
                    if char.isalpha():
                        char = char.lower()  # 统一转换为小写字母
                        letter_count[char] = letter_count.get(char, 0) + 1

    except FileNotFoundError:
        print(f"文件 '{filename}' 未找到.")
    except Exception as e:
        print(f"发生错误: {e}")
    else:
        # 按出现次数由高到低排序
        sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

        # 输出结果
        print("字母出现次数:")
        for letter, count in sorted_letter_count:
            print(f"{letter}: {count}")

# 用法示例：替换 'your_file.txt' 为你的实际文件路径
count_letters('e.txt')
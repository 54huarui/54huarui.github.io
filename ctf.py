def count_words(filename):
    # 初始化单词计数的字典
    word_count = {}

    try:
        # 打开文件
        with open(filename, 'r', encoding='utf-8') as file:
            # 读取整个文件内容
            content = file.read()
            # 根据连字符 '-' 分割文本成单词列表
            words = content.split('-')

            # 遍历每个单词
            for word in words:
                # 去除首尾空格并转为小写
                word = word.strip().lower()
                # 如果是非空单词，则统计次数
                if word:
                    word_count[word] = word_count.get(word, 0) + 1

    except FileNotFoundError:
        print(f"文件 '{filename}' 未找到.")
    except Exception as e:
        print(f"发生错误: {e}")
    else:
        # 按出现次数由高到低排序
        sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

        # 输出结果
        print("单词出现次数:")
        for word, count in sorted_word_count:
            print(f"{word}: {count}")


# 用法示例：替换 'your_file.txt' 为你的实际文件路径


count_words('e.txt')

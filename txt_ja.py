# ユーザーからアップロードされたファイルのパス
file_path = r"/mnt/c/Users/iniad/Downloads/DEG.txt"

# ファイルを読み込んで、日本語の文章のみを抽出するための関数を定義
def extract_japanese_text(file_path):
    import re
    
    # 日本語を含む文字列にマッチする正規表現パターン
    japanese_pattern = re.compile(r'[\u3000-\u303F\u3040-\u309F\u30A0-\u30FF\u3400-\u4DBF\u4E00-\u9FFF]+')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    # 日本語の文章のみを抽出
    japanese_lines = [line for line in content if japanese_pattern.search(line)]
    
    # 抽出した日本語の文章を新しいファイルに書き込む
    output_path = r"/mnt/c/Users/iniad/Downloads/DEG_ja.txt"
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(japanese_lines)
    
    return output_path

# 関数を実行して、抽出した日本語の文章のみが書かれたファイルのパスを取得
extracted_file_path = extract_japanese_text(file_path)
extracted_file_path

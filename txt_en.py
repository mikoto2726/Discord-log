import re

def extract_messages(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # メッセージの本文を抽出する正規表現パターン
    # ここでは簡単のため、タイムスタンプやユーザー名などを含む行の後に来るテキストを本文として扱います。
    pattern = r"\[\d{4}/\d{2}/\d{2} \d{2}:\d{2}\] .+?\n(.+?)(?=\n\[|\Z)"
    messages = re.findall(pattern, content, re.DOTALL)
    
    # 抽出したメッセージを新しいファイルに書き込む
    output_filepath =  r"/mnt/c/Users/iniad/Downloads/new_Hyperliquid.txt"
    with open(output_filepath, 'w', encoding='utf-8') as outfile:
        for message in messages:
            # メッセージの前後の空白を削除
            message = message.strip()
            # メッセージをファイルに書き込む
            outfile.write(f"- {message}\n")
    
    return output_filepath

# ファイルパスを指定して関数を実行
filepath =  r"/mnt/c/Users/iniad/Downloads/Hyperliquid.txt"
output_filepath = extract_messages(filepath)
print(f"メッセージが抽出されたファイルのパス: {output_filepath}")


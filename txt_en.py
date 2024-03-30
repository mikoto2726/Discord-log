
import re

def extract_messages_without_emojis_or_urls(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # メッセージの本文を抽出する正規表現パターン
    pattern = r"\[\d{4}/\d{2}/\d{2} \d{2}:\d{2}\] .+?\n(.+?)(?=\n\[|\Z)"
    messages = re.findall(pattern, content, re.DOTALL)
    
    # 絵文字やURLを除外するための正規表現パターン
    emoji_pattern = r":[a-zA-Z0-9_]+:"  # 絵文字をコロンで囲まれたテキストとして仮定
    url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    
    # 抽出したメッセージを新しいファイルに書き込む
    output_filepath = r"/mnt/c/Users/iniad/Downloads/new_Hyperliquid2.txt"
    with open(output_filepath, 'w', encoding='utf-8') as outfile:
        for message in messages:
            # 絵文字とURLを除去
            message_cleaned = re.sub(emoji_pattern, '', message)
            message_cleaned = re.sub(url_pattern, '', message_cleaned)
            # メッセージの前後の空白を削除
            message_cleaned = message_cleaned.strip()
            # メッセージをファイルに書き込む
            if message_cleaned:  # 空のメッセージは除外
                outfile.write(f"- {message_cleaned}\n")
    
    return output_filepath

# ファイルパスを指定して関数を実行
filepath = r"/mnt/c/Users/iniad/Downloads/Hyperliquid.txt"
output_filepath = extract_messages_without_emojis_or_urls(filepath)
print(f"絵文字や特別な記号を含まないメッセージが抽出されたファイルのパス: {output_filepath}")

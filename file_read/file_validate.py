from typing import Optional
import sys


def file_read(path: str) -> str:
    r = open(path)
    text = r.read()
    r.close()
    return text


def validate(text: str, max_length: int) -> Optional[str]:
    text_len = len(text)

    if text_len == 0:
        return "ファイルが空"

    if text_len <= max_length:
        return None

    return "長すぎ"


def get_args():
    return sys.argv[1:]


def main():
    args = get_args()
    path = args[0]
    max_length = int(args[1])

    text = file_read(path)

    error = validate(text, max_length)

    if error is None:
        print("OK!!")
    else:
        print("あかんやつや：" + error)


main()
"""
TODO

- pathが存在しない場合
- pyinstaller
"""

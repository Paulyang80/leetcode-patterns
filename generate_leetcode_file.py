#!/usr/bin/env python3

import os
import re

def leetcode_title_to_filename(title: str) -> str:
    """
    將 LeetCode 題目標題轉為檔案名稱（小寫、底線、去除標點與多餘空白）
    例如：
    '80. Remove Duplicates from Sorted Array II'
    -> '80_remove_duplicates_from_sorted_array_ii.py'
    """
    title = title.strip()
    match = re.match(r"(\d+)\.\s*(.*)", title)
    if not match:
        raise ValueError("標題格式錯誤，需包含題號與標題")
    num, name = match.groups()
    name = re.sub(r"[^a-zA-Z0-9 ]", " ", name)
    name = re.sub(r"\s+", "_", name.strip().lower())
    return f"{num}_{name}.py"

def create_leetcode_file(title: str, folder: str = "arrays"):
    """
    根據 LeetCode 題目標題自動生成對應的 Python 檔案。

    Args:
        title (str): LeetCode 題目標題，例如 "80. Remove Duplicates from Sorted Array II"
        folder (str): 檔案存放的資料夾，預設為 "arrays"
    """
    filename = leetcode_title_to_filename(title)
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        print(f"{path} 已存在")
        return
    with open(path, "w") as f:
        f.write("from typing import List\n\nclass Solution:\n    pass\n")
    print(f"已建立 {path}")

if __name__ == "__main__":
    title = input("請輸入 LeetCode 題目標題：\n")
    create_leetcode_file(title)

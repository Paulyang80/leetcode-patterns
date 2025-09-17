# 測試說明與自動產生 test file 教學

## 如何執行測試

1. 安裝 pytest（如尚未安裝）：
   ```sh
   pip install pytest
   ```
2. 在專案根目錄下執行：
   ```sh
   pytest test/
   ```
   或直接執行單一檔案：
   ```sh
   pytest test/test_88_merge_sorted_array.py
   ```

## 如何自動產生 LeetCode 題目的 test file？

你可以用如下 prompt 輸入給 Copilot 或 AI 助手：

```
import importlib

S = importlib.import_module("{題目資料夾}.{題目檔案名無副檔名}").Solution()

def test_basic():
    # 請根據題目設計一組基本測資
    assert S.{方法名}(...) == ...

def test_edge_case():
    # 請根據題目設計一組邊界測資
    assert S.{方法名}(...) == ...

# 可依需求增加更多測資
```

### 產生 test file 的範例 prompt

```
可以幫我依照這題寫一個 test file 嗎？（請參考 test/test_88_merge_sorted_array.py 的格式）
```

---

- 測試檔請統一放在 `test/` 資料夾下。
- 檔名建議為 `test_題號_題目英文名.py`。
- 若原始檔案名稱有數字開頭，請用 importlib.import_module 方式匯入。

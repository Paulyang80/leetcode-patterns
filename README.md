# LeetCode Patterns (Top 150 & Beyond)

My Leetcode Account: https://leetcode.com/u/paulyang80/

把零散刷題轉成「題型手冊」：每個資料夾代表一類題型，包含：
- **summary.md**：題型套路、常見變化、解題模板、易錯點
- **solutions/**：代表性題目的參考解（Python / C++），以「題號_題名」命名

> 目標：**先建立模板，再混合訓練**。面試前可快速翻閱整體思路，而非只看單題。

---

## 目錄（持續更新）
- `arrays/`：Two Pointers、Sliding Window、Prefix Sum
- `hashmap/`：Counting、去重、映射
- `binary-search/`：基礎 BS、答案域 BS、左右邊界
- `linked-list/`：反轉、快慢指針、相交
- `stack-queue/`：單調棧、最小棧、括號類
- `tree/`：DFS/BFS、遍歷、BST 性質
- `graph/`：拓撲排序、最短路、聯通分量
- `dp/`：一維 DP、區間 DP、狀態壓縮
- `math/`：位運算、數學技巧
- `misc/`：設計題、系統類（若需要）

> 你也可以用「Top 150 原分類」建資料夾，這份是依 **解法套路** 分類。

---

## 使用方式
1. 遇到新題 → 找到對應題型資料夾
2. 在 `solutions/` 新增解答檔（`<id>_<slug>.py` 或 `.cpp`）
3. 在 `summary.md` 補題目一行紀錄（思路 1–2 句 + 複雜度）
4. 每週整理一個題型的 **模板 & 易錯點**

---

## 命名規則
- 檔名：`<id>_<slug>.<py|cpp>` 例：`001_two_sum.py`
- 函式：Python 預設 `class Solution: ...`
- 註解：最上方 3 行寫 **思路 / 複雜度 / 易錯點**

---

## 推薦練法
- **先集中**：一週一題型（建立模板）
- **再混合**：面試前兩週打散刷題（模擬真實場景）
- 追蹤：在每個 `summary.md` 裡用 `- [x]` 勾已完成

---

## 進度（示例）
- Arrays：8 / 15  
- HashMap：6 / 10  
- Binary Search：5 / 9  
- DP：12 / 20  
（自行更新或用 GitHub Project 自動化）

---

## 環境
僅放程式碼與 Markdown；本 repo **不提交** 個人 venv 或快取檔。


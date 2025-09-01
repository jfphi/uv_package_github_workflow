### 範例 uv 專案

這是一個使用 uv 管理的最小可執行 Python 專案範例。

### 需求

- 已安裝 `uv`（安裝方式請參考官方文件 `https://docs.astral.sh/uv/`）
- Python 3.9 以上

### 專案結構

```
example/
  ├─ pyproject.toml
  ├─ README.md
  ├─ .gitignore
  ├─ src/
  │  └─ uv_example/
  │     ├─ __init__.py
  │     └─ cli.py
  └─ tests/
     └─ test_cli.py
```

### 快速開始

```bash
cd example
uv sync
uv run uv-example --name UV
uv run pytest -q
```

### 常用指令

- **新增相依套件**:
  ```bash
  uv add requests
  ```
- **移除相依套件**:
  ```bash
  uv remove requests
  ```
- **執行 linters / type-checkers**:
  ```bash
  uv run ruff check .
  uv run mypy src
  ```

### 發佈建置（選用）

```bash
uv build
```




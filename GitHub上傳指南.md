# GitHub 上傳指南

## 步驟 1: 在 GitHub 上創建新倉庫

1. 登錄到你的 GitHub 帳戶
2. 點擊右上角的 "+" 圖標，選擇 "New repository"
3. 在 "Repository name" 欄位中輸入 "Flask專案學習步驟指南"
4. 可以選擇添加描述（可選）
5. 選擇倉庫可見性（公開或私有）
6. 不要初始化倉庫（不要勾選 "Initialize this repository with a README"）
7. 點擊 "Create repository" 按鈕

## 步驟 2: 將本地倉庫推送到 GitHub

在你的本地終端中執行以下命令：

```bash
# 添加遠程倉庫
git remote add origin https://github.com/你的用戶名/Flask專案學習步驟指南.git

# 推送到 GitHub
git push -u origin master
```

如果你使用的是 SSH 而不是 HTTPS，則命令為：

```bash
git remote add origin git@github.com:你的用戶名/Flask專案學習步驟指南.git
git push -u origin master
```

## 步驟 3: 驗證上傳

1. 刷新你的 GitHub 倉庫頁面
2. 確認所有文件都已成功上傳
3. 檢查 README.md 是否正確顯示

## 常見問題解決

### 如果你遇到身份驗證問題：

#### 使用 HTTPS：
```bash
# 使用個人訪問令牌（PAT）進行身份驗證
git remote set-url origin https://你的用戶名:你的訪問令牌@github.com/你的用戶名/Flask專案學習步驟指南.git
```

#### 使用 SSH：
確保你已經設置了 SSH 密鑰：
```bash
# 檢查現有的 SSH 密鑰
ls -al ~/.ssh

# 如果需要，生成新的 SSH 密鑰
ssh-keygen -t ed25519 -C "your.email@example.com"

# 將 SSH 密鑰添加到 GitHub 帳戶
# 複製公鑰內容
cat ~/.ssh/id_ed25519.pub
# 然後在 GitHub 設置中添加這個密鑰
```

### 如果你遇到分支名稱問題：

如果你的默認分支是 `main` 而不是 `master`：
```bash
git push -u origin main
```

或者重命名本地分支：
```bash
git branch -M main
git push -u origin main
```

## 後續操作

成功上傳後，你可以：

1. 設置 GitHub Pages 來展示你的專案（如果需要）
2. 添加協作者（如果是團隊專案）
3. 設置分支保護規則
4. 配置 GitHub Actions 進行自動化測試和部署
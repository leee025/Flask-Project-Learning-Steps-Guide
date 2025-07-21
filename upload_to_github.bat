@echo off
echo 正在上傳專案到 GitHub...

set /p username="請輸入你的 GitHub 用戶名: "

echo 添加遠程倉庫...
git remote add origin https://github.com/%username%/Flask-Project-Learning-Steps-Guide.git

echo 設置主分支...
git branch -M main

echo 推送到 GitHub...
git push -u origin main

echo 完成！請檢查你的 GitHub 倉庫。
pause
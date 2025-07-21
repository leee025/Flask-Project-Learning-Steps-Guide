@echo off
echo 正在準備上傳專案到 GitHub...

echo 請輸入你的 GitHub 用戶名:
set /p username=leee025

echo 添加遠程倉庫...
git remote add origin https://github.com/%username%/Flask專案學習步驟指南.git

echo 推送到 GitHub...
git push -u origin master

echo 完成！請檢查你的 GitHub 倉庫。
pause
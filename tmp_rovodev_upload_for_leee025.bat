@echo off
echo ========================================
echo  上傳 Flask 專案到 GitHub
echo  用戶: leee025
echo  倉庫: Flask-Project-Learning-Steps-Guide
echo ========================================

echo.
echo 步驟 1: 檢查 Git 狀態...
"C:\Program Files\Git\bin\git.exe" status

echo.
echo 步驟 2: 添加所有文件到 Git...
"C:\Program Files\Git\bin\git.exe" add .

echo.
echo 步驟 3: 提交更改...
"C:\Program Files\Git\bin\git.exe" commit -m "Initial commit: Flask Project Learning Steps Guide"

echo.
echo 步驟 4: 設置主分支為 main...
"C:\Program Files\Git\bin\git.exe" branch -M main

echo.
echo 步驟 5: 添加遠程倉庫...
"C:\Program Files\Git\bin\git.exe" remote add origin https://github.com/leee025/Flask-Project-Learning-Steps-Guide.git

echo.
echo 步驟 6: 推送到 GitHub...
"C:\Program Files\Git\bin\git.exe" push -u origin main

echo.
echo ========================================
echo  上傳完成！
echo  你的倉庫位於: 
echo  https://github.com/leee025/Flask-Project-Learning-Steps-Guide
echo ========================================
echo.
pause
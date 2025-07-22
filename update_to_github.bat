@echo off
echo Staging changes...
git add .

echo Committing changes...
git commit -m "Update files"

echo Pushing to GitHub...
git push

echo.
echo Update complete.
pause

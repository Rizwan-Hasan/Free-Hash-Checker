@echo off

rmdir /s /q "build"
rmdir /s /q "dist"
del /s /q "Free Hash Checker.spec"

pyinstaller -y ^
--windowed ^
--onedir ^
--clean ^
--noupx ^
--name "Free Hash Checker" ^
--icon "./logo/icon.ico" ^
--add-data "./ui";"./ui/" ^
--add-data "./resources_rc.py";"." ^
--add-data "LICENSE";"." ^
--hidden-import "requests" ^
--version-file "version-file.txt" ^ "./AppRun.py"

rmdir /s /q "build"
del /s /q "Free Hash Checker.spec"
rmdir /s /q "dist\\Free Hash Checker\\ui\\__pycache__"
del /s /q "dist\\Free Hash Checker\\ui\\"*.png
del /s /q "dist\\Free Hash Checker\\ui\\"*.qrc
del /s /q "dist\\Free Hash Checker\\ui\\"*.ui
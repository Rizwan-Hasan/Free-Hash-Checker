@echo off

rmdir /s /q "build"
rmdir /s /q "dist"
rmdir /s /q "__pycache__"
rmdir /s /q "ui/__pycache__"

pyinstaller -y ^
--console ^
--name "Free-Hash-Checker" ^
--icon "logo/icon.ico" ^
--add-data "ui";"ui/" ^
--add-data "app.py";"." ^
--add-data "hashcalc.py";"." ^
--add-data "infoManager.py";"." ^
--add-data "LICENSE";"." ^
--add-data "resources_rc.py";"." ^
--add-data "updateManager.py";"." ^
--hidden-import "requests" ^
--version-file "version-file.txt" ^ "AppRun.py" ^
--clean

rmdir /s /q "build"
rmdir /s /q "__pycache__"
rmdir /s /q "ui/__pycache__"
del /s /q "dist\\Free-Hash-Checker\\ui\\"*.png
del /s /q "dist\\Free-Hash-Checker\\ui\\"*.qrc
del /s /q "dist\\Free-Hash-Checker\\ui\\"*.ui
del /s /q "dist\\Free-Hash-Checker\\ui\\__init__.py"
pause
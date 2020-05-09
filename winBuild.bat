@echo off

rmdir /s /q "build"
rmdir /s /q "dist"
del /s /q "Free-Hash-Checker.spec"

pyinstaller -y ^
--console ^
--name "Free-Hash-Checker" ^
--icon "freeHashChecker/logo/icon.ico" ^
--add-data "freeHashChecker/ui";"freeHashChecker/ui/" ^
--add-data "freeHashChecker/resources_rc.py";"." ^
--add-data "LICENSE";"." ^
--hidden-import "requests" ^
--version-file "version-file.txt" ^ "freeHashChecker/AppRun.py" ^
--clean

rmdir /s /q "build"
del /s /q "Free-Hash-Checker.spec"
rmdir /s /q "dist\\Free-Hash-Checker\\freeHashChecker\\ui\\__pycache__"
del /s /q "dist\\Free-Hash-Checker\\freeHashChecker\\ui\\"*.png
del /s /q "dist\\Free-Hash-Checker\\freeHashChecker\\ui\\"*.qrc
del /s /q "dist\\Free-Hash-Checker\\freeHashChecker\\ui\\"*.ui
del /s /q "dist\\Free-Hash-Checker\\freeHashChecker\\ui\\__init__.py"
pause
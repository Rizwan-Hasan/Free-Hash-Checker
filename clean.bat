@echo off

rmdir /s /q "build"
rmdir /s /q "dist"
rmdir /s /q "__pycache__"
rmdir /s /q "freeHashChecker/__pycache__"
rmdir /s /q "freeHashChecker/ui/__pycache__"
del /s /q "Free-Hash-Checker.spec"
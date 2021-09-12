rm -rf "build"
rm -rf "dist"
rm -rf "Free Hash Checker.spec"

pyinstaller -y \
    --console \
    --onedir \
    --clean \
    --name "Free Hash Checker" \
    --icon "./logo/icon.ico" \
    --add-data ./"ui":./"ui/" \
    --add-data ./"resources_rc.py":./"." \
    --add-data ./"LICENSE":./"." \
    --hidden-import "requests" \
    --version-file "version-file.txt" "./AppRun.py"

rm -rf "build"
rm -rf "Free Hash Checker.spec"
rm -rf "dist/Free Hash Checker/ui/__pycache__"
rm -rf "dist/Free Hash Checker/ui/"*.png
rm -rf "dist/Free Hash Checker/ui/"*.qrc
rm -rf "dist/Free Hash Checker/ui/"*.ui

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['freeHashChecker\\AppRun.py'],
             pathex=['C:\\Users\\Rizwan\\PycharmProjects\\Free-Hash-Checker'],
             binaries=[],
             datas=[('freeHashChecker/ui', 'freeHashChecker/ui/'), ('freeHashChecker/resources_rc.py', '.'), ('LICENSE', '.')],
             hiddenimports=['requests'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Free-Hash-Checker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , version='version-file.txt', icon='freeHashChecker\\logo\\icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Free-Hash-Checker')

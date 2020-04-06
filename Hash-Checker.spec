# -*- mode: python -*-

block_cipher = None


a = Analysis(['AppRun.py'],
             pathex=['D:\\Downloads\\Free-Hash-Checker'],
             binaries=[],
             datas=[('ui', 'ui/'), ('app.py', '.'), ('hashcalc.py', '.'), ('infoManager.py', '.'), ('LICENSE', '.'), ('resources_rc.py', '.'), ('updateManager.py', '.')],
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
          name='Hash-Checker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , version='version-file.txt', icon='logo\\icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Hash-Checker')

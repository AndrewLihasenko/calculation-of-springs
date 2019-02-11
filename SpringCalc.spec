# -*- mode: python -*-

block_cipher = None


a = Analysis(['calc.py'],
             pathex=['E:\\Program\\Python\\Projects\\PyQt5\\Calculation_of_springs'],
             binaries=[],
             datas=[('spring_resize.png', '.'), ('icon.png', '.'), ('OST_1_13553-79-Spring_2A.TIF', '.')],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='SpringCalc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )

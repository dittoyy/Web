#coding=utf-8
from distutils.core import setup
import py2exe
import glob

#python setup.py py2exe --includes sip     图标要手动复制图片到dist文件夹去

setup(
# targets to build
    windows = [{"script":"dysyui.py", "icon_resources": [(1, "logo1.ico")]} ],
    options = { "py2exe":{"dll_excludes":["MSVCP90.dll"],"bundle_files": 3,}},
    data_files = [("imageformats",glob.glob("C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\*.dll"))]
)
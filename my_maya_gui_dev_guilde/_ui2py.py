# coding:utf-8
# convert *.ui to *_ui.py (using PySide2 （>= Maya2018）)
# jason.li@neobards.cn | 2019.08.01


import os
import sys
# default using Maya2018 compile ui to py
# sys.path.append（r'C:\Program Files\Autodesk\Maya2018\Python\Lib\site-packages')
try:
    from pyside2uic import compileUi
    print('compileUi for PySide2')
except:
    from pysideuic import compileUi     # PySide (Maya2014~2016)
    print('compileUi for PySide')

import Qt


# ----------------------------------------------------------------------
def ui2py(uifile):
    """"""
    pyfilename = '_'.join(uifile.rsplit('.', 1)) + '.py'
    with open(pyfilename, 'w') as pyfile:
        compileUi(uifile, pyfile)
        print('compile ui to py done -> %s' % pyfilename)
    return pyfilename


def convert(py_uifile):
    Qt._cli(['--convert', py_uifile])
    print('convert py_uifile for PySide & PySide2 done')



# ----------------------------------------------------------------------
def main():
    """"""
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        for f in files:
            try:
                py = ui2py(f)
                convert(py)
            except Exception as ex:
                print(ex.message)
                


if __name__ == '__main__':
    main()
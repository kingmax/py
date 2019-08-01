# coding:utf-8
# maya script tool with gui dev guide description, test in maya2016~2019
# jason.li@neobards.cn | 2019.08.01

desc = '''
0.request: Qt.py, _ui2py.py, lib.py, _win_template.py
1.using Qt Designer          -> xxx.ui
2.using _ui2py               -> xxx_ui.py (with convert for PySide2 and PySide)
3.copy _win_template.py      -> xxx.py
4.in xxx.py implement functions
5.in maya usage:

#coding:utf-8
from NB2 import xxx
reload(xxx)
xxx.main()

'''

print(desc)
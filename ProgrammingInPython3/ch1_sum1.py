#!/usr/bin/env python3
#coding:utf-8
"""
  Author:  kingmax_res@163.com
  Purpose: Programming In Python3 Example | chapter 1
  Created: 10/03/20
"""

print('Type integers, each followed by Enter or just Enter to finish')
total = 0
count = 0


while True:
    line = input('integer: ')
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        total += number
        count += 1
    else:
        break
    

if count:
    print(f'count={count}, total={total}, mean={total/count}')



def main(*args, **kwargs):
    """"""
    pass


if __name__ == '__main__':
    main()
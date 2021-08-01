#!/usr/bin/env python3
#coding:utf-8
"""
  Author:  kingmax_res@163.com
  Purpose: Programming In Python3 Example | chapter 1 | sum2, input can using file
  Created: 10/04/20
"""

print('Type integers, each followed by Enter; or ^D or ^Z to finish')

total = 0
count = 0

while True:
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break
    
if count:
    print(f'count={count}, total={total}, mean={total/count}')



def main(*args, **kwargs):
    """"""
    pass


if __name__ == '__main__':
    main()
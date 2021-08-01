print('type some integers:')

total = 0
count = 0

while 1:
    try:
        line = input('input integer:(end with enter, enter q to exit): ')
        #if line.lower() == "q":
            #break
        
        n = int(line)
        total += n
        count += 1
    except Exception as ex:
        #print(ex)
        break

        
if count:
    print(f'total={total}, count={count}, mean={total/count}')
    
    
num = int(input())
bul = True
for subtract in range(2,num):
    if num % subtract == 0:
        print('False')
        bul = False
        break
if bul and num > 1 :
    print('True')
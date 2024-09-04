aray = [
        [0,1,2],
        [3,4,5],
        [6,7,8]
]
ar = []
print(aray)
def Enterdata():
    for i in range(len(aray)):
        ar.append([])
        for j in range(len(aray[i])):
            x = int(input("Nhap phan tu :"))
            ar[i].append(x)
Enterdata()
print(ar)


def Seach(ar, aray):
    positions = []
    
    # Duyệt qua từng phần tử của mảng 2 chiều array1
    for i1 in range(len(ar)):
        for j1 in range(len(ar[i1])):
            element = ar[i1][j1]
            found = False
            for i2 in range(len(aray)):
                for j2 in range(len(aray[i2])):
                    if i1==i2 and j1==j2 and aray[i2][j2] == element :
                        break
                    else:
                        if aray[i2][j2] == element:
             
                            print(f"{ar[i1][j1]} can co {abs(i2-i1)+abs(j2-j1)}")
                            found = True
                            break
                    if found:
                     break
         


Seach(ar, aray)

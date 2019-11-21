x = 1000000000
sum=0
y=0
gaji = [int(0), int(0), int(x) * .1, int(x) * .1, int(x) * .5, int(x) * .5, int(x) * .5, int(x) * .2]
print("Modal awal pengusaha:", x)
for i in gaji :
    sum = sum+i
    y+=1
    print("gaji bulan ke-",y,"sebesar:", i)
print("Total gaji adalah:", sum)
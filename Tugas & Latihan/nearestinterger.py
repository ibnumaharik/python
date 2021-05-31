##Ibnu Maharik 411201154
def Number(n, m) :

    a = int(n / m)
     
    n1 = m * a
     
    if((n * m) > 0) :
        n2 = (m * (a + 1))
    else :
        n2 = (m * (a - 1))
     
    if (abs(n - n1) < abs(n - n2)) :
        return n1
     
    return n2
     
n = int(input('Masukan Angka :')) 
m = int(input('Masukan Angka :'))
print(Number(n, m))
 

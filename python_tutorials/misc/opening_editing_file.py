for i in range (20):
    f1=open('test.inp', 'r')
    extinp = f1.readlines()
    f1.close()
    extinp[13] = 'set s %d\n'%(i+1)
    print extinp[13]
    f11=open('test.inp', 'w')
    f11.writelines(extinp)
    f11.close()    

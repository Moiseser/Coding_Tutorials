#Loop created for testing writing merge file for T4 discs 
# m=1
# k=12
# for j in range(Discs):
#     #print j 
#     print k
#     if radius[j,0]<midpoint:
#         f44=open('merge.inp','r')
#         xx = f44.readlines()
#         xx[k] = 'read psf xplor card name structures/ext_disc.psf\n'
#         xx[k+1] = 'read coor card name structures/disc%d.crd\n'%(m)
#         f44=open('merge.inp', 'w')
#         f44.writelines(xx)
#         m+=1
#         k+=2
# f44=open('merge.inp', 'r')
# xx = f44.readlines()
# f44.close()
# xx[k] = 'set frame %d\n write psf xplor card name Time_Frame@{frame}.psf\n write coor pdb card name Time_Frame@{frame}.pdb\n stop'%(1)
# f44=open('merge.inp', 'w')
# f44.writelines(xx)
# f44.close()

#File which called orignal charmm merge disc script which just looped over discs if they were all the same ext or con 
# f33=open('merge.inp', 'r')
# movie_frame = f33.readlines()
# f33.close()
# movie_frame[29] = 'set frame %d\n'%(1)
# f33=open('merge.inp', 'w')
# f33.writelines(movie_frame)
# f33.close()
# sh.call('charmm <merge.inp >job2.out', shell=True)

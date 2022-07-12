import matplotlib
import numpy as np
import matplotlib.pyplot as plt

listax=[]
listay=[]
j=0
i=0
while i<20:
    listax.append(i)
    i=i+1
while j<20:
    listay.append(j*2)
    j=j+1    
xx=np.array(listax)
yy=np.array(listay) 
################  BARRE ##############
plt.barh(xx,yy,height=0.7)
plt.show()

# plt.scatter(xx,yy,color='g')

# listax2=[]
# listay2=[]
# p=0
# q=0
# while p<20:
#     listax2.append(p+5)
#     p=p+1
# while q<20:
#     listay2.append((q+3)*2)
#     q=q+1    
# xx2=np.array(listax2)
# yy2=np.array(listay2) 

# plt.scatter(xx2,yy2,color='yellow')
# plt.show()

# font1={'family':'serif','color':'red','size':20}
# font2={'family':'serif','color':'b','size':15}
# font3={'family':'serif','color':'brown','size':15}
####################  SUBPLOT  ############################
# plt.subplot(1,2,1)
# plt.plot(xx,yy,'D:y')
# plt.title("Esplodo",fontdict=font1)
# plt.xlabel("Cose",fontdict=font2)
# plt.ylabel("A Caso",fontdict=font3)
# plt.grid(color='blue',linestyle='--',linewidth=1)

# plt.subplot(1,2,2)
# plt.plot(xx,yy,'D:y')
# plt.title("Esplodo",fontdict=font1)
# plt.xlabel("Cose",fontdict=font2)
# plt.ylabel("A Caso",fontdict=font3)
# plt.grid(color='blue',linestyle='--',linewidth=1)

# plt.suptitle('Absurd',color='green',size=20)


# plt.show() 
# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.randint(100, size=(100))
# sizes = 10 * np.random.randint(100, size=(100))
#################### SCATTER #############################
# plt.scatter(x, y,c=colors, s=sizes, alpha=0.6, cmap='nipy_spectral')

# plt.colorbar()

# plt.show()
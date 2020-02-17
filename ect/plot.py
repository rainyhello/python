# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:54:52 2020
@author: Tsinghua
下面是成图算法
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit
 
 
excel = 'E:/log/data_process.xlsx'
save_path='E:/log/picture/'
df = pd.read_excel(excel)
 
#a=['21','29','51','81','150','297','394','583','708','1057','1430']
d=np.array([22,29,51,81,150,297,394,583,708,1057,1430])
b=list(range(1,12))
c=list(range(1,29))
 
#da = pd.DataFrame(columns=a,index=b)
#da = pd.DataFrame(columns=b,index=a)
 
for j in range(0,9):
    ss = np.zeros([28,0])
#取出Excel中某些行
    for i in range(0,11):
        dd = pd.DataFrame(df.ix[4+j*11+i,2:30],dtype=np.float)
        ss = np.append(ss,dd.values,1)

#    ss = np.transpose(ss)#矩阵转置
#    每个电容的28通道图
    plt.figure(figsize=(12,8), dpi=100)#设置画板大小
    plt.figure(1)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=0.3, hspace=None)

    for i in range(0,11):
        plt.subplot(3,4,i+1)
        plt.plot(c,ss[:,i])     #斜率成图
    
    plt.savefig(save_path+'板卡'+str(j)+'电容'+'.png')
#   plt.show()
#   plt.clf()
# =============================================================================
# #    每个通道的散点图前面10个点
#     plt.figure(figsize=(28,16), dpi=100)#设置画板大小
#     plt.figure(1)
#     plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
#                 wspace=0.3, hspace=None)
#     
#     for i in range(0,28):
#         plt.subplot(7,4,i+1)
#         plt.plot(d[:],ss[i,:])
#         
#     plt.savefig(save_path+'板卡'+str(j)+'.png')
#     plt.show()
#     plt.clf()
# =============================================================================
#去除最大电容后的成图，前10个电容线性度会更好一些
    plt.figure(figsize=(28,16), dpi=100)#设置画板大小
    plt.figure(2)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.3, hspace=None)
    for i in range(0,28):
        plt.subplot(7,4,i+1)
        plt.plot(d[:9],ss[i,:9])
        
    plt.savefig(save_path+'无'+str(j)+'通道'+'.png')
#    plt.show()
#    plt.clf()
#==============================================================================
    pp = np.array([])
    pp1 = np.zeros(shape=(28,1))
    pp2 = np.zeros(shape=(28,1))
    
    for i in range(0,28):
        ploy = np.polyfit(ss[i,0:10],d[0:10],deg=1)#只拟合前面10个电容
        pp = np.append(pp,ploy,0)#得到拟合方程的两个参数，前面是斜率，后面的偏移量
#       plt.plot(e,np.polyval(ploy,e))
#       plt.plot(list(range(0,28)),pp)
        
    for i in range(0,28):
        pp1[i] = pp[2*i]    #这个是斜率
        pp2[i] = pp[2*i+1]  #偏移量

    plt.figure(figsize=(10,10), dpi=100)#设置画板大小
    plt.figure(3)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.3, hspace=None)
    plt.subplot(3,3,j+1)
    plt.plot(list(range(0,28)),pp1)     #斜率成图
    plt.savefig(save_path+'EMB'+'斜率'+'.jpg')
    
    
    plt.figure(figsize=(10,10), dpi=100)#设置画板大小
    plt.figure(4)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.3, hspace=None)
    plt.subplot(3,3,j+1)
    plt.plot(list(range(0,28)),pp2)     #偏移量成图    
    plt.savefig(save_path+'EMB'+'偏移'+'.jpg')

#plt.show()
#plt.clf()

#保存的时候遇到过保存空白图像的问题，
#是因为将plt.savefig('D:/log/picture/i+5.png')放到了plt.show()之后，
#只要先保存在显示就可以正常保存了。

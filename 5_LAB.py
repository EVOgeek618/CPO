#!/bin/python3
from web3 import Web3
import time
import matplotlib.pyplot as plt
TX=[]
ETH=[]
d=0
"""web3=Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/e518cfd0c7844d3e894f06128a8d539a"))
list1=range(8958400,8959401)
print(web3.eth.gasPrice)
for i in list1:
		try:
			d+=1
			blockTran=web3.eth.getBlock(i).transactions
			e=0	
			EX=[]
			for t in range(len(blockTran)):
				try:
					Tran=web3.eth.getTransaction(blockTran[t])
					print(d,"-",t)
					e+=((Tran.gasPrice*Tran.gas)/1e18)
					EX.append((Tran.gasPrice*Tran.gas)/1e18)
				except:
					t-=2
					for s in range(60):
						print("\r"+str(s+1), end="")
						time.sleep(1)
					print("\n")
			TX.append(e)
		except:
			i-=1
			for s in range(60):
				print("\r"+str(s+1), end="")
				time.sleep(1)
with open ("TX.txt","w") as T:
	for j in range(1001):
		T.write(str(list1[j])+" "+str(TX[j])+"\n")
	T.close()"""
with open ("TX.txt","r") as T:
	for j in T.readlines():
		ETH.append(j[:-1].split(" "))
	T.close()
x=[]
y=[]
y2=[]
mo,sad=0,0
for i in ETH:
	com=float(i[1])
	block=int(i[0])
	x.append(block)
	y.append(com)
	y2.append((com/(com+2))*100)
	mo+=com*1/1001
	sad+=(com**2)*1/1001
fig, ax=plt.subplots()
ax.bar(x,y)
fig2, ax2=plt.subplots()
ax2.bar(x,y2)
y.sort()
print("Медиана:",y[500])
print("Матожидание:",mo)
print("Размах:",y[-1]-y[0])
print("Дисперсия:",sad-mo*mo)
print("Среднеквадротичное отклонение:",(sad-mo*mo)**0.5)
plt.show()

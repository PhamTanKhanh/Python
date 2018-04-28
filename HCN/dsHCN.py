from classHCN import HCN	
n=input("Nhap so HCN: ")
hcn=[]
for i in range(0,n):
	ten=input("nhap ten: ")
	dai=input("nhap chieu dai: ")
	rong=input("nhap chieu rong: ")
	h = HCN(ten,dai,rong)
	hcn.append(h)

for i in hcn:
	cv=i.getCV()
	dt=i.getDT()
	print(i.toString()+" CV:"+str(cv)+" DT:"+str(dt))
	#print(str(cv))
	#print(str(dt))

dtmax = hcn[0].getDT()



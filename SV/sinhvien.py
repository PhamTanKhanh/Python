class SinhVien:
	Ten=""
	NamSinh=""
	Khoa=""
	def __init__(self,Ten,NamSinh,Khoa):
		self.Ten=Ten
		self.NamSinh=NamSinh
		self.Khoa=Khoa

	def setTen(self,Ten):
		self.Ten=Ten

	def getTen(self):
		return self.Ten

	def setNS(self,NamSinh):
		self.NamSinh=NamSinh

	def getNS(self):
		return self.NamSinh

	def setKhoa(self,Khoa):
		self.Khoa=Khoa

	def getKhoa(self):
		return self.Khoa

	def toString(self):
		print("Ho ten: "+str(self.Ten)+"\nNam Sinh: "+str(self.NamSinh)+"\nKhoa: "+str(self.Khoa))


class Infor:
    def __init__(self,ten,ngay,sdt) -> None:
          ds = ten.split()
          self.s = ds[-1]
          self.ss = ds[:-1]
          self.ten = ten 
          self.ngay = ngay
          self.sdt = sdt
    def __str__(self) -> str:
        return f'{self.ten}: {self.sdt} {self.ngay}'

e=[]
with open('SOTAY.txt','r') as file:
    s = file.readline()
    ten=""
    ngay=""
    sdt=""
    while s:
        s=s.strip()
        if "Ngay" in s:
            ngay = s[5:]
        elif "0" in s:
            sdt = s
            e.append(Infor(ten,ngay,sdt))
        else: 
            ten = s
        s=file.readline()
e = sorted(e,key=lambda x: (x.s,x.ss))
# with open('DIENTHOAI.txt','w') as file:
#     for i in e:
#         file.write(i)
for i in e:
    print(i)
jinsu=int(input("입력 진수 결정(2,8,10,16)"))
su=(input("값 입력"))
if(jinsu == 16):
    su=int(su,16)
if(jinsu == 8):
    su=int(su,8)
if(jinsu == 10):
    su=int(su,10)
if(jinsu == 2):
    su=int(su,2)
a16jinsu = hex(su)
a10jinsu = su
a8jinsu = oct(su)
a2jinsu = bin(su)
print("16진수 =>", a16jinsu)
print("10진수 =>", a10jinsu)
print("8진수 =>", a8jinsu)
print("2진수 =>", a2jinsu)
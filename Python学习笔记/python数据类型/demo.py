a='neil'
b=20
print('我叫%s，今年%d岁了'%(a,b))
print('我叫{0}，今年{1}岁了'.format(a,b))
print(f"我叫{a}，今年{b}岁了")
print('{0:.3f}'.format(3.4959))
s='I am Neil'
#编码
byte=s.encode(encoding="GBK")
#解码
print(byte.decode(encoding="GBK"))
def fun(arg1,arg2):
    
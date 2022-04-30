#MiniAESpagina19tema2

# importar librerias de matematicas entera
from math import *



F.<xi>=GF(2^4,modulus=GF(2)[x](x^4+x+1))


F.modulus()

def nibblesub(ll):
    xx=vector(ll)
    if xx != 0:
        xx=vector(reversed(vector(F(vector(reversed(xx)))^(-1))))
    return list(xx*matrix(GF(2),4,[0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1])+vector([0,0,1,1]))

def shiftrow(ll):
    return [ll[0],ll[3],ll[2],ll[1]]

def mixcolumn(ll):
    return [list(reversed(vector(ele))) for ele in(matrix(F,2,[xi+1,xi,xi,xi+1])*matrix(F,2,[F(vector(reversed(ll[0]))),F(vector(reversed(ll[2]))),F(vector(reversed(ll[1]))),F(vector(reversed(ll[3])))])).transpose().list()]

def addroundkey(ll,kk):
    return [list(vector(ll[0])+vector(kk[0])),list(vector(ll[1])+vector(kk[1])),list(vector(ll[2])+vector(kk[2])),list(vector(ll[3])+vector(kk[3]))]
#CalculaK0,K1,K2

def keysquedule(kk):
    ww=list(reversed(vector(GF(2),kk.bits())))
#SiK0esmenorde16bit,serellenaconceros
    while len(ww)<16:
        ww=[GF(2)(0)]+ww
    #Calculamosk1,k2ylometemosenlalista
    ww=[[ww[0],ww[1],ww[2],ww[3]],[ww[4],ww[5],ww[6],ww[7]],[ww[8],ww[9],ww[10],ww[11]],[ww[12],ww[13],ww[14],ww[15]]]
    ww+=[list(vector(ww[0])+vector(nibblesub(ww[3]))+vector(GF(2),[0,0,0,1]))]#w4
    ww+=[list(vector(ww[1])+vector(ww[4]))]#w5
    ww+=[list(vector(ww[2])+vector(ww[5]))]#w6
    ww+=[list(vector(ww[3])+vector(ww[6]))]#w7
    ww+=[list(vector(ww[4])+vector(nibblesub(ww[7]))+vector(GF(2),[0,0,1,0]))]#w8
    ww+=[list(vector(ww[5])+vector(ww[8]))]#w9
    ww+=[list(vector(ww[6])+vector(ww[9]))]#w10
    ww+=[list(vector(ww[7])+vector(ww[10]))]#w11
    return ww
def MiniAES(kk,mm):
    ww=keysquedule(kk)#w0,w1,w2,w3,.....,w11
    #m[i]
    estado=list(reversed(vector(GF(2),mm.bits())))
    while len(estado)<16:
        estado=[GF(2)(0)]+estado
    estado=[[estado[0],estado[1],estado[2],estado[3]],[estado[4],estado[5],estado[6],estado[7]],[estado[8],estado[9],estado[10],estado[11]],[estado[12],estado[13],estado[14],estado[15]]]
    #YaaplicolafunciondeencriptarEk()--->MiniAes
    estado=addroundkey(estado,[ww[0],ww[1],ww[2],ww[3]])#XOR
    estado=[nibblesub(ele) for ele in estado]#GAMMA
    estado=shiftrow(estado)#PI
    estado=mixcolumn(estado)#O
    estado=addroundkey(estado,[ww[4],ww[5],ww[6],ww[7]])
    estado=[nibblesub(ele) for ele in estado]
    estado=shiftrow(estado)
    estado=addroundkey(estado,[ww[8],ww[9],ww[10],ww[11]])
    salida=list(reversed(estado[0]+estado[1]+estado[2]+estado[3]))
    return estado,Integer(salida,base=2).hex()

clave=49616461%(65536)

mensaje=list(0x01234567.bits())

#DividimosenbloquesdetamanoN=16
mens2=[1,1,1,0,0,1,1,0,1,0,1,0,0,0,1,0]
mens1=[1,1,0,0,0,1,0,0,1]+[0,0,0,0,0,0,0]
c0='0x0001'
c1='0x'+MiniAES(clave,Integer(mens1,base=2)^(Integer(c0)))[1]
c2='0x'+MiniAES(clave,Integer(mens2,base=2)^(Integer(c1)))[1]
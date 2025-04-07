országok = []
with open('EUcsatlakozas.txt', 'r', encoding='utf-8') as file:
    for sor in file:
        országok.append(sor.strip().split(';'))
    for ország in országok:
        ország[1]=ország[1].split('.')

def tagállam_18(tagállamok):
    számolo = 0
    for tagállam in tagállamok:
        if int(tagállam[1][0])<= 2018:
            számolo += 1
    print(számolo)

def _2007ben_csat(országok):
    szakolo = 0
    for ország in országok:
        if ország[1][0] == '2007':
            szakolo += 1
    print(szakolo)

def magy_cst(országok):
    for ország in országok:
        if ország[0] == 'Magyarország':
            print(*ország[1], sep='-')

def májusi_csat(országok):
    for ország in országok:
        if ország[1][1] == '05':
            print('volt májusi csatlakozás')
            return
    print('nem volt májusi csatlakozás')

def utolsó(országok):
    utolsó = országok[0]
    for ország in országok:
        if int(ország[1][0]) > int(utolsó[1][0]):
            utolsó = ország
        elif int(ország[1][0]) == int(utolsó[1][0])  and int(ország[1][1]) > int(utolsó[1][1]):
            utolsó = ország
        elif int(ország[1][0]) == int(utolsó[1][0]) and int(ország[1][1]) == int(utolsó[1][1]) and int(ország[1][2]) > int(utolsó[1][2]):
            utolsó = ország
    print(utolsó[0])
 
def átlag (országok):
    átlag = {}
    for ország in országok:
        if ország[1][0] not in átlag:
            átlag[ország[1][0]] = 1
        else:
            átlag[ország[1][0]] += 1
    print(átlag)

tagállam_18(országok)
_2007ben_csat(országok)
magy_cst(országok)
májusi_csat(országok)
utolsó(országok)
átlag(országok)
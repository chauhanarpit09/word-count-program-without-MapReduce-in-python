#%%
import re
file = open("file.txt","r")

l = file.read()
l = re.sub("[:,.?()#$]","",l).split()

d = {}
for i in l:
    if i in d.keys():
        d[i] = d[i]+1
    else:
        d[i] = 1
for k,v in d.items():
    print(k , " ",v," times" )

file.close()


# %%

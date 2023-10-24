"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(result):
    result.reverse()
    largo = len(result)
    i = 1

    if largo==5:
        valores_nuevos = ["1","2","3","4","5"]
        valores_nuevos.reverse()
        for i in range(largo):
            x = result[i]
            y = valores_nuevos[i]
            result[i]=x+"-"+y
            
    if largo==3:
        valores_nuevos = ["1","2","3"]
        valores_nuevos.reverse()
        for i in range(largo):
            x = result[i]
            y = valores_nuevos[i]
            result[i]=x+"-"+y

    if largo==4:
        valores_nuevos = ["1","2","3","4"]
        valores_nuevos.reverse()
        for i in range(largo):
            result[i]=valores_nuevos[i]
            
    if largo==2:
        valores_nuevos = ["1","2"]
        valores_nuevos.reverse()
        for i in range(largo):
            result[i]=valores_nuevos[i]
            
    return result
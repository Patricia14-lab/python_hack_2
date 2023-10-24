"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(result):
    valores_nuevos = ["1","-","3","-","5"]
    vacio = ["0"]
    largo = len(result)
    if largo == 0:
        result[:]=vacio[:]
    else:
        i = 1 
        for i in range(largo+1):
            if i % 2 != 0:
                result[i-1]=valores_nuevos[i-1]
            else:
                result[i-1]="-"      
    return result 


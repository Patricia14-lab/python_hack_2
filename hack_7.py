"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(result):
    vacio = [0]
    i = 0 
    largo = len(result)
    if result == [] or result == [0]:
            result=vacio
    else:
        while (i <(largo)):
            if i % 2 != 0:
                result[i] = i+1
            else:
                
                result[i]=f"{i+1}"
            i+=1
    return result
"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""
def fn_hack_2(result):
    letras = []
    for caracter in result:
        if caracter.lower() not in 'aeiou':
            letras.append(caracter)
    result = ''.join(letras) 

    return result



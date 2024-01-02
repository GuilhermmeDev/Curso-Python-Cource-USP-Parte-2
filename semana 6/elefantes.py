def incomodam(n):
    if n < 1:
        return ''
    else:
        return "incomodam " + str(incomodam(n-1))

def elefantes(n,m=None):
    if not m:
        m,n = n,2
    if n <= m:
        if n == 2:
            string = 'Um elefante incomoda muita gente\n'       
            string += str(n) + ' elefantes ' + incomodam(n) + 'muito mais\n'
        else:
            string = str(n) + ' elefantes ' + incomodam(n) + 'muito mais\n'
        if n < m:
            string += f"{n} elefantes incomodam muita gente\n"
        
        return string + elefantes(n+1,m)
    
    return ""



print(elefantes(4))
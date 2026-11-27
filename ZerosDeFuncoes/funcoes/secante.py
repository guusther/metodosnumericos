
def secante(x0, x1,funcao, tolerancia):
     
     historico = []
     while True:
        i = len(historico) + 1
        
        
        fx1 = funcao(x1)
        fx0 = funcao(x0)

        if fx1 - fx0 == 0:
            raise ValueError(f"Divisão por zero: f(x1)=f(x2) em x0={x0}, x1={x1}")
        x2 = x1 - fx1 * ((x1 - x0) / (fx1 - fx0))
        fx2 = funcao(x2)

        historico.append({"iteracao" : i, "x" : x2, "fx" : fx2})
        if abs(fx2) < tolerancia:
            break
        else:
            x0 = x1
            x1 = x2
        
     return historico

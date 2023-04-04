stack = []

with open("Calc1.stk", "r") as file:
    # Lê cada linha do arquivo
    for line in file:
      line = line.rstrip()
      if line.isdigit():
        stack.append(float(line))
      else:
        operando2 = stack.pop()
        operando1 = stack.pop()
        resultado = eval(f"{operando1} {line} {operando2}")
        stack.append(resultado)

resultado_final = stack.pop()  
print(resultado_final)
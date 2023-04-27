from enum import Enum
import re

# Tipos de token
class TokenType(Enum):
  NUM = 'NUM'
  MINUS = 'MINUS'
  PLUS = 'PLUS'
  SLASH = 'SLASH'
  STAR = 'STAR'

# Classe do token
class Token:  
  def __init__(self, type: TokenType, value: str) -> None:
    self.type = type
    self.value = value

  # Realiza a operação e retorna outro token com o resultado
  def evaluate(self, other, operator):
    if operator.type == TokenType.PLUS:
      result = float(self.value) + float(other.value)
    elif operator.type == TokenType.MINUS:
      result = float(self.value) - float(other.value)
    elif operator.type == TokenType.SLASH:
      result = float(self.value) / float(other.value)
    elif operator.type == TokenType.STAR:
      result = float(self.value) * float(other.value)
    return Token(TokenType.NUM, str(result))

  # É o formato que o token é printado
  def __str__(self) -> str:
    return "Token [type=" + self.type.value + ", value=" + self.value + "]"


class Regex:
  @staticmethod
  def isNum(token: str):
    match = re.fullmatch("^[0-9]+$", token)
    if match:
      return True
    return False

  @staticmethod
  def isOP(token: str):
    match = re.fullmatch("^[+\-\*/]$", token)
    if match:
      return True
    return False


stack = []
tokens_list = []
invalido = False

# scanning
with open("Task 3/Calc3.stk", "r") as file:
    # Lê cada linha do arquivo
    for line in file:
      line = line.rstrip()
      # se for um dígito, cria um token do tipo num e adiciona à lista de tokens
      if Regex.isNum(line):
          token = Token(TokenType.NUM, line)
          tokens_list.append(token)
      # se não, cria um token do tipo da operação e adiciona à lista
      elif Regex.isOP(line):
        if line == '+':
          token = Token(TokenType.PLUS, line)
        elif line == '-':
          token = Token(TokenType.MINUS, line)
        elif line == '/':
          token = Token(TokenType.SLASH, line)
        elif line == '*':
          token = Token(TokenType.STAR, line)
        tokens_list.append(token)
      else:
        # Levanta um erro quando o caractere é inválido
        print(f"Error: Unexpected character: {line}")
        invalido = True
        break

if not invalido:
  # percorre cada token e vai fazendo o processo da stack
  for token in tokens_list:
    print(token)
    if token.type == TokenType.NUM:
      stack.append(token)
    else:
      operando2 = stack.pop()
      operando1 = stack.pop()
      newToken = operando1.evaluate(operando2, token)
      stack.append(newToken)

  token_final = stack.pop()  
  print(token_final.value)
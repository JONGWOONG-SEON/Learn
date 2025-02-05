import sys

#
# 컨텍스트(Context)
# 인터프리터에서 전역적으로 사용되는 정보를 포함하는 클래스
#
class Context:
  def __init__(self):
    self._vars = {}

  def set(self, var , value):
    self._vars[var] = value
  
  def get(self, exp):
    return self._vars[exp]


#
# 추상 표현(Abstract Expression)
# 추상 구문 트리(Abstract Syntax Tree)의 모든 노드에서 공통적으로 사용하는
# Interpret 연산을 선언하는 클래스
#
class AbstractExpression:
  def interpret(self,context):
    return False
#
# 터미널 표현(Terminal Expression)
# 문법에서 터미널 기호에 해당하는 Interpret 연산을 구현하는 클래스
# (문장에서 터미널 기호마다 하나의 인스턴스가 필요함)
#

class TerminalExpression(AbstractExpression):
  def __init__(self, value):
    AbstractExpression.__init__(self)
    self._value = value

  def interpret(self,context):
    return context.get(self._value)


#
# 비터미널 표현(Nonterminal Expression)
# 문법에서 비터미널 기호에 대한 Interpret 연산을 구현하는 클래스
# (문법 규칙마다 하나의 클래스가 필요함)
#

class NonterminalExpression(AbstractExpression):
  def __init__(self, left, right):
    AbstractExpression.__init__(self)
    self._lop = left
    self._rop = right

  def interpret(self, context):
    return self._lop.interpret(context) and self._rop.interpret(context)

# 매우 간단한 표현식 트리의 예제
# 표현식 (A AND B)에 해당하는 코드
if __name__ == "__main__":
  A = TerminalExpression("A")
  B = TerminalExpression("B")
  exp = NonterminalExpression(A,B)
  
  context = Context()
  context.set("A",True)
  context.set("B",True)

  print(str(context.get("A")) + " AND " + str(context.get("B")), end = "" )
  print(" = " + str(exp.interpret(context)))

  context.set("A", True)
  context.set("B", False)

  print(str(context.get("A")) + " AND " + str(context.get("B")), end = "" )
  print(" = " + str(exp.interpret(context)))


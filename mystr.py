# class MyStr

class MyStr:
    def __init__(self,s):
        self.s = s

    def __truediv__(self, other):
        return self.s.split(other)

    def __add__(self, other):
        return self.s + other

    def __mul__(self, other):
        return self.s * other

    def __str__(self):
        return self.s

    def __radd__(self, other):
        return other+self.s

    def __neg__(self):
        return self.s[::-1]


s = MyStr('Hello Phython')
t = s / ' '
print(type(t))
print(t)

print(s + '~~~')
print(MyStr('python')*3)
print('hello' + ' ' + MyStr('world'))
print(-MyStr('python'))
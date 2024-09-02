class math ():
  def _init_(self, a,b):
    self.a=a
    self.b=b
  def sum(self): 
      return self.a + self.b
  def sub(self):
      return self.a-self.b
  def mul(self):
      return( self.a * self.b)
p=math(8,5)
a=p.sum()
print(a)
b=p.sub()
print(b)
c=p.mul() 
print(c)




class triangle(math):
    def _init_(self,d):
      self.d =d
    
      super()._init_(a,b)
    def area(self):
        return self.a*self.b*self.d
q=triangle(5)
print(q.area())
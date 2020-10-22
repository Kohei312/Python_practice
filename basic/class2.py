## クラスの多重継承
## 書き方 : class クラス名(継承先1, 継承先2):

class ClassA():

    def __init__(self, name):
        self.a_name =  name

    def print_a(self):
        print("ClassAのメソッド実行")
        print("a = {}".format(self.a_name))
    
    def print_hi(self):
        print("a Hi")

class ClassB():
    def __init__(self, name):
        self.b_name =  name

    def print_b(self):
        print("ClassBのメソッド実行")
        print("b = {}".format(self.b_name))
    
    def print_hi(self):
        print("b Hi")

class NewClass(ClassA, ClassB):
    def __init__(self,a_name,b_name, newName):
        ClassA.__init__(self,a_name)
        ClassB.__init__(self,b_name)
        self.name = newName
    
    def print_new_name(self):
        print("name = {}".format(self.name))

    def print_hi(self):
        ClassA.print_hi(self)
        ClassB.print_hi(self)
        print("NewClass hi")

samp = NewClass("Aname","Bname","NewClassName")

samp.print_a()
samp.print_b()
samp.print_new_name()
samp.print_hi()
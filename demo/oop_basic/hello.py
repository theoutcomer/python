class Hello(object):
    def __init__(self,name,score,age):
        self.name = name
        self.score = score#public
        self.__age = age#private

    def hello(self,name='world'):
        print('Hello1,%s.'%self.name)
        print('Hello2,%s你拿下了%s分'%(self.name,self.score))
    
    def set_name(self,name):
        if 5< len(name) < 21:
            self__name = name
        else:
            raise ValueError("bad name")
    
    def set_score(self,score):
        if 0< score < 101:
            self__score = score
        else:
            raise ValueError("bad score")
        
    def set_age(self,age):
        if 0< age < 123:
            self__age = age
        else:
            raise ValueError("bad age")   

    def get_name(self): 
        return self.__name
    
    def get_score(self): 
        return self.__score
    
    def get_age(self): 
        return self.__age
    


h = Hello("强子",100,18)
h.hello()
h.__age = 22
h._Hello__age = 26#不能直接访问__age是因为Python解释器对外把__age变量改成了_Hello__age，
print(h._Hello__age)#可强行输出私有变量
print(h.__age)#外部值与内部值不一样
print(h.get_age())#错误示范
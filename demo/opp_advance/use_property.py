class Student(object):
    # __slots__ = ('name','age')
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError("score must between 0~100!")
        self._score = value

s = Student()
s.score=99
print('s.score=',s.score)

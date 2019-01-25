class A(object):
    def __init__(self):
        self._a = "A"
    def fa(self):
        print self._a
        self.__class__.f_st()
    @staticmethod
    def f_st():
        print ("this is Static Fucntion")


if __name__ == "__main__":
    insa = A()
    insa.fa()
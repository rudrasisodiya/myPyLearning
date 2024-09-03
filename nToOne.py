class NtoOne:

    def nToOne(self,k):
        if k == 0:
            return
        print(k, end="\n")
        self.nToOne(k - 1)

obj = NtoOne()
obj.nToOne(5)
l1 = [12,23,412,124,1243,62,1,45,89,1540]
l2 = [12, 35, 1, 10, 34, 1]
l3 = [10, 5, 10]
l4 = [10, 10, 10]

class largeval:
    def larg(self,l2):
        larg = l2[0]
        for i in l2:
            if larg<=i:  
                larg = i   
        print(larg)
# obj1 = largeval()
# obj1.larg(l2)


class smallVal:
    def small(self,l4):
        smallVal = l4[0]
        for i in l4:
            if smallVal >= i: 
                smallVal = i   
        print(smallVal)
# obj2 = smallVal()
# obj2.small(l4) 

class secondLargVal:
    def secondLar(self,l2):
        l2.sort()
        print(l2)
        ValLen = len(l2)
        # print(ValLen)
        for i in l2:
            print(i,end=" ")
            # print(l2[i],end=" ")
            
obj3 = secondLargVal()
obj3.secondLar(l2)
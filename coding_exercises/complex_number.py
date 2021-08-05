def complexNumberMultiply(a, b):
        A, B = a.split("+"), b.split("+")
        print("A", A)
        print("B", B)
        A[1], B[1] = A[1][:-1], B[1][:-1]
        print("A1", A[1])
        print("B1",B[1])
        
        A = [int(x) for x in A]
        print("A..",A)
        
        B = [int(x) for x in B]
        print("B..",B)
        
        return "+".join([str(A[0]*B[0]-A[1]*B[1]), str(A[0]*B[1]+A[1]*B[0])+"i"])

# def complexNumberMultiply(self, a: str, b: str) -> str:
#         def decode(s):
#             temp=s.split('+')
#             return int(temp[0]), int(temp[1].replace('i', ''))
#         a1,a2=decode(a)
#         b1,b2=decode(b)
#         new1=a1*b1-a2*b2
#         new2=a1*b2+b1*a2
#         return str(new1)+'+'+str(new2)+'i'

print(complexNumberMultiply("1+-2i", "1+-3i"))
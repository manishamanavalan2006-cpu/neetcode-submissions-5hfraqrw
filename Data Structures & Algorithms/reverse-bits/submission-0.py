class Solution:
    def reverseBits(self, n: int) -> int:
        output=""
        decimalno=0
        while n!=0:
            rever=n%2
            output+=str(rever)
            n//=2
        
        if len(output)<32:
            data=32-len(output)
            output=output+"0"*data
        
        for i in output:
            decimalno=decimalno*2+int(i)
        return decimalno
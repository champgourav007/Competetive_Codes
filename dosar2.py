def sol(input_from_question):
    input = input_from_question.split(" ")
    n = int(input[0])
    arr = []
    for i in range(n):
        arr.append(int(input[i+1]))
    print()
    mp = {}
    Sum = 0
    res = []
    for i in range(n):
        # Calculating the residue of
        # prefixSum
        Sum = (Sum + arr[i]) % n
 
        # If the pre[i]%n==0
        if (Sum == 0) :
            # print size
            res.append(i+1)
 
            # Print the first i indices
            for j in range(i + 1):
                res.append(j+1)
            return res
 
        # If this sum was seen earlier,
        # then the contiguous subsegment
        # has been found
        if Sum in mp :
           
            # Print the size of subset
            print((i - mp[Sum]))
 
            # Print the indices of contiguous
            # subset
            for j in range(mp[Sum] + 1,
                           i + 1):
                res.append(j+1)
 
            return res
        else:
            mp[Sum] = i
    return res
        
            

if __name__ == "__main__":
    input_from_question = input()
    print(sol(input_from_question))
    
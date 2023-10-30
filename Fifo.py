
##FIFO page replacement algorithm

capacity=3
process_list=[1,2,3,4,5,3,3,2,2,1,5]
s=[]
page_fault=0
for i in process_list:
    if i not in s:
        if len(s)==capacity:
            s.remove(s[0])
            s.append(i)
        else:
            s.append(i)
        page_fault+=1
print("the no page fault:",[page_fault])                
             

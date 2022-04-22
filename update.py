def update(*args):
    print(len(args))
    li=list(args)
    print(li)
    del li[0]
    print(li)
    q="update "+ args[0] + " set " 
    
    if(len(li[0])==2):
          for i in range(len(li)):
              if(i%2==0):
                q+=li[0][i] + " = ""'" +li[0][i+1]+"'"
    elif(len(li[0])>2):
         for i in range(len(li[0])):
            if(i%2==0):
                q+=li[0][i] + " = " + li[0][i+1] + ", "
        
    q+=" where "
    for i in range(len(li[1])):
        if(i%2==0):
            q+=li[1][i] + " = ""'" +li[1][i+1]+"'"   

    return(q) 
#q=q[0:len(q)-4]

def summer(a,b,c):
    result =  a+b+c
    return result

def minPrice(cost):
    List = []
    n = len(cost[0])
    print "Please confirm that the number of columns in your input is -", n  
    for i in range(n):
        for j in range(n):
            if (i == j):
                continue
            else :
                for p in range(n):
                    if ( j == p):
                        continue
                    else:
                        sumV = summer(cost[0][i],cost[1][j],cost[2][p])
                        List.append(sumV)
    print (List)
    optimalCost = min(List)
    return optimalCost                      

if __name__ == '__main__':
    # Intialize Cost as 3xn 2d Matrix before exceution
    # cost = [[2,2,1],[2,3,1],[2,1,1]]
    # cost = [[1,2,2,1,4,5],
    #         [2,2,1,4,6,7],
    #         [2,1,2,1,2,1]] 
    cost = [[1,2,2],[2,2,1],[2,1,2]] 
    result = minPrice(cost)
    print "Optimal Cost is - ", result
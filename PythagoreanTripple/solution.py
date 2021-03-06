def pythagoreanTriplets(limits) :
    c, m = 0, 2
    result = 0
 
    # Limiting c would limit
    # all a, b and c
    while c < limits :
         
        # Now loop on n from 1 to m-1
        for n in range(1, m) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
 
            # if c is greater than
            # limit then break it
            if c > limits :
                break
            
            if a + b + c == limits: return a*b*c
 
        m = m + 1

print(pythagoreanTriplets(1000))
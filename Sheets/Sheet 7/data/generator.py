import random

def data_generator (intercept, slope, size):

    random.seed(1337)
    
    f = lambda x : intercept + slope * x
    
    data = [ ]

    for _ in range ( size ):

        while True :

            x = random.random( )
            
            y = random.random( )
            
            label = 1 if f(x) > y else -1

            if abs (f(x) -y) > 0.1:
            
                break ;

        data.append ( ( x, y, label ) )

    return data

#!/usr/bin/env python3

import time
import argparse

def diamond(n = 7):
    if n%2 == 0:
        n = eval(input("please use an odd number: "))
    num_stars = [i for i in range(1, n+2, 2)]
    num_stars = num_stars+num_stars[-2::-1]
    d_list = [0]*len(num_stars)
    for i in range(len(num_stars)):
        nt = num_stars[i]
        buff = int((n - nt)/2)
        d_list[i] = " "*buff+"*"*nt+" "*buff

    return(d_list)


# took these colors from the following stack overflow thread
# https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python

color_dict = {"p" : "\033[95m",
              "c" : "\033[96m",
              "d": "\033[36m",
              "b" : "\033[36m",
              "g" : "\033[92m",
              "y" : "\033[93m",
              "r" : "\033[91m",
              "e" : "\033[0m"
             }

d = diamond(21)

def diamond_print2(iter_max = 1, 
                   shape = d, 
                   color_vect = ["r", "b", "g", "p"]):
    color_d = 0*len(d)
    col_iter = 1
    #d_list
    def color_iter(color_vect = color_vect):
        color_vect_list = [0]*len(color_vect)
        color_vect_list[0] = color_vect

        for i in range((len(color_vect_list) -1)):
            color_vect = color_vect[1:] + [color_vect[0]]
            color_vect_list[i + 1] = color_vect

        return(color_vect_list)
    
    cvl = color_iter()
    
        
        
#         col_iter += 1
    t = 0
    while t < iter_max:
        for i in range(len(cvl)):
            # pattern to follow is: (color + d row + end, next) + same pattern _next_ color  
            for k in range(len(shape)):
                print(*map(lambda x: color_dict[x]+shape[k]+color_dict["e"], [cvl[j][i] for j in range(len(cvl))]))
                time.sleep(.02)
        t += 1


if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--iter_max", type=int, help="how many repeats?", required=True)
    parser.add_argument("-c", "--colors",
                        help='colors you would like to see, default "brg" ("blue red green")', default = "brg")
    args = parser.parse_args()
    diamond_print2(iter_max = args.iter_max, color_vect = list(args.colors))



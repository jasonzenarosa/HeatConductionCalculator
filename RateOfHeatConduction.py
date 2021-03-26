from variables import *


def empty():
    print("")


while True:
    empty()
    print("Q / t = (k * A * deltaT) / L ")
    empty()
    solvingFor = input("What are you solving for?  ")
    empty()
    try:
        if solvingFor == "Q":
            t = time()
            k = thermal()
            T1 = initial_temp()
            T2 = final_temp()
            delta_T = abs(T2 - T1)
            A = area()
            L = length()
            Q = (t * k * A * delta_T) / L
            empty()
            print("Q = " + str(Q) + " J")
        elif solvingFor == "t":
            Q = heat()
            k = thermal()
            T1 = initial_temp()
            T2 = final_temp()
            delta_T = abs(T2 - T1)
            A = area()
            L = length()
            t = (Q * L) / (k * A * delta_T)
            empty()
            print("t = " + str(t) + " sec")
        elif solvingFor == "k":
            Q = heat()
            t = time()
            T1 = initial_temp()
            T2 = final_temp()
            delta_T = abs(T2 - T1)
            A = area()
            L = length()
            k = (Q * L) / (t * A * delta_T)
            empty()
            print("k = " + str(k) + " J/smK")
        elif solvingFor == "deltaT":
            t = time()
            k = thermal()
            Q = heat()
            A = area()
            L = length()
            delta_T = (Q * L) / (t * k * A)
            empty()
            print("deltaT = " + str(delta_T) + " K")
        elif solvingFor == "A":
            t = time()
            k = thermal()
            T1 = initial_temp()
            T2 = final_temp()
            delta_T = abs(T2 - T1)
            Q = heat()
            L = length()
            A = (Q * L) / (t * k * delta_T)
            empty()
            print("A = " + str(A) + " sq. m")
        elif solvingFor == "L":
            t = time()
            k = thermal()
            T1 = initial_temp()
            T2 = final_temp()
            delta_T = abs(T2 - T1)
            A = area()
            Q = heat()
            L = (t * k * A * delta_T) / Q
            empty()
            print("L = " + str(L) + " m")
        elif solvingFor == "exit":
            break
        else:
            print("error: invalid variable")
    except ValueError:
        empty()
        print("error: invalid value")
    empty()

import sys
import os


def prime(s):
    # your code goes here
    prime = True

            for i in range (1, s):

                    if i != 1 :

                        if s % i ==0:

                        	prime = False

                        	

            if prime == True:

            	print(f"{s} is a prime numner")

            else:

                print(f"{s} is not a prime number")

   

def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))

import sys
def main(argv):
    print('line1')
    print("Hello ", str(sys.argv[1]))

if __name__ == "__main__":
   main(sys.argv[1:])

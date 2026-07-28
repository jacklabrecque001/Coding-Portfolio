from markov_model import MarkovModel
import stdio
import sys

# Entry point.
def main():
    k=int(sys.argv[1])
    n=int(sys.argv[2])
    text=sys.stdin.read()
    model=MarkovModel(text,k)
    a=model.gen(text[0:k],n)
    stdio.writeln(a)
if __name__ == "__main__":
    main()
    

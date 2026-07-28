from markov_model import MarkovModel
import stdio
import sys

# Entry point.
def main():
    k=int(sys.argv[1])
    s=sys.argv[2]
    
    text=sys.stdin.read()
    #stdio.writeln(text)
    model=MarkovModel(text,k)
    replaced=model.replace_unknown(s)
    stdio.writeln(replaced)
    return(replaced)

if __name__ == "__main__":
    main()

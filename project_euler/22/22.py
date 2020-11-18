

def main():
    print("euler 22") ## p022_names.txt

    fin = open("p022_names.txt").read();

    names = fin.split('","');
    names[0]=names[0][1:]
    names[-1]=names[-1][:-1]
    names.sort()

    totalLetterScore = 0
    nth = 0
    
    for name in names:
        nth+=1
        letterScore = 0
        for letter in name:
            letterScore += lScore(letter)*nth
        totalLetterScore+=letterScore
        if name == "COLIN":
            print(">",letterScore)
##        break

    print("total>",totalLetterScore)

    print("end of program")

def lScore(letter):
    return {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26,
    }[letter]

main()

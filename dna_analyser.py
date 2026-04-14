print("    ***(DNA ANALYSER)***    ")

while True:

    seq1 = input("Enter your DNA sequence: ").upper()
    print("Given DNA Sequence:", seq1)

    countA = 0
    countT = 0
    countG = 0
    countC = 0

    valid = True

    for base in seq1:
        if base == "A":
            countA += 1
        elif base == "G":
            countG += 1
        elif base == "C":
            countC += 1
        elif base == "T":
            countT += 1
        else:
            print("Invalid base found:", base)
            valid = False


# ---- (ATGC Counter) ---- [this counts the ATGC count in the dna]

    if valid:
        print("A Count:", countA)
        print("C Count:", countC)
        print("G Count:", countG)
        print("T Count:", countT)

# ---- (GC % Calculator) ---- [this calculates the CG% of the dna]

        totlen = len(seq1)
        gccount = countC + countG
        GC = round((gccount / totlen) * 100, 2)

        print("GC%:", GC, "%")

# ---- (SEQUENCE COMPARATOR) ---- [this compares the given dna and another dna]

        compare = input("Do you want to compare another DNA? (y/n): ").lower()

        if compare == "y":

            seq2 = input("Enter second DNA sequence: ").upper()
            print("Second DNA Sequence needed to compared:", seq2)

            valid2 = True
            for base in seq2:
                if base not in "ATGC":
                    print("Invalid base found in second DNA:", base)
                    valid2 = False

            if valid2:

                minlen = min(len(seq1), len(seq2))

                matches = 0

                print("--- Mutation Detection ---")

                for i in range(minlen):
                    if seq1[i] == seq2[i]:
                        matches += 1
                    else:
                        print("Mutation Found at position: " , i+1 , seq1[i] , "->" , seq2[i])

                similarity = round((matches / minlen) * 100, 2)

                print("Similarity:", similarity, "%")

    else:
        print("Invalid DNA sequence. Analysis stopped.")

# ---- (REPEAT PROGRAM) ----

    quest = input("Do you want to analyse another DNA? (y/n): ")

    if quest.lower() != "y":
        break

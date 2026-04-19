print("    ***(DNA ANALYSER)***    ")

# ---------- FASTA READER ----------
def read_fasta(filename):

    sequences = {}
    name = ""

    with open(filename) as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                name = line[1:]
                sequences[name] = ""
            else:
                sequences[name] += line.upper()

    return sequences


# ---------- CODON TABLE (DNA → PROTEIN) ----------
codon_table = {
'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
'ATT':'I','ATC':'I','ATA':'I','ATG':'M',
'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*',
'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
'AAT':'N','AAC':'N','AAA':'K','AAG':'K',
'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
'TGT':'C','TGC':'C','TGA':'*','TGG':'W',
'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
'GGT':'G','GGC':'G','GGA':'G','GGG':'G'
}


while True:

# ---------- LOAD OPTION ----------
    load = input("Load DNA from FASTA file? (y/n): ").lower()

    if load == "y":
        filename = input("Enter FASTA filename: ")
        sequences = read_fasta(filename)

        names = list(sequences.keys())

        seq1 = sequences[names[0]]
        print("Loaded Sequence:", names[0])

        if len(names) >= 2:
            seq2 = sequences[names[1]]
        else:
            seq2 = ""

    else:
        seq1 = input("Enter your DNA sequence: ").upper()
        seq2 = ""

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


# ---- ATGC COUNTER ----
    if valid:

        print("A Count:", countA)
        print("C Count:", countC)
        print("G Count:", countG)
        print("T Count:", countT)

# ---- GC % CALCULATOR ----
        totlen = len(seq1)
        gccount = countC + countG
        GC = round((gccount / totlen) * 100, 2)

        print("GC%:", GC, "%")

# ---- DNA → RNA TRANSCRIPTION ----
        rna = seq1.replace("T", "U")
        print("RNA Sequence:", rna)

# ---- PROTEIN TRANSLATION ----
        protein = ""

        for i in range(0, len(seq1)-2, 3):
            codon = seq1[i:i+3]
            amino = codon_table.get(codon, "?")
            protein += amino

        print("Protein Sequence:", protein)

# ---- SEQUENCE COMPARATOR ----
        compare = input("Do you want to compare another DNA? (y/n): ").lower()

        if compare == "y":

            if seq2 == "":
                seq2 = input("Enter second DNA sequence: ").upper()

            print("Second DNA Sequence:", seq2)

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
                        print(
                            "Mutation Found at position:",
                            i+1,
                            seq1[i],
                            "->",
                            seq2[i]
                        )

                similarity = round((matches / minlen) * 100, 2)

                print("Similarity:", similarity, "%")

    else:
        print("Invalid DNA sequence. Analysis stopped.")

# ---- REPEAT PROGRAM ----
    quest = input("Do you want to analyse another DNA? (y/n): ")

    if quest.lower() != "y":
        break

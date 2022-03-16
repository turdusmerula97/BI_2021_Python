class rna:
    def __init__(self, sequence):
        segments = [x for x in sequence.strip().split('>') if x]
        titles = []
        sequences = []
        for seg in segments:
            lines = seg.splitlines()
            titles.append(lines[0].strip())
            sequences.append(''.join(lines[1:]))
            self.data = dict(zip(titles, sequences))

    def reverse_complement(self, sequence):
        compl_dict = {'A': 'U', 'G': 'C', 'C': 'G', 'U': 'A'}
        return "".join(compl_dict[n] for n in reversed(sequence))

    def gc_content(self, sequence):
        g_number = int(sequence.count('G'))
        c_number = int(sequence.count('C'))
        tot_nucleotids = len(sequence)
        gc_percentage = ((g_number + c_number) / tot_nucleotids) * 100
        print(tot_nucleotids, gc_percentage)


class dna(rna):
    def reverse_complement(self, sequence):
        compl_dict = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
        return "".join(compl_dict[n] for n in reversed(sequence))

    def transcribe_dna(self, sequence):
        rna = []
        for i in sequence:
            if i == "T":
                rna += "U"
            else:
                rna += i
        return rna
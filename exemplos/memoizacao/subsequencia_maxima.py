sequencia0 = [-10, 20, 10, -30, 40]
sequencia1 = [ 80, 20, 10, -70, 30]
sequencia2 = [1,2,3,9,4,5,6]
sequencia3 = [9,5,6,3,9,6,4,7]

class max_subseq_finder():
    def __init__(self):
        self.max_subseq = []
        self.seq_original = []
        self.seqs_exploradas = []
        self.totalCalls = 0
        self.totalMemoization = 0

    def encontre_subsequencia_crescente_maxima(self, sequencia, index):
        self.totalCalls += 1

        if sequencia in self.seqs_exploradas:
            self.totalMemoization += 1
            return

        self.seqs_exploradas += [list(sequencia)]

        if len(sequencia) > 1:
            if sequencia[-1] >= sequencia[-2]:
                if len(self.max_subseq) < len(sequencia):
                    self.max_subseq = sequencia
            else:
                sequencia.pop(-1)

        if index == len(self.seq_original)-1:
            return
        else:
            for (indice, item) in enumerate(self.seq_original[index+1:]):
                self.encontre_subsequencia_crescente_maxima(sequencia+[item],index+indice+1)

        pass

    def maxima_subsequencia(self, sequencia_original):

        self.max_subseq = []
        self.seq_original = []
        self.seqs_exploradas = []

        self.seq_original = sequencia_original
        for (indice, item) in enumerate(self.seq_original):
            self.encontre_subsequencia_crescente_maxima([item],indice)
        return self.max_subseq

seq_max_finder = max_subseq_finder()

max_subseq0 = seq_max_finder.maxima_subsequencia(sequencia0)
print(max_subseq0)

max_subseq1 = seq_max_finder.maxima_subsequencia(sequencia1)
print(max_subseq1)

max_subseq2 = seq_max_finder.maxima_subsequencia(sequencia2)
print(max_subseq2)

max_subseq3 = seq_max_finder.maxima_subsequencia(sequencia3)
print(max_subseq3)


sequencia0 = [-10, 20, 10, -30, 40]
sequencia1 = [ 80, 20, 10, -70, 30]
sequencia2 = [1,2,3,9,4,5,6]
sequencia3 = [9,5,6,3,9,6,4,7]

class max_subseq_finder():
    def __init__(self):
        self.max_subseq = []
        self.seq_original = []
        self.seqs_exploradas = []

    def encontre_subsequencia_crescente_maxima(self, sequencia, index):
        if sequencia in self.seqs_exploradas:
            return

        self.seqs_exploradas += [sequencia]

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

    def maxima_subsequencia(self, sequencia_original, seqs_exploradas=[]):

        self.max_subseq = []
        self.seq_original = []
        self.seqs_exploradas = seqs_exploradas

        self.seq_original = sequencia_original
        for (indice, item) in enumerate(self.seq_original):
            self.encontre_subsequencia_crescente_maxima([item],indice)
        return self.max_subseq, seqs_exploradas

class max_common_subseq_finder():
    def __init__(self):
        self.seq_originais = []
        self.seq_indexes = []
        self.max_subseq = []
        self.max_subseq_finder = max_subseq_finder()

    def maxima_subsequencia_comum(self,sequencias):
        self.seq_originais = sequencias
        self.seq_indexes = []
        self.max_subseq = []
        self.seq_exploradas = [[]*len(sequencias)]

        maximas_subsequencias = [[]*len(sequencias)]
        for i in range(len(sequencias)):
            for (indice, item) in enumerate(self.seq_originais[i]):
                subseq, seq_exploradas_parcial = self.max_subseq_finder.maxima_subsequencia([item],self.seq_exploradas[i])
                self.seq_exploradas += seq_exploradas_parcial
                maximas_subsequencias[i] += [subseq]

        pass



common_seq_max_finder = max_common_subseq_finder()
max_subseq0 = common_seq_max_finder.maxima_subsequencia_comum([sequencia0,sequencia1])
print(max_subseq0)



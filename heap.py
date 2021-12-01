class maxHeap:
    def __init__(self):
        self.H = [-1]
        self.D = [-1]
        self.n = 0

    def Maximum(self):
        return self.H[1]

    def Insert(self, name, value):
        self.n = self.n + 1
        self.H.append(name)
        self.D.append(value)
        self.HeapFy(self.n)

    def Delete(self, h):
        if(self.n == 1 or h == self.n ):
            self.D.pop()
            self.H.pop()
            self.n = self.n - 1
        else:
            self.D[h]=self.D.pop()
            self.H[h]=self.H.pop()
            self.n = self.n - 1
            self.HeapFy(h)
    
    def HeapFy(self, k):
        if k > 1 and self.D[k] > self.D[k/2]:
            h = k
            while h>1 and self.D[h] > self.D[h/2]:
                self.swap(h, h/2)
                h = h/2
        else:
            if k <= self.n/2 and (((2*k + 1) <= self.n and self.D[k] < max(self.D[2*k], self.D[(2*k) + 1]))
                or (2*k + 1 > self.n and self.D[k] < self.D[2*k])):
                h = k
                while h <= (self.n)/2 and (((2*h+1) <= self.n and self.D[h] < max( self.D[2*h], self.D[(2*h) + 1]))
                    or (2*h + 1 > self.n and self.D[h] < self.D[2*h])):
                    d = 2*h
                    if (2*h+1) <= self.n and self.D[2*h] < self.D[(2*h) + 1]: d = 2*h + 1 
                    self.swap(h,d)
                    h = d

    def swap(self, h, d):
        temp = self.D[h]
        self.D[h] = self.D[d]
        self.D[d] = temp

        temp = self.H[h]
        self.H[h] = self.H[d]
        self.H[d] = temp

    def HeapSort(self):
        sorted_edges = []
        sorted_weights = []
        while(self.n >= 1):
            sorted_edges.append(self.H[1])
            sorted_weights.append(self.D[1])
            self.Delete(1)
        return [sorted_weights,sorted_edges]
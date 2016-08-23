
import numpy


def GetMatrixA(urls, id): #url-id编码的dict
    n = len(urls)
    A = [[0.0] * n for i in range(n)]
    for url in urls:
        for link in url.link_to:
            try:
                A[url.id][link] += 1
            except:
                print('log-error')
                pass
    return A


class RankPage(object):
    def __init__(self, A): #传入一个二维矩阵，和一个一维矩阵
        self.A = numpy.array(A)
        self.B = []
        n = len(A)
        for i in range(n):
            self.B.append([1 / n])

    def calcu(self):
        for i in range(10):
            self.B = self.A.dot(self.B)
        res = [x[0] for x in self.B]
        return res

    def deepcalcu(self):
        pass

# A = GetMatrixA(urls, id)
# ranker = RankPage(A)
# rankB = ranker.calcu()
# for i in range(len(rankB)):
#     urls[i].rank = rankB[i]
#urls = sorted(urls, key=lambda x: x.rank, reverse=True)
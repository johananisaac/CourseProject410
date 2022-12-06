from math import log

# @parameters 
k1 = 1.2 #factor 1
k2 = 100 #factor 2
b = 0.75 #Document normalizer
R = 0.0 #Relevancy, 0 means no relevancy infor is known


def getK(docLength, averageDocLength):
    result = k1 * (1- b + b * (float(docLength)/float(averageDocLength)))
    return result

def getIDF(r,R,N,n):
    result = log( ( (r + 0.5) / (R - r + 0.5) ) / ( (n - r + 0.5) / (N - n - R + r + 0.5)))
    return result

def getdocTermWeight(k1, f, b, docLength, averageDocLength):
    K = k1 * (1- b + b * (float(docLength)/float(averageDocLength)))
    result = ((k1 + 1) * f) / (K + f)
    return result

def getqueryTermWeight(k2,qf):
    result = ((k2 + 1) * qf) / (k2 + qf)
    return result

def getBM25Score(n, f, qf, r, N, docLength, averageDocLength):
    IDF= getIDF(r,R,N,n)
    docTermWeight = getdocTermWeight(k1, f, b, docLength, averageDocLength)
    queryTermWeight = getqueryTermWeight(k2,qf)
    result = IDF * docTermWeight * queryTermWeight
    return result

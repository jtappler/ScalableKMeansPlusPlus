def initi(X, K):
    C = [X[0]]
    for k in range(1, K):
        D = numpy.array([min([scipy.inner(c-x,c-x) for c in C]) for x in X])
        probs = D/D.sum()
        cumprobs = probs.cumsum()
        r = scipy.rand()
        for j,p in enumerate(cumprobs):
            if r < p:
                i = j
                break
        C.append(X[i])
    return C

def logLikelihood(beta, points):
    return 1/(1.0+et**(-(np.dot(beta,points))))

def nearest_cluster_center(point, cc):
    index.min = point.group
    distance.min = FLOAT_MAX
    for i, c in enumerate(cc):
        d = sqrd(c, point)
        if distance.min > d:
            distance.min = d
            index.min = i
    return (index.min, distance.min)

def sqrd(a, b):
        return (a.x-b.x)**2+(a.y-b.y)**2
 
def kMeansPP(points, cc):
    cc[0] = copy(choice(points))
    d = [0.0 for a in xrange(len(points))]
 
    for i in xrange(1, len(cc)):
        s = 0
        for j, p in enumerate(points):
            d[j] = nearest_cluster_center(p, cc[:i])[1]
            s += d[j]
        s *= random()
        for j, di in enumerate(d):
            s -= di
            if s > 0:
                continue
            cc[i] = copy(points[j])
            break
    for p in points:
        p.group = nearest_cluster_center(p, cc)[0]
    return
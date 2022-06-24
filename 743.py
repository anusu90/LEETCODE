class Solution:
    def networkDelayTime(self, B: List[List[int]], A: int, C: int) -> int:
        pq=[]
        adjMap={}
        dist = [-1 for _ in range(0,A+1)]
        dist[0]=0
        for f,t,d in B:
            if f in adjMap:
                adjMap[f].append((d,t))
            else:
                adjMap[f]=[(d,t)]
        dist[C]=0
        heappush(pq,(0,C))
        while len(pq)>0:
            n = len(pq)
            for _ in range(n):
                d,node = heappop(pq)
                if node in adjMap:
                    for di,travel_to_node in adjMap[node]:
                        if  dist[travel_to_node]==-1 or di+d<dist[travel_to_node]:
                            dist[travel_to_node]=di+d
                            heappush(pq,(di+d,travel_to_node))
        m=-1
        for x in dist:
            if x==-1:
                return -1
            else:
                m=max(m,x)
        return m

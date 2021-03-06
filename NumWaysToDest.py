from heapq import heappop, heappush
from typing import List


def num(parent, cur, dp):
    if cur == 0:
        return 1
    if cur not in dp:
        dp[cur] = sum(num(parent, par, dp) for par in parent[cur])
    return dp[cur]


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        parent = [set() for _ in range(n)]
        dist = [None] * n
        dist[0] = 0
        parent[0].add(0)
        q = [(0, 0)]
        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        while q:
            d, cur = heappop(q)
            if dist[cur] == d:
                for nr, nd in adj[cur]:
                    if dist[nr] is None or dist[nr] >= d + nd:
                        if d + nd == dist[nr]:
                            parent[nr].add(cur)
                        else:
                            parent[nr] = {cur}
                            heappush(q, (d + nd, nr))
                        dist[nr] = d + nd
        return num(parent, n - 1, {})


if __name__ == '__main__':
    print(Solution().countPaths(
        36,
        [[0, 1, 7748], [2, 1, 6906], [0, 2, 14654], [2, 3, 4731], [3, 1, 11637], [3, 0, 19385], [4, 1, 9668], [4, 2,
                                                                                                               2762], [
             5, 3, 2151], [6, 2, 10826], [5, 6, 3944], [6, 1, 17732], [6, 3, 6095], [0, 6, 25480], [4, 6, 8064], [5, 7,
                                                                                                                  7439], [
             2, 7, 14321], [1, 7, 21227], [6, 7, 3495], [3, 7, 9590], [0, 7, 28975], [4, 7, 11559], [8, 1, 27468], [8,
                                                                                                                    4,
                                                                                                                    17800], [
             8, 7, 6241], [6, 8, 9736], [8, 0, 35216], [8, 2, 20562], [5, 8, 13680], [7, 9, 14770], [5, 9, 22209], [0,
                                                                                                                    9,
                                                                                                                    43745], [
             9, 8, 8529], [4, 10, 32170], [10, 8, 14370], [10, 7, 20611], [10, 6, 24106], [0, 10, 49586], [9, 10,
                                                                                                           5841], [10,
                                                                                                                   2,
                                                                                                                   34932], [
             11, 2, 35928], [7, 11, 21607], [10, 11, 996], [6, 11, 25102], [0, 11, 50582], [12, 8, 22131], [12, 6,
                                                                                                            31867], [12,
                                                                                                                     7,
                                                                                                                     28372], [
             11, 12, 6765], [12, 3, 37962], [12, 10, 7761], [12, 4, 39931], [0, 13, 44838], [13, 9, 1093], [5, 13,
                                                                                                            23302], [8,
                                                                                                                     13,
                                                                                                                     9622], [
             14, 8, 11195], [7, 14, 17436], [13, 14, 1573], [3, 15, 40109], [15, 2, 44840], [15, 8, 24278], [15, 12,
                                                                                                             2147], [15,
                                                                                                                     1,
                                                                                                                     51746], [
             15, 7, 30519], [15, 0, 59494], [15, 5, 37958], [10, 15, 9908], [13, 15, 14656], [15, 14, 13083], [15, 4,
                                                                                                               42078], [
             6, 15, 34014], [11, 15, 8912], [15, 9, 15749], [16, 15, 9675], [0, 16, 69169], [3, 16, 49784], [16, 11,
                                                                                                             18587], [4,
                                                                                                                      16,
                                                                                                                      51753], [
             8, 16, 33953], [16, 13, 24331], [16, 10, 19583], [16, 1, 61421], [16, 5, 47633], [9, 16, 25424], [3, 17,
                                                                                                               59433], [
             11, 17, 28236], [17, 10, 29232], [17, 6, 53338], [9, 17, 35073], [17, 15, 19324], [17, 4, 61402], [13, 17,
                                                                                                                33980], [
             0, 17, 78818], [17, 14, 32407], [17, 7, 49843], [1, 17, 71070], [17, 8, 43602], [17, 12, 21471], [5, 17,
                                                                                                               57282], [
             17, 16, 9649], [18, 13, 38474], [3, 18, 63927], [2, 18, 68658], [18, 11, 32730], [18, 0, 83312], [6, 18,
                                                                                                               57832], [
             18, 10, 33726], [14, 18, 36901], [18, 5, 61776], [18, 17, 4494], [18, 1, 75564], [18, 8, 48096], [4, 18,
                                                                                                               65896], [
             18, 16, 14143], [18, 7, 54337], [15, 18, 23818], [18, 12, 25965], [9, 18, 39567], [19, 5, 65575], [9, 19,
                                                                                                                43366], [
             10, 19, 37525], [13, 19, 42273], [19, 2, 72457], [14, 19, 40700], [16, 19, 17942], [19, 0, 87111], [19, 17,
                                                                                                                 8293], [
             20, 15, 32190], [14, 20, 45273], [20, 18, 8372], [19, 20, 4573], [8, 20, 56468], [20, 9, 47939], [20, 4,
                                                                                                               74268], [
             20, 3, 72299], [20, 7, 62709], [16, 21, 9928], [21, 1, 71349], [2, 21, 64443], [7, 21, 50122], [21, 10,
                                                                                                             29511], [6,
                                                                                                                      21,
                                                                                                                      53617], [
             21, 14, 32686], [21, 3, 59712], [21, 17, 279], [11, 21, 28515], [5, 21, 57561], [12, 21, 21750], [22, 11,
                                                                                                               41416], [
             22, 17, 13180], [3, 22, 72613], [21, 22, 12901], [22, 13, 47160], [4, 22, 74582], [16, 22, 22829], [1, 22,
                                                                                                                 84250], [
             9, 22, 48253], [22, 0, 91998], [14, 22, 45587], [22, 10, 42412], [19, 22, 4887], [22, 12, 34651], [2, 22,
                                                                                                                77344], [
             5, 22, 70462], [23, 4, 4185], [5, 23, 65], [4, 24, 74851], [24, 6, 66787], [22, 24, 269], [2, 24, 77613], [
             15, 24, 32773], [12, 24, 34920], [24, 3, 72882], [24, 23, 70666], [16, 24, 23098], [18, 24, 8955], [24, 5,
                                                                                                                 70731], [
             24, 14, 45856], [24, 7, 63292], [24, 20, 583], [24, 0, 92267], [24, 17, 13449], [25, 14, 50927], [25, 10,
                                                                                                               47752], [
             25, 7, 68363], [25, 13, 52500], [25, 24, 5071], [25, 12, 39991], [16, 25, 28169], [25, 4, 79922], [2, 25,
                                                                                                                82684], [
             25, 17, 18520], [0, 25, 97338], [25, 18, 14026], [6, 25, 71858], [25, 11, 46756], [25, 8, 62122], [25, 1,
                                                                                                                89590], [
             25, 23, 75737], [25, 19, 10227], [25, 22, 5340], [25, 3, 77953], [9, 25, 53593], [21, 25, 18241], [25, 15,
                                                                                                                37844], [
             9, 26, 60567], [7, 26, 75337], [26, 18, 21000], [5, 26, 82776], [6, 26, 78832], [21, 26, 25215], [26, 13,
                                                                                                               59474], [
             19, 26, 17201], [26, 15, 44818], [26, 14, 57901], [26, 1, 96564], [4, 26, 86896], [26, 20, 12628], [26, 24,
                                                                                                                 12045], [
             26, 11, 53730], [3, 26, 84927], [26, 12, 46965], [26, 17, 25494], [26, 2, 89658], [10, 26, 54726], [22, 26,
                                                                                                                 12314], [
             25, 26, 6974], [22, 27, 6693], [27, 9, 54946], [27, 0, 98691], [2, 27, 84037], [25, 27, 1353], [22, 28,
                                                                                                             13055], [9,
                                                                                                                      28,
                                                                                                                      61308], [
             23, 28, 83452], [28, 8, 69837], [18, 28, 21741], [28, 13, 60215], [16, 28, 35884], [5, 28, 83517], [3, 28,
                                                                                                                 85668], [
             24, 28, 12786], [28, 27, 6362], [12, 28, 47706], [28, 25, 7715], [28, 15, 45559], [28, 10, 55467], [28, 0,
                                                                                                                 105053], [
             28, 19, 17942], [1, 28, 97305], [2, 28, 90399], [28, 7, 76078], [11, 28, 54471], [26, 28, 741], [6, 28,
                                                                                                              79573], [
             14, 28, 58642], [28, 17, 26235], [21, 28, 25956], [20, 28, 13369], [19, 29, 3375], [13, 30, 69897], [0, 30,
                                                                                                                  114735], [
             30, 1, 106987], [30, 16, 45566], [30, 6, 89255], [30, 18, 31423], [28, 30, 9682], [30, 21, 35638], [30, 2,
                                                                                                                 100081], [
             30, 7, 85760], [30, 17, 35917], [14, 30, 68324], [24, 30, 22468], [3, 30, 95350], [23, 30, 93134], [19, 30,
                                                                                                                 27624], [
             15, 30, 55241], [30, 12, 57388], [31, 21, 38885], [31, 22, 25984], [31, 16, 48813], [31, 7, 89007], [26,
                                                                                                                  31,
                                                                                                                  13670], [
             31, 1, 110234], [31, 29, 27496], [23, 31, 96381], [31, 10, 68396], [14, 31, 71571], [2, 31, 103328], [31,
                                                                                                                   15,
                                                                                                                   58488], [
             11, 31, 67400], [31, 3, 98597], [12, 31, 60635], [31, 9, 74237], [8, 31, 82766], [25, 31, 20644], [18, 31,
                                                                                                                34670], [
             24, 31, 25715], [31, 13, 73144], [31, 27, 19291], [31, 17, 39164], [31, 6, 92502], [31, 30, 3247], [31, 19,
                                                                                                                 30871], [
             4, 32, 84389], [16, 32, 32636], [32, 0, 101805], [32, 24, 9538], [19, 32, 14694], [18, 32, 18493], [14, 32,
                                                                                                                 55394], [
             32, 20, 10121], [7, 32, 72830], [32, 21, 22708], [17, 32, 22987], [3, 32, 82420], [1, 32, 94057], [33, 8,
                                                                                                                87411], [
             20, 33, 30943], [31, 33, 4645], [33, 27, 23936], [7, 33, 93652], [25, 33, 25289], [22, 33, 30629], [33, 30,
                                                                                                                 7892], [
             28, 33, 17574], [33, 9, 78882], [33, 3, 103242], [33, 6, 97147], [11, 33, 72045], [33, 10, 73041], [13, 33,
                                                                                                                 77789], [
             21, 33, 43530], [33, 23, 101026], [4, 33, 105211], [33, 16, 53458], [29, 33, 32141], [33, 17, 43809], [33,
                                                                                                                    24,
                                                                                                                    30360], [
             5, 34, 106200], [13, 34, 82898], [28, 34, 22683], [34, 20, 36052], [34, 3, 108351], [22, 34, 35738], [14,
                                                                                                                   34,
                                                                                                                   81325], [
             25, 34, 30398], [34, 8, 92520], [4, 34, 110320], [10, 34, 78150], [34, 17, 48918], [31, 34, 9754], [18, 34,
                                                                                                                 44424], [
             34, 32, 25931], [34, 26, 23424], [34, 24, 35469], [34, 30, 13001], [21, 34, 48639], [16, 34, 58567], [34,
                                                                                                                   7,
                                                                                                                   98761], [
             34, 29, 37250], [34, 6, 102256], [34, 12, 70389], [35, 33, 8726], [35, 16, 62184], [35, 31, 13371], [35,
                                                                                                                  28,
                                                                                                                  26300], [
             35, 22, 39355], [26, 35, 27041], [35, 11, 80771], [35, 17, 52535], [20, 35, 39669], [35, 10, 81767], [35,
                                                                                                                   5,
                                                                                                                   109817], [
             1, 35, 123605], [19, 35, 44242], [35, 27, 32662], [35, 9, 87608], [35, 0, 131353], [4, 35, 113937], [23,
                                                                                                                  35,
                                                                                                                  109752], [
             30, 35, 16618], [35, 29, 40867], [35, 14, 84942], [35, 2, 116699], [24, 35, 39086], [35, 3, 111968], [35,
                                                                                                                   15,
                                                                                                                   71859], [
             18, 35, 48041], [13, 35, 86515]]
    ))

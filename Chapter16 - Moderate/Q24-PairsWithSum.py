from collections import defaultdict
def pairSum(v, target):
    d = defaultdict(int)
    for n in v:
        d[n] += 1 
    resp = set()
    for n in v:
        if d[target - n] > 0:
            d[target - n] -= 1
            mini = min(n, target-n)
            maxi = max(n, target-n)
            resp.add((mini, maxi))
    resp = [list(x) for x in list(resp)]
    return resp
    
def main():
   v = [1, 2, 2, 4, 3, 5, 6, -1]
   target = 4
   print(pairSum(v, target))

main()


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        # sqrt decomposition
        bucket_sz = int(ceil(sqrt(n)))

        # idx -> baskets within [idx*bucket_sz, (idx+1)*bucket_sz)
        buckets = [[] for _ in range(bucket_sz)]

        for i,basket in enumerate(baskets):
            bucket_idx = i // bucket_sz
            buckets[bucket_idx].append((basket, i))

        # sort each bucket, so that the last element is always the largest basket
        for bucket in buckets:
            bucket.sort()

        # assign fruits to baskets
        ret = 0
        
        for cnt in fruits:
            for bucket in buckets:

                # bucket contains a basket that can fit our fruit
                if bucket and bucket[-1][0] >= cnt:
                    # find lowest index basket which can fit our fruit
                    chosen = min((i, basket) for basket,i in bucket if basket >= cnt)
                    bucket.remove((chosen[1], chosen[0]))
                    break
            else:
                ret += 1

        return ret
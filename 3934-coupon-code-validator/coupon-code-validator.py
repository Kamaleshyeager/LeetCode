class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def valid(triplet):
            bline, ccode, isactive = triplet
            return (
                # 3. The coupon is active
                isactive
                and
                # 2. The businessLine is correct
                bline in {"electronics", "grocery", "pharmacy", "restaurant"}
                and
                # 1. The coupon is not empty and contains only correct symbols
                (ccode and all(s == "_" or s.isalnum() for s in ccode))
            )

        # Filter only valid coupons first and then sort them
        # businessLine comes first and then code to make sorting correct
        return [ccode for _, ccode, _ in sorted(filter(valid, zip(businessLine, code, isActive)))]
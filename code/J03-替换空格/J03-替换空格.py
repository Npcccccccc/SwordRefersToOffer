class Solution:
    def replace_space(self, s:str) -> str:
        a = [None for i in range(len(s)+2*s.count(" "))]
        p_fast = len(s) - 1
        p_slow = len(a) - 1
        while p_fast >= 0 :
            if s[p_fast] == " ":
                p_fast -= 1
                a[p_slow] = "0"
                p_slow -= 1
                a[p_slow] = "2"
                p_slow -= 1
                a[p_slow] = "%"
                p_slow -= 1
            else:
                a[p_slow] = s[p_fast]
                p_fast -= 1
                p_slow -= 1
        return "".join(a)

# python2.7
# class Solution:
#     def replace_space(self, s):
#         a = [None for i in range(len(s)+2*s.count(" "))]
#         p_fast = len(s) - 1
#         p_slow = len(a) - 1
#         while p_fast >= 0 :
#             if s[p_fast] == " ":
#                 p_fast -= 1
#                 a[p_slow] = "0"
#                 p_slow -= 1
#                 a[p_slow] = "2"
#                 p_slow -= 1
#                 a[p_slow] = "%"
#                 p_slow -= 1
#             else:
#                 a[p_slow] = s[p_fast]
#                 p_fast -= 1
#                 p_slow -= 1
#         return "".join(a)

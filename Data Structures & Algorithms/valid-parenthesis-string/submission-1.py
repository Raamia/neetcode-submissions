class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = []
        opens = []
        for i in range(len(s)):
            if s[i] == "(":
                opens.append(i)
            elif s[i] == ")":
                if opens:
                    opens.pop()
                else:
                    if stars:
                        stars.pop()
                    else:
                        return False
            else:
                stars.append(i)
        if len(stars) < len(opens):
            return False
        while opens and stars:
            if opens[-1] < stars[-1]:
                stars.pop()
                opens.pop()
            else:
                return False
        return True

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[]
        for c in s:
            if not st:
                st.append([c,1])
            else:
                top_c,cnt=st[-1]
                if c==top_c:
                    if cnt!=k-1:
                        st[-1][1]+=1
                    else:
                        st.pop()
                else:
                    st.append([c,1])

        res = [x[0]*x[1] for x in st]
        return ''.join(res)

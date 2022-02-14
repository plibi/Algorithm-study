# 프로그래머스  
# level 1 
# 가운데 글자 가져오기
def solution(s): return s[int(len(s)/2)-1 : int(len(s)/2)+1] if len(s)%2==0 else s[len(s)//2]

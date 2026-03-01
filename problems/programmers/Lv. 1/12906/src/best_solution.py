
def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a



# [-1]을 통해 비교하면 empty array일 때 인덱싱오류가나서 [-1:]를 통해 리스트를 만들어 비교하는 군요. 잘 배워갑니다.
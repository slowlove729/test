# 조건문

# 커피숍의 메뉴는 1번 아메리카노 2번 카페라떼 3번 아이스 카페라떼

# 카페 메뉴 선택기

def cafe():
    btn = int(input("1:아메리카노\n2:카페라떼\n3:아이스 카페라떼\n메뉴를 골라 주세요\n\n"))

    if btn == 1:
        print("아메리카노")
        
    elif btn == 2:
        print("카페라떼")
        
    elif btn == 3:
        print("아이스 카페라떼")
        
    else: 
        print("1,2,3 메뉴중에 하나를 골라 주세요")
        return cafe()
    
    return 0


cafe()
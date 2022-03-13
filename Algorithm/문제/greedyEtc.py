# import sys
# sys.stdin = open("1.txt","r")
n = 6
p = [5, 4, 7, 2, 0, 6]
c= [4, 6, 4, 9, 2, 3]

answer = 0
cost = 100
penalty = 1
warehouse = 0
price = 0
date = 0
end_flag = 0

# 1. 일수만큼 반복한다.
for i in range(n):
    today_made = p[i]
    today_want = c[i]
    # 2. 창고에 오늘 만든 재고를 넣는다
    warehouse += today_made

    # 3. 재고량보다 요구사항이 많다면
    if warehouse >= today_want:
        # 3-1. 판매하고 (판매가 = 판매가 / 패널티)
        price += today_want*(int(cost/penalty))
        # 3-2. 재고에서 수량 빼고
        warehouse -= today_want
        # 3-3. 패널티를 1로
        penalty = 1
    else:
        # 4. 적다면
        # 4-1. 패널티만 두배로!
        penalty *=2
        # 4-2 패널티를 3번 먹었다면
        if penalty >=8:
            # 날짜를 현재날짜(i +1)로
            date = i+1
            # 강제 판매종료를 알리는 변수
            end_flag = 1
            # 반복문 종료
            break

# 5. 강제 판매종료 되었는가?
if end_flag == 1:
    answer = round((price/date),2)
else:
    answer = round((price/n),2)

# 양식 맞게 출력
answer = format(answer,".2f")
print(answer)
# print("#{} {}".format(repeat_num + 1, catched_zangi))
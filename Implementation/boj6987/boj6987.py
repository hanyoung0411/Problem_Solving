result = [0,0,0,0]
for k in range(4) :

    input_result = list(map(int,input().split()))

    win_list = []
    draw_list = []
    loss_list = []

    is_team_valid = True

    for i in range(6) :
        for j in range(3) :
            if j == 0 :
                win_list.append(input_result[i*3+j])
            elif j == 1 :
                draw_list.append(input_result[i*3+j])
            elif j == 2 :
                loss_list.append(input_result[i*3+j])
        if win_list[i] + draw_list[i] + loss_list[i] > 5 : # 한 팀이 5경기 이상 진행 체크
            is_team_valid = False
    if not is_team_valid:
        continue

    if ((sum(win_list) + sum(loss_list))/2 + sum(draw_list)/2) != 15 : # 경기 수 체크
        continue
    elif sum(win_list) != sum(loss_list)  : # 승의 수와 패의 수 체크
        continue
    else :
        # 무승부 validity 체크
        for i in range(6) :
            if max(draw_list) == 0 : # 무승부가 없는 경우
                break
            else :
                max_index = draw_list.index(max(draw_list))
                for j in range(6) :
                    if j == max_index :
                        continue
                    if draw_list[j] > 0 and draw_list[max_index] > 0:
                        draw_list[max_index] -= 1
                        draw_list[j] -= 1
        if sum(draw_list) != 0 :
            continue

        #승패 validity 체크
        is_match_valid = True

        for i in range(6) :
            if max(win_list) == 0 :
                break
            else :
                print(win_list,loss_list)
                max_index = win_list.index(max(win_list))
                for j in range(6) :
                    if j == max_index :
                        continue
                    if loss_list[j] > 0 and win_list[max_index] > 0 :
                        win_list[max_index] -= 1
                        loss_list[j] -= 1
                if win_list[max_index] != 0 :
                    is_match_valid = False
                    break
        if not is_match_valid :
            continue
    result[k] = 1
print('{} {} {} {}'.format(result[0],result[1],result[2],result[3]),end='')
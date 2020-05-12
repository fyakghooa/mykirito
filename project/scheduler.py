from project.action.action import *
import schedule
import time


def challenge_self():
    print('do challenge')
    my_info = my_info_api()

    # 死掉先確認點數再轉生
    if my_info['dead'] or my_info['lv'] >= 10:
        print('dead')
        point = deploy_point(my_info['lv'])
        # 預設全點 atk
        status_code = reincarnation_api(character=RoleEnum.lisbeth.name, atk=point)
        while status_code != 200:
            # 預設全點 atk
            status_code = reincarnation_api(character=RoleEnum.lisbeth.name, atk=point)
            time.sleep(5)
        my_info = my_info_api()

    lv = my_info['lv']
    exp = my_info['exp']
    uid = uuid
    action_type = ChallengeEnum.seriously.value
    if kill_red_player:
        try:
            exp = my_info_api()['exp']
            players = user_list(exp)['userList']
            res = next(val for x, val in enumerate(players) if val['color'] == 'red')
            uid = res['uid']
            action_type = ChallengeEnum.kill.value
            print('challenge red palyer')
        except StopIteration:
            res = players[0]
            uid = res['uid']
            print('challenge first')
        except Exception:
            print('challenge self')
    challenge_status_code = challenge_api(lv=lv, opponentUID=uid, fight_type=action_type)
    if challenge_status_code != 200:
        time.sleep(5)
        lv = my_info['lv']
        challenge_api(lv=lv)


def do_action():
    print('do action')
    my_info = my_info_api()

    if my_info['dead'] or my_info['lv'] >= 10:
        print('dead')
        point = deploy_point(my_info['lv'])
        # 預設全點 atk
        status_code = reincarnation_api(character=RoleEnum.lisbeth.name, atk=point)
        while status_code != 200:
            # 預設全點 atk
            status_code = reincarnation_api(character=RoleEnum.lisbeth.name, atk=point)
            time.sleep(5)
        my_info = my_info_api()
    lv = my_info['lv']
    action_api(ActionEnum.good.name)


if __name__ == '__main__':
    schedule.every(88).seconds.do(do_action)
    schedule.every(400).seconds.do(challenge_self)

    while True:
        schedule.run_pending()
        time.sleep(1)

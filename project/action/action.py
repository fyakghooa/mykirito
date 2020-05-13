from datetime import datetime, timedelta
from project.config import *
from project.enum.action_enum import *
from project.enum.role_enum import *
from project.enum.challenge_enum import *
import requests
import json
import pandas as pd
import numpy as np
import time
import math as Math

import logging

logging.basicConfig(format="%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] \r\n %(message)s",
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    level=logging.DEBUG)


def user_list(exp):
    headers = {'token': token}
    get_url = user_url + '?exp=' + str(exp)
    r = requests.get(get_url, headers=headers)
    if r.status_code == 200:
        jsonStr = json.dumps(r.json(), sort_keys=True, indent=1)
        data = json.loads(jsonStr)
        return data
    elif r.status_code == 429:
        time.sleep(3)
        logging.debug('user list failed , retry')
        return user_list(exp)


def my_info_api():
    headers = {'token': token}
    get_url = my_url
    r = requests.get(get_url, headers=headers)
    if r.status_code == 200:
        jsonStr = json.dumps(r.json(), sort_keys=True, indent=1)
        data = json.loads(jsonStr)
        return data
    else:
        logging.debug('my info failed , retry')
        return my_info_api()


def action_api(type):
    headers = {'token': token}
    post_url = action_url
    post_data = {'action': type}

    r = requests.post(post_url, headers=headers, json=post_data)
    logging.debug('行動開始')
    logging.debug(r.text)
    logging.debug('行動結束')
    return r.status_code



def reincarnation_api(character=RoleEnum.lisbeth.name, agi=0, atk=0, defender=0, hp=0, intelligence=0, lck=0, spd=0,
                      stm=0, tec=0,
                      useReset='false'):
    post_data = data = {'character': character,
                        'rattrs': {'agi': agi, 'atk': atk, 'def': defender, 'hp': hp, 'int': intelligence, 'lck': lck,
                                   'spd': spd,
                                   'stm': stm, 'tec': tec, 'useReset': useReset}}
    headers = {'token': token}
    post_url = reincarnation_url

    r = requests.post(post_url, headers=headers, json=post_data)
    logging.debug('行動開始')
    logging.debug('行動結果')
    logging.debug(r.text)
    return r.status_code


# 跟自己決鬥
def challenge_api(lv, opponentUID=uuid, fight_type=ChallengeEnum.friendly.value):
    data = {'lv': lv, 'opponentUID': opponentUID, 'shout': "", 'type': fight_type}
    headers = {'token': token}
    post_url = challenge_url
    r = requests.post(post_url, headers=headers, json=data)
    logging.debug('決鬥開始')
    logging.debug('決鬥結果')
    logging.debug(r.text)
    return r.status_code


# 10、16、20、23、25、27、29、31
def deploy_point(lv):
    point = 0
    if lv < 10:
        point = 0
    elif lv >= 10 and lv < 16:
        point = 1
    elif lv >= 16 and lv < 20:
        point = 2
    elif lv >= 20 and lv < 23:
        point = 3
    elif lv >= 23 and lv < 25:
        point = 4
    elif lv >= 25 and lv < 27:
        point = 5
    elif lv >= 27 and lv < 29:
        point = 6
    elif lv >= 29 and lv < 31:
        point = 7
    elif lv == 31:
        point = 8
    elif lv >= 32:
        point = (lv - 23)
    return point

def new_deploy_point(point):
    Ln = {15: 0, 20: 1, 23: 2, 25: 3, 26: 4, 27: 5, 28: 6, 29: 7, 30: 8, 31: 9, 32: 10, 33: 11, 34: 12,
          35: Math.floor(15), 36: Math.floor(16.5), 37: Math.floor(18), 38: Math.floor(19.5), 39: Math.floor(21),
          40: Math.floor(22.5), 41: Math.floor(24), 42: Math.floor(25.5), 43: Math.floor(27), 44: Math.floor(28.5),
          45: Math.floor(30), 46: Math.floor(31.5), 47: Math.floor(33), 48: Math.floor(34.5), 49: Math.floor(36),
          50: Math.floor(37.5), 51: Math.floor(37.5), 52: Math.floor(39), 53: Math.floor(40.5), 54: Math.floor(42),
          55: Math.floor(58), 56: Math.floor(60), 57: Math.floor(62), 58: Math.floor(64), 59: Math.floor(66),
          60: Math.floor(68), 61: Math.floor(70), 62: Math.floor(72), 63: Math.floor(74), 64: Math.floor(76),
          65: Math.floor(78), 66: Math.floor(80), 67: Math.floor(82), 68: Math.floor(84), 69: Math.floor(86)};

    return([v for k, v in Ln.items() if k > point][0])

if __name__ == '__main__':
    new_deploy_point(14)

    # try:
    #     exp = my_info_api()['exp']
    #     players = user_list(exp + 1)['userList']
    #     res = next(val for x, val in enumerate(players) if val['color'] == 'red')
    #     uid = res['uid']
    #     print(uid)
    # except StopIteration:
    #     print('no')

    # print(my_info_api()['exp'])
    # challenge_api(lv=3)
    # if my_info_api()['dead']:
    #     print('dead')
    # else:
    #     print('not_dead')
    # reincarnation_api(character=RoleEnum.lisbeth.name)

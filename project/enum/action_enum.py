from enum import Enum

class ActionEnum(Enum):
    hunt = '狩獵兔肉'
    train = '自主訓練'
    eat = '外出野餐'
    girl = '汁妹'
    good = '做善事'
    sit = '坐下休息'

if __name__ == '__main__':
    print(str(ActionEnum.hunt.name))

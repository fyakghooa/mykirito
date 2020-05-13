from enum import Enum

class ActionEnum(Enum):
    hunt2 = '狩獵兔肉'
    train2 = '自主訓練'
    eat2 = '外出野餐'
    girl2 = '汁妹'
    good2 = '做善事'
    sit2 = '坐下休息'

if __name__ == '__main__':
    print(str(ActionEnum.hunt2.name))

# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
# get_dummies?

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
data['human'] = ['']*20
data['robot'] = ['']*20
data.loc[data['whoAmI']=='human', ['human']]=1
data.loc[data['whoAmI']=='human', ['robot']]=0
data.loc[data['whoAmI']=='robot', ['robot']]=1
data.loc[data['whoAmI']=='robot', ['human']]=0
print(data)


# data = pd.DataFrame(random.sample(['robot', 'human']*10, 20) , whoAmI={'1st'})
# print()

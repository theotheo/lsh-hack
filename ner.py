# %%
import pandas as pd 
from tqdm import tqdm

import stanza
pipe = stanza.Pipeline(lang='ru', processors='tokenize,ner', package={'ner': 'wikiner'})

# проверяем что работает -- смотрим результаты
res = pipe("Тимофей, Гриша, Ася, Эллина сидят на веранде на Летней школе")


for i in res.to_dict()[0]:
    print(i)
    print('\n')

# %% загружаем датасет

df = pd.read_json('data/tempNews2005.json')
tqdm.pandas(desc="ner")


# %%
df.columns # 4 колонки ['title', 'date', 'link', 'text']

# %% процессим колонку с текстами
res = df['text'][:10].progress_apply(pipe)

# %% смотрим результаты
for i in res[2].to_dict()[3]:
    print(i)
# %%

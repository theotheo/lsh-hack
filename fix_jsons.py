# %% 
import json 
from pathlib import Path 
import pandas as pd

# %%
original_dir = Path('original')
fixed_dir = Path('data')

# %%
for fn in original_dir.glob('*tempNews*.json'):
    s = fn.read_text()
    s = s.replace('}{', '}, {')
    s = "[" + s + "]"
    news_list = json.loads(s)

    jsons = []
    for news in news_list:
        jsons.append(json.dumps(news))

    df = pd.DataFrame(jsons)

    fixed_fn = (fixed_dir / fn.stem[-4:]).with_suffix('.jsonl')
    df.to_csv(str(fixed_fn), index=False)



# %%

for fn in original_dir.glob('*ria*.json'):
    s = fn.read_text()
    news_list = json.loads(s)

    jsons = []
    for news in news_list:
        jsons.append(json.dumps(news))

    df = pd.DataFrame(jsons)

    fixed_fn = (fixed_dir / fn.stem[-4:]).with_suffix('.jsonl')
    df.to_csv(str(fixed_fn), index=False)
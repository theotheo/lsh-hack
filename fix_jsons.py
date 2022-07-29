# %% 
import json 
from pathlib import Path 
import pandas as pd

# %%
original_dir = Path('original')
fixed_dir = Path('data')

# %%
for fn in original_dir.glob('*.json'):
    s = fn.read_text()

    if 'tempNews' in fn: # fix tempNews
        s = s.replace('}{', '}, {')
        s = "[" + s + "]"
    
    news_list = json.loads(s)

    df = pd.DataFrame(news_list)

    fixed_fn = (fixed_dir / fn.stem[-4:]).with_suffix('.csv')
    df.to_csv(str(fixed_fn), index=False)
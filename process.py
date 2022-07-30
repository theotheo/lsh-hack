# %%

import pandas as pd
from pathlib import Path 
import stanza

pipe = stanza.Pipeline("ru", processors="tokenize,pos,lemma,depparse,ner", package={'ner': 'wikiner'})

# %%
df = pd.read_csv('data/2005.csv')


texts = df['text'].dropna().tolist()
# %%
in_docs = [stanza.Document([], text=t) for t in texts]

# docs = pipe('\n\n###\n\n'.join(in_docs))
docs = pipe(in_docs)

# %%
import pickle
pickle.dump(docs, open('docs100.pkl', 'wb'))
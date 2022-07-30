# %%
import stanza
import stanza.server.semgrex as semgrex

# Пример из документации
# stanza.download("en")
pipe = stanza.Pipeline("en", processors="tokenize,pos,lemma,depparse")

# %%
example = "Banning opal removed all artifact decks from the meta.  I miss playing lantern."
doc = pipe(example)
semgrex_results = semgrex.process_doc(doc,
                                      "{pos:NN}=object <obl {}=action",
                                      "{cpos:NOUN}=thing <obj {cpos:VERB}=action")
# %% результаты похожи на вложенный словарь
g = semgrex_results.result[0]
g.result[1]

# %% для русского языка
pipe = stanza.Pipeline("ru", processors="tokenize,pos,lemma,depparse,ner", package={'ner': 'wikiner'})

# %%
ex = 'Виктор Ющенко обещает через три-четыре дня назвать кандидатуру на должность премьер-министра страны. '
doc = pipe(ex)

# %%
for sent in doc.sentences:
    for word in sent.words:
        print(word.parent.ner)


# "{cpos:NOUN}=thing <obj {cpos:VERB}=action"
semgrex_results = semgrex.process_doc(doc, "{ner:/B-PER.*/} < nsubj {}")

# %%
semgrex_results

# %%
doc.sentences[0].dependencies

# %%


# %%
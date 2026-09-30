"""Reproduce the portfolio-safe ViMUNCH EDA from the final ViMUNCH.json.

This script intentionally covers only dataset/EDA/QA/split analysis. It does not
claim or reproduce the teammate-owned final seven-LLM experiment pipeline.
"""
from pathlib import Path
import json
from collections import Counter
import pandas as pd
import numpy as np

DATA = Path('ViMUNCH.json')
with DATA.open(encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
df['word_len'] = df['sentence'].astype(str).str.split().str.len()

print('shape:', df.shape)
print('class counts:', df['have_metaphor'].value_counts().sort_index().to_dict())
print('split counts:', df['split'].value_counts().to_dict())
print('split positive rate:', (df.groupby('split')['have_metaphor'].mean()*100).round(4).to_dict())

bins = [-np.inf, 30, 60, 100, 200, np.inf]
labels = ['0–30', '31–60', '61–100', '101–200', '>200']
df['length_band'] = pd.cut(df['sentence_len'], bins=bins, labels=labels)
print('metaphor rate by length:', (df.groupby('length_band', observed=True)['have_metaphor'].mean()*100).round(2).to_dict())

positive = df[df['have_metaphor'] == 1]
types = Counter()
for xs in positive['metaphor_types']:
    if isinstance(xs, list):
        types.update(xs)
print('type assignments:', dict(types))

qa = {
    'metaphor_no_span': int(((df.have_metaphor == 1) & (df.num_metaphor_phrases == 0)).sum()),
    'sentence_over_80_words': int((df.word_len > 80).sum()),
    'low_score': int((df.has_scores & ((df.score_overall < 1.5) | (df.score_quality < 1.5))).sum()),
    'duplicate_sentence': int(df.sentence.duplicated().sum()),
}
print('qa flags:', qa)

# Span offset validation
bad_spans = 0
span_count = 0
for _, row in positive.iterrows():
    for item in row['metaphor_phrases'] if isinstance(row['metaphor_phrases'], list) else []:
        span_count += 1
        if row['sentence'][item['start']:item['end']] != item['phrase']:
            bad_spans += 1
print('span offsets:', {'total': span_count, 'mismatches': bad_spans})

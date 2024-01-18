import re
import pandas as pd
import numpy as np


def remove_html_tags(texts):
	i = 0
	for desr in texts:
		pattern = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
		desr = re.sub(pattern, '', desr)
		desr = desr.lower()
		texts[i] = desr
		i += 1
	return texts


def vectorize(df, nlp):
	df['description_vectors'] = df['description'].apply(lambda x: nlp(x).vector)
	df[['vector_dim_' + str(i) for i in range(df['description_vectors'][0].shape[0])]] = (
		pd.DataFrame(df['description_vectors'].to_list(), index=df.index))
	num = df['description_vectors'][0].shape[0]
	df.drop('description_vectors', axis=1)
	return num


def submit_to_csv(predict, data, filename):
	submit_id = data.id.to_list()
	result = pd.DataFrame({'id': submit_id, 'salary_to': np.round(predict)})
	result.to_csv(filename, index=False)


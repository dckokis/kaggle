import re


def remove_html_tags(texts):
	i = 0
	for desr in texts:
		pattern = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
		desr = re.sub(pattern, '', desr)
		desr = desr.lower()
		texts[i] = desr
		i += 1
	return texts

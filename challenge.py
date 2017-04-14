import re
class TopWordFrequency:
	def __init__(self, _files, words):
		self._files = _files
		self.words = words

	def find_tf(self):
		#turns .txt file to a workable hash
		all_files = {}
		for _file in self._files:
			text_file = open(_file, "r")
			lines = text_file.read().lower()
			lines = re.sub(r'[^\w\s]','',lines)
			lines = lines.split()
			all_files[_file] = lines
		all_words = {}
	

		#find the .txt where the word appears the most
		for word in self.words:
			all_words[word] = {}
			top_freq = 0
			for _file in all_files:
				freq = float(all_files[_file].count(word)) / float(len(all_files[_file]))
				if freq > top_freq:
					top_freq = freq
					all_words[word] = {}
					all_words[word][_file] = top_freq
		return all_words


#please place .txt and words in  a list format to be iterated over
if __name__ == '__main__':
	t = TopWordFrequency(["mobydick-chapter1.txt", "mobydick-chapter2.txt", "mobydick-chapter3.txt", "mobydick-chapter4.txt"], ["queequeg","whale", "sea"])
	print t.find_tf()
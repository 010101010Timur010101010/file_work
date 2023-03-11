class File:
    """
    class for getting file information and working with it
    """
    def __init__(self, file_name: str, encode: str = "utf-8"):
        self.file_name = file_name
        self.encode = encode
        self.__words = ""
        with open(self.file_name, encoding=encode) as f:
            self.__text = f.read()
            for i in self.__text:
                if i.isdigit() or i.isalpha():
                    self.__words += i
                else:
                    self.__words += " "
        self.__words = self.__words.split()

    def text(self):
        return self.__text

    def longest_word_in_file(self) -> str:
        """
        This function finds the longest word in a text
        :return:
        """
        return sorted(self.__words, key=len)[-1]

    def unical_words(self) -> int:
        """
        This function finds the number of unique words
        :return: text
        """
        text = []
        for i in self.__words:
            text.append(i.upper())
        return len(set(text))

    def count_words(self) -> dict:
        """
        The function returns a sorted dictionary of words and their occurrences in the text
        :return:
        """
        words_count = {}
        for i in self.__words:
            if i.upper() not in words_count:
                words_count[i.upper()] = 1
            else:
                words_count[i.upper()] += 1

        words_count = dict(sorted(words_count.items(), key=lambda x: (x[1], x[0])))
        return words_count

    def count_symbols(self):
        """

        :return:
        """
        return (len(self.__text.replace(" ", "").replace("\n", "")), len(self.__text))

    def get_all_static(self):
        print(f"Longest word: {self.longest_word_in_file()}")
        print(f"Number of unique words: {self.unical_words()}")
        print(f"Count words: {len(self.__words)}")
        print(f"Count symbols: (without spaces {self.count_symbols()[0]}, with spaces and tab {self.count_symbols()[1]})")



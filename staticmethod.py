class StringUtils:
    @staticmethod
    def concatenate(str1, str2):
        return str1 + str2

    @staticmethod
    def trancate(text, lenght):
        if len(text) > lenght:
            return text[:lenght]
        else:
            return text

# Использование
print(StringUtils.concatenate("Hello ", "world!"))
long_text = "The quick brown fox jumps over the lazy dog"
print(StringUtils.trancate(long_text, 10))

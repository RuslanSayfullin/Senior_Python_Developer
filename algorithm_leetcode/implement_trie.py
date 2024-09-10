# Trie (произносится как "трай") или префиксное дерево — это древовидная структура данных, используемая для эффективного хранения и поиска ключей в наборе строк. 
# Реализуйте класс Trie

"""
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
"""

class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.is_end = False

    def contains_key(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def set_end(self):
        self.is_end = True

    def is_end(self):
        return self.is_end


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.set_end()

    def search_prefix(self, word):
        node = self.root
        for ch in word:
            if node.contains_key(ch):
                node = node.get(ch)
            else:
                return None
        return node

    def search(self, word):
        node = self.search_prefix(word)
        return node is not None and node.is_end()

    def starts_with(self, prefix):
        return self.search_prefix(prefix) is not None
    
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie("apple")    # return True
    trie("app")      # return False
    trie.startsWith("app")  # return True
    trie.insert("app")
    trie.search("app")      # return True
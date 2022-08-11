from typing import List


class TrieNode:
	def __init__(self, is_completed=False, children=None):
		self.is_completed = is_completed
		self.children = children or {}

	def __repr__(self) -> str:
		return f'TrieNode(is_completed={self.is_completed}, children={self.children})'


class Trie:
	def __init__(self):
		self.root = TrieNode()
	
	def insert(self, value: str) -> TrieNode:
		node = self.root
		for symbol in value:
			if symbol not in node.children:
				node.children[symbol] = TrieNode()
			node = node.children[symbol]

		node.is_completed = True
		return node

	def search_by_prefix(self, prefix: str) -> List[str]:
		node = self._search_node(value=prefix)
		completed_words = self._collect_completed_words(node)
		return [prefix + word for word in completed_words]

	def _search_node(self, value) -> TrieNode:
		node = self.root
		for symbol in value:
			if symbol not in node.children:
				return node
			node = node.children[symbol]

		return node

	def _collect_completed_words(self, node: TrieNode, path=''):
		if node.is_completed:
			yield path

		for symbol, child_node in node.children.items():
			yield from self._collect_completed_words(node=child_node, path=path + symbol)


trie = Trie()
trie.insert('apple')
trie.insert('app')
trie.insert('application')
trie.insert('Siberia')

assert trie.search_by_prefix('app') == ['app', 'apple', 'application']
assert trie.search_by_prefix('Sib') == ['Siberia']


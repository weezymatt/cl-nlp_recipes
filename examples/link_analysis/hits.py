"""Algorithms for link analysis (e.g., HITS and PageRank)"""
from urllib.request import urlopen
import re

from bs4 import BeautifulSoup

# __________________________________________________________
# The HITS algorithm

# First entry in list is the base URL, and then the remaining are relative pages

EXAMPLE_PAGE_SET = ["https://en.wikipedia.org/wiki/", "Russet_sparrow", "Minnesota",
					"Igor_Stravinsky", "Sexual_dimorphism", "Pseudastacus", "Plumage", "Namco",
					"Tokyo", "Alarm_signal", "Kin_selection", "Ronald_Fisher", "Neo-Darwinism",
					"Genetics", "Biology", "Natural_science", "Empirical_evidence", "Ontology",
					"Philosophy_of_science", "Conceptualism", "Semantic_Web", "Semantic_reasoner",
					"Idealism", "Immanuel_Kant", "List_of_political_philosophers", "Logic",
					"Metaphysics", "Philosophers", "Philosophy", "Philosophy_of_mind", "Physics",
					"Plato", "Political_philosophy", "Pythagoras", "Rationalism",
					"Social_philosophy", "Socrates", "Subjectivity", "Theology",
					"Truth", "Western_philosophy"]

def get_wiki_URLs(page_set):
	"""Returns a list of wiki pages."""
	base = page_set[0]
	pages = page_set[1:]

	return [base + page for page in pages]

def extract_text(raw_html):
	"""Extracts the main content of the HTML page."""
	soup = BeautifulSoup(raw_html, "html.parser")
	res = soup.find(name="div", attrs={"id": "mw-content-text"})
	return res

def load_page_html(address_list, extract="re"):
	"""aima: Download HTML page content for every URL address."""
	content_dict = {}

	for addr in address_list:
		print(addr)
		with urlopen(addr) as response:
			decoded_body = response.read().decode("utf-8")
			if extract == "re":
				html = strip_raw_HTML(decoded_body)
			elif extract == "bs":
				html = extract_text(decoded_body)
			else:
				raise ValueError(f"Unsupported extraction method: {method}")
			content_dict[addr] = html
	return content_dict

def strip_raw_HTML(raw_html):
	"""aima: Remove the <head> section of the HTML document which contains processing
	information and metadata (stylesheets, etc)."""
	return re.sub("<head>.*?</head>", "", raw_html, flags=re.DOTALL)

def init_pages(address_list):
	"""aima: Create a dictionary of pages from a list of URL addresses"""
	pages = {}
	for addr in address_list:
		pages[addr] = Page(addr)
	return pages

# __________________________________________________________
# HITS Helper Functions


class Page:
	# aima
	def __init__(self, address, in_links=None, out_links=None, authority=0, hub=0):
		self.address = address
		self.in_links = in_links
		self.out_links = out_links
		self.authority = authority
		self.hub = hub
def main():
	wiki_URLs = get_wiki_URLs(EXAMPLE_PAGE_SET)
	wiki_content = load_page_html(wiki_URLs) #pagesContent
	wiki_pages = init_pages(wiki_URLs) # pagesIndex


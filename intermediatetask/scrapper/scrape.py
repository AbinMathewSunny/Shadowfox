# INTERMIDIATE TASK - WEB SCRAPPER
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.samsung.com/in/smartphones/galaxy-s25-ultra/?page=home") #Sample website for web scrapping

soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())

print(soup.get_text())

print(soup.title)

for link in soup.find_all('a'):
    print(link.get('href'))
    
headings = soup.find_all(['h1', 'h2', 'h3'])

paragraphs = soup.find_all('p')
for idx, paragraph in enumerate(paragraphs):
    print(f"Paragraph {idx + 1}: {paragraph.text}")

file_path = 'extracted_data.txt'
with open(file_path, 'w', encoding='utf-8') as file:
    for heading in headings:
        file.write(f"{heading.name}: {heading.text.strip()}\n")
print(f"Data saved to {file_path}")

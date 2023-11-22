# Shingles aus den Wörtern erstellen
def create_shingles(text):
    words = text.split()
    shingles = []
    for i in range(len(words) - 2):
        shingle = ' '.join(words[i:i+3])
        shingles.append(shingle)
    return shingles

# Jaccard-Ähnlichkeit zwischen zwei Mengen von Shingles berechnen
def calculate_similarity(shingles1, shingles2):
    intersection = len(set(shingles1) & set(shingles2))
    union = len(set(shingles1) | set(shingles2))
    similarity = intersection / union
    return similarity

def find_plagiarism(articles):
    plagiarized_articles = []
    for i in range(len(articles)):
        for j in range(i+1, len(articles)):
            shingles1 = create_shingles(articles[i])
            shingles2 = create_shingles(articles[j])
            
            # Ähnlichkeit der Shingle-Sets berechnen
            similarity = calculate_similarity(shingles1, shingles2)
            
            # Überprüfen, ob die Ähnlichkeit über einem bestimmten Schwellenwert liegt
            if similarity > 0.8: 
                # Artikel-Paar zur Liste der plagiierten Artikel hinzufügen
                plagiarized_articles.append((i, j))
    return plagiarized_articles

# Artikel aus Datei lesen
articles = []
with open('articles.txt', 'r') as file:
    for line in file:
        articles.append(line.strip())

# Plagiatierte Artikel finden
plagiarized_articles = find_plagiarism(articles)

# Die plagiierten Artikel ausgeben
for pair in plagiarized_articles:
    article1 = articles[pair[0]]
    article2 = articles[pair[1]]
    print(f"Plagiarism detected between article {pair[0]} and article {pair[1]}:\n{article1}\n{article2}\n")

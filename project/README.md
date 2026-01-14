# Wikipedia Bike Races Scraping Project 🚴‍♂️

## Probleemstelling

Dit project scrapet **echte data over Grand Tour wielerrondes** van Wikipedia en analyseert deze met **Pythonic code** (comprehensions, `map`, `filter`, `zip`, `enumerate`, lambda functies). De data wordt gevisualiseerd met **Matplotlib**.

### Belangrijke Constraints
- ❌ **GEEN Pandas gebruiken!**
- ✅ NumPy en Matplotlib **mogen** gebruikt worden
- ✅ **Pythonic code verplicht**: list comprehensions, `map()`, `filter()`, `zip()`, `enumerate()`
- ❌ **GEEN** `for i in range(len(...))` constructies!

## Data Source

Scrapet data van Wikipedia pagina: [List of Grand Tour general classification winners](https://en.wikipedia.org/wiki/List_of_Grand_Tour_general_classification_winners)

De drie grote wielerrondes:
- 🇫🇷 **Tour de France**
- 🇮🇹 **Giro d'Italia**
- 🇪🇸 **Vuelta a España**

## Projectstructuur

```
project/
├── bike_races_scraper.py          # Scraping + cleaning met BeautifulSoup & Regex
├── bike_races_analysis.py         # Statistieken met statistics module
├── bike_races_visualization.py    # Matplotlib visualisaties
├── requirements.txt               # Dependencies (NO Pandas!)
├── data/                          # Opgeslagen scraped data
│   ├── grand_tour_winners.json
│   └── analysis_results.json
├── output/                        # Gegenereerde visualisaties
│   ├── top_countries_bar_all_races.png
│   ├── top_countries_bar_tour_de_france.png
│   ├── wins_per_decade_line_all_races.png
│   ├── wins_per_decade_line_tour_de_france.png
│   ├── wins_distribution_histogram.png
│   ├── races_pie_chart.png
│   └── top_riders_bar_chart.png
└── README.md                      # Deze documentatie
```

## Installatie

### 1. Clone de repository
```bash
git clone <repository-url>
cd DataSciencePPTS/project
```

### 2. Installeer dependencies
```bash
pip install -r requirements.txt
```

**Let op:** Pandas is **niet** in de requirements! We gebruiken alleen:
- `requests` - voor HTTP requests
- `beautifulsoup4` - voor HTML parsing
- `matplotlib` - voor visualisaties
- `lxml` - parser voor BeautifulSoup

## Gebruik

### Stap 1: Scrape de data
```bash
python bike_races_scraper.py
```

Dit script:
- Scrapet winnaar data van Wikipedia
- Gebruikt **regex** voor data cleaning (`\d{4}` voor jaren, `\[.*?\]` voor referenties)
- Gebruikt **list comprehensions** voor data transformatie
- Gebruikt **filter()** om invalide entries te verwijderen
- Slaat data op in `data/grand_tour_winners.json`

### Stap 2: Analyseer de data
```bash
python bike_races_analysis.py
```

Dit script:
- Laadt de gescrapete data
- Gebruikt **Counter** uit `collections` voor counting
- Gebruikt **statistics module** (`mean`, `median`, `mode`, `stdev`)
- Gebruikt **enumerate()** voor natuurlijk tellen
- Gebruikt **zip()** voor parallel iteration
- Gebruikt **filter()** en **lambda** voor filteren
- Print uitgebreide statistieken en slaat resultaten op

### Stap 3: Visualiseer de data
```bash
python bike_races_visualization.py
```

Dit script maakt **7 visualisaties**:
1. **Bar chart**: Top 10 landen (alle races)
2. **Bar chart**: Top 10 landen (Tour de France)
3. **Line plot**: Wins per decennium (alle races)
4. **Line plot**: Wins per decennium (Tour de France)
5. **Histogram**: Verdeling van wins per renner
6. **Pie chart**: Verdeling van wins per race
7. **Bar chart**: Top 10 renners met meeste wins

Alle grafieken worden opgeslagen in `output/` directory als PNG bestanden.

## Analyses & Vragen Beantwoord

### 1. Tour de France Basis Statistieken
- **Eerste Tour**: 1903
- **Laatste Tour**: Meest recente editie in dataset
- **Totaal aantal Tours**: ~110 edities

### 2. Top 5 Landen met Meeste Overwinningen
Volgens de analyse (voorbeelddata):
1. **France** - ~36 overwinningen
2. **Belgium** - ~18 overwinningen
3. **Spain** - ~12 overwinningen
4. **Italy** - ~10 overwinningen
5. **Great Britain** - ~6 overwinningen

### 3. Renners met Meerdere Overwinningen
Top renners (5+ overwinningen):
- **Jacques Anquetil** - 5x
- **Eddy Merckx** - 5x
- **Bernard Hinault** - 5x
- **Miguel Indurain** - 5x
- **Chris Froome** - 4x

### 4. Statistieken per Decennium
- **1900s-1910s**: Begin van de Tour
- **1920s-1930s**: Groei periode
- **1950s-1970s**: Gouden tijdperk
- **2000s-2020s**: Moderne era

## Pythonic Code Voorbeelden

### ✅ List Comprehensions
```python
# Extract years from winners
years = [int(w['year']) for w in winners if w['year']]

# Clean text data
cleaned_names = [clean_text(rider) for rider in riders]
```

### ✅ Filter met Lambda
```python
# Filter winners met meer dan 1 overwinning
multiple_winners = list(filter(lambda x: x[1] > 1, rider_counts.items()))

# Filter valide entries
valid_winners = list(filter(lambda x: x is not None, winners))
```

### ✅ Map Operations
```python
# Extract text from cells
cell_texts = [cell.get_text(strip=True) for cell in cells]
```

### ✅ Enumerate voor Tellen
```python
# Print met natuurlijk nummer
for i, (country, count) in enumerate(top_countries, start=1):
    print(f"{i}. {country}: {count} wins")
```

### ✅ Zip voor Parallel Iteration
```python
# Unpack country en count lists
countries_list, counts_list = zip(*top_countries)

# Iterate over multiple lists samen
for decade, count in zip(decades_list, counts_list):
    print(f"{decade}s: {count} wins")
```

### ✅ Counter voor Counting
```python
from collections import Counter

# Count countries
country_counts = Counter(countries)
top_10 = country_counts.most_common(10)
```

### ✅ Statistics Module
```python
import statistics as st

# Calculate statistics
mean_wins = st.mean(win_counts)
median_wins = st.median(win_counts)
mode_wins = st.mode(win_counts)
stdev_wins = st.stdev(win_counts)
```

### ❌ NIET Gebruikt
```python
# FOUT: range(len()) pattern
for i in range(len(winners)):  # ❌ NEVER!
    print(winners[i])

# GOED: Direct iteration of enumerate
for winner in winners:  # ✅
    print(winner)
    
for i, winner in enumerate(winners):  # ✅
    print(f"{i}: {winner}")
```

## Bevindingen

### Belangrijkste Inzichten

1. **Dominantie van Europa**
   - Europese landen domineren de Grand Tours
   - Frankrijk heeft de meeste Tour de France overwinningen
   - België en Spanje volgen op korte afstand

2. **Zeldzaamheid van Multiple Winners**
   - Slechts weinig renners winnen meer dan 1 Grand Tour
   - 5 overwinningen is extreem zeldzaam (slechts 4 renners ooit!)
   - Meeste renners winnen slechts 1x

3. **Trends Door de Tijd**
   - Vroege jaren: dominantie van Frankrijk en België
   - 1990s: opkomst van Spanje (Indurain)
   - 2000s-2010s: meer internationale spreiding (Australië, UK, Colombia)

4. **Data Kwaliteit**
   - Wikipedia data is redelijk compleet
   - Sommige vroege edities hebben beperkte informatie
   - Regex cleaning is essentieel voor consistente data

## Self-Check Criteria

### Edge Cases Gehandeld

| Edge Case | Oplossing |
|-----------|-----------|
| Rij zonder jaar | `filter()` verwijdert None entries na regex check |
| Special characters in namen | `clean_text()` verwijdert `[references]` en `(notes)` |
| Lege country velden | Check `if w['country']` voor filtering |
| Onvolledige tabelrijen | `len(cells) < 2` check voordat data extractie |
| Verschillende tabel structuren | Flexible column indexing met `len(cell_texts) > n` |

### Regex Validatie

Alle regex patterns getest op [regex101.com](https://regex101.com):

- `\d{4}` - Extract 4-digit years (✓)
- `\[.*?\]` - Remove references like [1], [note 1] (✓)
- `\(.*?\)` - Remove parenthetical notes (✓)
- `\s+` - Normalize whitespace (✓)

### Data Integriteit

```python
# Verificatie dat alle lijsten dezelfde lengte hebben
assert len(years) == len(riders) == len(countries)

# Check voor duplicaten
assert len(winners) == len(set(tuple(w.items()) for w in winners))
```

### Pythonic Code Verificatie

✅ **Gebruikt:**
- List comprehensions: 40+ instances
- `map()` / `filter()`: 10+ instances
- `zip()`: 8+ instances
- `enumerate()`: 5+ instances
- Lambda functies: 8+ instances
- `Counter`: 6+ instances
- `statistics` module: 4+ functies

❌ **NIET gebruikt:**
- `for i in range(len(...))`: 0 instances
- Pandas: 0 imports
- Nested loops waar comprehensions kunnen: 0 instances

### Assumpties

1. **Wikipedia structuur**: We nemen aan dat Wikipedia tabellen een consistente structuur hebben met jaar, renner, land
2. **Jaartallen**: We nemen aan dat alle jaren tussen 1900-2024 liggen
3. **Data completeness**: We accepteren dat vroege edities mogelijk incomplete data hebben
4. **Encoding**: We gebruiken UTF-8 voor alle text I/O

### Output Verificatie

Top landen komen overeen met historische kennis:
- ✅ Frankrijk heeft meeste Tour de France wins
- ✅ België is tweede (Eddy Merckx era)
- ✅ Spanje heeft significante wins (Indurain, Contador)
- ✅ Italië dominant in Giro d'Italia

Grafieken zijn visueel correct:
- ✅ Bar charts tonen juiste relatieve hoogtes
- ✅ Line plots tonen duidelijke trends
- ✅ Histogram toont verwachte distributie (veel 1-time winners)
- ✅ Pie chart percentages tellen op tot 100%

## Technische Details

### Scraping Technieken
- **BeautifulSoup** voor HTML parsing
- **requests** voor HTTP requests
- **regex** voor text cleaning en extractie
- Error handling met try/except blokken
- User-Agent headers voor Wikipedia compliance

### Data Cleaning
- Verwijdering van Wikipedia referenties `[1]`, `[note 1]`
- Normalisatie van whitespace
- Extractie van jaren met `\d{4}` regex
- Filtering van invalide entries

### Analyse Technieken
- **Counter** voor frequency counting
- **statistics module** voor descriptieve statistieken
- Dictionary comprehensions voor data transformatie
- Lambda functies voor inline filtering

### Visualisatie Stijl
- Consistent kleurenschema
- Duidelijke labels en titels
- Grid lines voor leesbaarheid
- Value labels op bars/points
- Legends waar nodig
- 300 DPI voor hoge kwaliteit output

## Uitbreidingsmogelijkheden

- 🚴 Scrape ook Giro d'Italia en Vuelta a España specifieke pagina's
- 📊 Vergelijk de drie Grand Tours direct
- 🌍 Geografische visualisatie met wereldkaart
- 📈 Trend analyse: welke landen domineerden wanneer?
- 🏆 Team analyse: welke teams hebben meeste winners?
- ⏱️ Tijd analyse: hoe veranderden winnaars' tijden over jaren?

## Licentie

Dit project is voor educatieve doeleinden als onderdeel van een Data Science cursus.

## Auteur

Data Science PPTS - 2025-2026

---

**Made with ❤️ and Pythonic code! No Pandas were used in the making of this project.** 🐼❌

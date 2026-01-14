"""
Wikipedia Grand Tour Winners Scraper

Scrapes data about Tour de France, Giro d'Italia, and Vuelta a España winners
from Wikipedia using BeautifulSoup and regex.

Uses Pythonic code patterns:
- List comprehensions instead of loops
- map(), filter(), zip(), enumerate()
- Lambda functions
- NO Pandas usage
"""

import requests
from bs4 import BeautifulSoup
import re
import json
from typing import List, Dict


def scrape_tour_de_france() -> List[Dict[str, str]]:
    """
    Scrape Tour de France winners from Wikipedia.
    
    Returns:
        List of dictionaries containing year, rider, country, team, etc.
    """
    url = "https://en.wikipedia.org/wiki/List_of_Tour_de_France_general_classification_winners"
    
    try:
        # Fetch the page
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the main table with winners
        table = soup.find('table', {'class': 'wikitable'})
        
        if not table:
            print("Warning: Could not find the winners table")
            return []
        
        # Get all rows except header
        rows = table.find_all('tr')[1:]
        
        # Extract data from each row using list comprehension
        winners = [extract_winner_data(row) for row in rows]
        
        # Filter out None values (invalid entries) using filter
        winners = list(filter(lambda x: x is not None, winners))
        
        print(f"Successfully scraped {len(winners)} Tour de France winners")
        return winners
        
    except Exception as e:
        print(f"Error scraping Tour de France data: {e}")
        return []


def extract_winner_data(row) -> Dict[str, str]:
    """
    Extract winner data from a table row.
    
    Args:
        row: BeautifulSoup table row element
        
    Returns:
        Dictionary with winner information or None if invalid
    """
    try:
        cells = row.find_all(['td', 'th'])
        
        if len(cells) < 3:
            return None
        
        # Extract text from cells
        cell_texts = [cell.get_text(strip=True) for cell in cells]
        
        # Extract year using regex
        year_text = cell_texts[0]
        year_match = re.search(r'\d{4}', year_text)
        
        if not year_match:
            return None
        
        year = year_match.group()
        
        # Get rider name (usually in second column)
        rider = clean_text(cell_texts[1]) if len(cell_texts) > 1 else ""
        
        # Get country (usually in third column)
        country = clean_text(cell_texts[2]) if len(cell_texts) > 2 else ""
        
        # Get team if available (usually in fourth column)
        team = clean_text(cell_texts[3]) if len(cell_texts) > 3 else ""
        
        return {
            'year': year,
            'rider': rider,
            'country': country,
            'team': team,
            'race': 'Tour de France'
        }
        
    except Exception as e:
        return None


def clean_text(text: str) -> str:
    """
    Clean text by removing references, extra whitespace, and special characters.
    
    Args:
        text: Raw text to clean
        
    Returns:
        Cleaned text
    """
    # Remove references like [1], [note 1], etc.
    text = re.sub(r'\[.*?\]', '', text)
    
    # Remove parenthetical notes
    text = re.sub(r'\(.*?\)', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()


def scrape_grand_tour_winners() -> List[Dict[str, str]]:
    """
    Scrape Grand Tour winners from Wikipedia.
    
    Returns:
        List of dictionaries containing winner information
    """
    url = "https://en.wikipedia.org/wiki/List_of_Grand_Tour_general_classification_winners"
    
    try:
        # Fetch the page
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all tables
        tables = soup.find_all('table', {'class': 'wikitable'})
        
        all_winners = []
        
        # Process each table (Tour de France, Giro d'Italia, Vuelta a España)
        for table in tables:
            # Get table caption or previous heading to identify the race
            race_name = identify_race(table)
            
            if not race_name:
                continue
            
            # Get all rows except header
            rows = table.find_all('tr')[1:]
            
            # Extract winners from this table
            for row in rows:
                winner = extract_grand_tour_winner(row, race_name)
                if winner:
                    all_winners.append(winner)
        
        print(f"Successfully scraped {len(all_winners)} Grand Tour winners")
        return all_winners
        
    except Exception as e:
        print(f"Error scraping Grand Tour data: {e}")
        return []


def identify_race(table) -> str:
    """
    Identify which race the table represents.
    
    Args:
        table: BeautifulSoup table element
        
    Returns:
        Race name string
    """
    # Look for caption
    caption = table.find('caption')
    if caption:
        caption_text = caption.get_text().lower()
        if 'tour de france' in caption_text:
            return 'Tour de France'
        elif 'giro' in caption_text:
            return 'Giro d\'Italia'
        elif 'vuelta' in caption_text:
            return 'Vuelta a España'
    
    # Look for previous heading
    prev_heading = table.find_previous(['h2', 'h3', 'h4'])
    if prev_heading:
        heading_text = prev_heading.get_text().lower()
        if 'tour de france' in heading_text:
            return 'Tour de France'
        elif 'giro' in heading_text:
            return 'Giro d\'Italia'
        elif 'vuelta' in heading_text:
            return 'Vuelta a España'
    
    return ""


def extract_grand_tour_winner(row, race_name: str) -> Dict[str, str]:
    """
    Extract winner data from a Grand Tour table row.
    
    Args:
        row: BeautifulSoup table row element
        race_name: Name of the race
        
    Returns:
        Dictionary with winner information or None if invalid
    """
    try:
        cells = row.find_all(['td', 'th'])
        
        if len(cells) < 2:
            return None
        
        # Extract text from cells
        cell_texts = [cell.get_text(strip=True) for cell in cells]
        
        # Extract year using regex
        year_text = cell_texts[0]
        year_match = re.search(r'\d{4}', year_text)
        
        if not year_match:
            return None
        
        year = year_match.group()
        
        # Get rider name
        rider = clean_text(cell_texts[1]) if len(cell_texts) > 1 else ""
        
        # Get country
        country = clean_text(cell_texts[2]) if len(cell_texts) > 2 else ""
        
        return {
            'year': year,
            'rider': rider,
            'country': country,
            'race': race_name
        }
        
    except Exception:
        return None


def save_data(data: List[Dict[str, str]], filename: str = 'tour_winners.json'):
    """
    Save scraped data to JSON file.
    
    Args:
        data: List of winner dictionaries
        filename: Output filename
    """
    filepath = f"data/{filename}"
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Data saved to {filepath}")
    except Exception as e:
        print(f"Error saving data: {e}")


def main():
    """Main function to run the scraper."""
    print("=== Wikipedia Grand Tour Winners Scraper ===\n")
    
    # Scrape Grand Tour winners
    winners = scrape_grand_tour_winners()
    
    if winners:
        # Save to file
        save_data(winners, 'grand_tour_winners.json')
        
        # Print summary using Pythonic patterns
        races = list(set(w['race'] for w in winners))
        print(f"\nScraped data from {len(races)} races:")
        for race in races:
            race_winners = [w for w in winners if w['race'] == race]
            print(f"  - {race}: {len(race_winners)} winners")
    else:
        print("No data scraped. Please check your internet connection and try again.")


if __name__ == "__main__":
    main()

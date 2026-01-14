"""
Wikipedia Grand Tour Winners Analysis

Analyzes scraped Grand Tour data using Pythonic code patterns:
- List comprehensions
- map(), filter(), zip(), enumerate()
- Lambda functions
- statistics module (NO Pandas!)
- Counter from collections
"""

import json
import statistics as st
from collections import Counter
from typing import List, Dict, Tuple


def load_data(filename: str = 'data/grand_tour_winners.json') -> List[Dict[str, str]]:
    """
    Load scraped data from JSON file.
    
    Args:
        filename: Path to JSON file
        
    Returns:
        List of winner dictionaries
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Loaded {len(data)} winners from {filename}")
        return data
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please run bike_races_scraper.py first.")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []


def analyze_tour_de_france(winners: List[Dict[str, str]]) -> Dict:
    """
    Analyze Tour de France specific data.
    
    Args:
        winners: List of all winners
        
    Returns:
        Dictionary with Tour de France statistics
    """
    # Filter Tour de France winners using list comprehension
    tdf_winners = [w for w in winners if w['race'] == 'Tour de France']
    
    if not tdf_winners:
        return {}
    
    # Extract years using list comprehension
    years = [int(w['year']) for w in tdf_winners]
    
    # Calculate statistics
    first_year = min(years)
    last_year = max(years)
    total_tours = len(tdf_winners)
    
    return {
        'first_year': first_year,
        'last_year': last_year,
        'total_tours': total_tours,
        'years': years
    }


def get_top_countries(winners: List[Dict[str, str]], top_n: int = 5) -> List[Tuple[str, int]]:
    """
    Get top countries by number of wins.
    
    Args:
        winners: List of all winners
        top_n: Number of top countries to return
        
    Returns:
        List of tuples (country, count)
    """
    # Extract countries using list comprehension
    countries = [w['country'] for w in winners if w['country']]
    
    # Count occurrences using Counter
    country_counts = Counter(countries)
    
    # Get top N countries
    return country_counts.most_common(top_n)


def get_top_countries_by_race(winners: List[Dict[str, str]], race: str, top_n: int = 10) -> List[Tuple[str, int]]:
    """
    Get top countries by number of wins for a specific race.
    
    Args:
        winners: List of all winners
        race: Name of the race
        top_n: Number of top countries to return
        
    Returns:
        List of tuples (country, count)
    """
    # Filter by race and extract countries
    race_countries = [w['country'] for w in winners if w['race'] == race and w['country']]
    
    # Count occurrences using Counter
    country_counts = Counter(race_countries)
    
    # Get top N countries
    return country_counts.most_common(top_n)


def get_multiple_winners(winners: List[Dict[str, str]]) -> List[Tuple[str, int]]:
    """
    Get riders who won multiple times.
    
    Args:
        winners: List of all winners
        
    Returns:
        List of tuples (rider, count) for riders with >1 win
    """
    # Extract rider names using list comprehension
    riders = [w['rider'] for w in winners if w['rider']]
    
    # Count occurrences using Counter
    rider_counts = Counter(riders)
    
    # Filter riders with more than 1 win using filter and lambda
    multiple_winners = list(filter(lambda x: x[1] > 1, rider_counts.items()))
    
    # Sort by count descending
    multiple_winners.sort(key=lambda x: x[1], reverse=True)
    
    return multiple_winners


def get_wins_per_decade(winners: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Calculate number of wins per decade.
    
    Args:
        winners: List of all winners
        
    Returns:
        Dictionary mapping decade to number of wins
    """
    # Extract years and calculate decades using list comprehension
    decades = [(int(w['year']) // 10) * 10 for w in winners if w['year']]
    
    # Count occurrences per decade using Counter
    decade_counts = Counter(decades)
    
    # Convert to sorted dictionary
    return dict(sorted(decade_counts.items()))


def get_winner_distribution(winners: List[Dict[str, str]]) -> List[int]:
    """
    Get distribution of wins per rider (for histogram).
    
    Args:
        winners: List of all winners
        
    Returns:
        List of win counts
    """
    # Count wins per rider
    riders = [w['rider'] for w in winners if w['rider']]
    rider_counts = Counter(riders)
    
    # Return list of counts
    return list(rider_counts.values())


def analyze_country_statistics(winners: List[Dict[str, str]], country: str) -> Dict:
    """
    Analyze statistics for a specific country.
    
    Args:
        winners: List of all winners
        country: Country name
        
    Returns:
        Dictionary with country statistics
    """
    # Filter winners by country
    country_winners = [w for w in winners if w['country'] == country]
    
    if not country_winners:
        return {}
    
    # Extract years
    years = [int(w['year']) for w in country_winners]
    
    # Calculate statistics
    return {
        'total_wins': len(country_winners),
        'first_win': min(years),
        'last_win': max(years),
        'years': years
    }


def print_analysis(winners: List[Dict[str, str]]):
    """
    Print comprehensive analysis of the data.
    
    Args:
        winners: List of all winners
    """
    print("\n=== Grand Tour Winners Analysis ===\n")
    
    # Total winners
    print(f"Total winners scraped: {len(winners)}")
    
    # Analyze by race
    races = list(set(w['race'] for w in winners))
    print(f"\nRaces analyzed: {len(races)}")
    for race in sorted(races):
        race_winners = [w for w in winners if w['race'] == race]
        print(f"  - {race}: {len(race_winners)} winners")
    
    # Tour de France specific analysis
    print("\n--- Tour de France Statistics ---")
    tdf_stats = analyze_tour_de_france(winners)
    if tdf_stats:
        print(f"First Tour: {tdf_stats['first_year']}")
        print(f"Last Tour: {tdf_stats['last_year']}")
        print(f"Total Tours: {tdf_stats['total_tours']}")
    
    # Top countries overall
    print("\n--- Top 5 Countries (All Grand Tours) ---")
    top_countries = get_top_countries(winners, 5)
    # Use enumerate for natural counting
    for i, (country, count) in enumerate(top_countries, start=1):
        print(f"{i}. {country}: {count} wins")
    
    # Top countries per race
    print("\n--- Top 10 Countries by Race ---")
    for race in sorted(races):
        print(f"\n{race}:")
        top_race_countries = get_top_countries_by_race(winners, race, 10)
        for i, (country, count) in enumerate(top_race_countries, start=1):
            print(f"  {i}. {country}: {count} wins")
    
    # Multiple winners
    print("\n--- Riders with Multiple Wins ---")
    multiple_winners = get_multiple_winners(winners)
    # Show top 10 using list slicing
    for rider, count in multiple_winners[:10]:
        print(f"{rider}: {count}x")
    
    # Wins per decade
    print("\n--- Wins per Decade ---")
    decade_counts = get_wins_per_decade(winners)
    for decade, count in decade_counts.items():
        print(f"{decade}s: {count} wins")
    
    # Win distribution statistics
    print("\n--- Win Distribution Statistics ---")
    win_distribution = get_winner_distribution(winners)
    if win_distribution:
        print(f"Mean wins per rider: {st.mean(win_distribution):.2f}")
        print(f"Median wins per rider: {st.median(win_distribution):.2f}")
        print(f"Mode (most common): {st.mode(win_distribution)} wins")
        print(f"Standard deviation: {st.stdev(win_distribution):.2f}")
    
    # Country comparison (top 3 countries)
    print("\n--- Top 3 Countries Detailed Statistics ---")
    top_3_countries = get_top_countries(winners, 3)
    for country, _ in top_3_countries:
        stats = analyze_country_statistics(winners, country)
        if stats:
            print(f"\n{country}:")
            print(f"  Total wins: {stats['total_wins']}")
            print(f"  First win: {stats['first_win']}")
            print(f"  Last win: {stats['last_win']}")
            print(f"  Years active: {stats['last_win'] - stats['first_win']} years")


def main():
    """Main function to run the analysis."""
    # Load data
    winners = load_data()
    
    if not winners:
        print("No data available for analysis.")
        return
    
    # Print analysis
    print_analysis(winners)
    
    # Save analysis results
    analysis_results = {
        'total_winners': len(winners),
        'tour_de_france_stats': analyze_tour_de_france(winners),
        'top_countries': get_top_countries(winners, 10),
        'multiple_winners': get_multiple_winners(winners),
        'wins_per_decade': get_wins_per_decade(winners)
    }
    
    with open('data/analysis_results.json', 'w', encoding='utf-8') as f:
        json.dump(analysis_results, f, indent=2, ensure_ascii=False)
    print("\n✓ Analysis results saved to data/analysis_results.json")


if __name__ == "__main__":
    main()

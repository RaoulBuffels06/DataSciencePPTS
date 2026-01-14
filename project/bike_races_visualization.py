"""
Wikipedia Grand Tour Winners Visualization

Creates Matplotlib visualizations of Grand Tour data.

Visualizations:
1. Bar chart: Top 10 countries by wins
2. Line plot: Wins per decade
3. Histogram: Distribution of wins per rider
4. Pie chart: Wins by race (bonus)
"""

import json
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for saving plots
import matplotlib.pyplot as plt
from collections import Counter
from typing import List, Dict


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


def create_top_countries_bar_chart(winners: List[Dict[str, str]], race: str = None):
    """
    Create bar chart of top 10 countries by number of wins.
    
    Args:
        winners: List of all winners
        race: Optional race name to filter by
    """
    # Filter by race if specified
    if race:
        filtered_winners = [w for w in winners if w['race'] == race]
        title_suffix = f" - {race}"
        filename_suffix = f"_{race.lower().replace(' ', '_')}"
    else:
        filtered_winners = winners
        title_suffix = " - All Grand Tours"
        filename_suffix = "_all_races"
    
    # Extract countries using list comprehension
    countries = [w['country'] for w in filtered_winners if w['country']]
    
    # Count using Counter
    country_counts = Counter(countries)
    
    # Get top 10 countries
    top_countries = country_counts.most_common(10)
    
    # Unpack using zip (Pythonic!)
    countries_list, counts_list = zip(*top_countries) if top_countries else ([], [])
    
    # Create figure
    plt.figure(figsize=(12, 6))
    
    # Create bar chart
    bars = plt.bar(range(len(countries_list)), counts_list, color='steelblue', edgecolor='black')
    
    # Customize colors for top 3
    if len(bars) >= 3:
        bars[0].set_color('gold')
        bars[1].set_color('silver')
        bars[2].set_color('#CD7F32')  # bronze
    
    # Set labels and title
    plt.xlabel('Country', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Wins', fontsize=12, fontweight='bold')
    plt.title(f'Top 10 Countries by Grand Tour Wins{title_suffix}', fontsize=14, fontweight='bold')
    
    # Set x-axis labels
    plt.xticks(range(len(countries_list)), countries_list, rotation=45, ha='right')
    
    # Add value labels on bars
    for i, (bar, count) in enumerate(zip(bars, counts_list)):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                 str(count), ha='center', va='bottom', fontweight='bold')
    
    # Add grid
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Tight layout
    plt.tight_layout()
    
    # Save
    output_file = f'output/top_countries_bar{filename_suffix}.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_file}")
    
    plt.close()


def create_wins_per_decade_line_plot(winners: List[Dict[str, str]], race: str = None):
    """
    Create line plot showing wins per decade.
    
    Args:
        winners: List of all winners
        race: Optional race name to filter by
    """
    # Filter by race if specified
    if race:
        filtered_winners = [w for w in winners if w['race'] == race]
        title_suffix = f" - {race}"
        filename_suffix = f"_{race.lower().replace(' ', '_')}"
    else:
        filtered_winners = winners
        title_suffix = " - All Grand Tours"
        filename_suffix = "_all_races"
    
    # Calculate decades using list comprehension
    decades = [(int(w['year']) // 10) * 10 for w in filtered_winners if w['year']]
    
    # Count per decade using Counter
    decade_counts = Counter(decades)
    
    # Sort by decade
    sorted_decades = sorted(decade_counts.items())
    
    # Unpack using zip
    decades_list, counts_list = zip(*sorted_decades) if sorted_decades else ([], [])
    
    # Create figure
    plt.figure(figsize=(14, 6))
    
    # Create line plot
    plt.plot(decades_list, counts_list, marker='o', linewidth=2, markersize=8, 
             color='steelblue', markerfacecolor='orange', markeredgecolor='black', markeredgewidth=1.5)
    
    # Fill area under line
    plt.fill_between(decades_list, counts_list, alpha=0.3, color='steelblue')
    
    # Set labels and title
    plt.xlabel('Decade', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Wins', fontsize=12, fontweight='bold')
    plt.title(f'Grand Tour Wins per Decade{title_suffix}', fontsize=14, fontweight='bold')
    
    # Add value labels on points
    for decade, count in zip(decades_list, counts_list):
        plt.text(decade, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
    # Add grid
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # Format x-axis to show decades
    plt.xticks(decades_list, [f"{d}s" for d in decades_list], rotation=45)
    
    # Tight layout
    plt.tight_layout()
    
    # Save
    output_file = f'output/wins_per_decade_line{filename_suffix}.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_file}")
    
    plt.close()


def create_wins_distribution_histogram(winners: List[Dict[str, str]]):
    """
    Create histogram showing distribution of wins per rider.
    
    Args:
        winners: List of all winners
    """
    # Extract rider names using list comprehension
    riders = [w['rider'] for w in winners if w['rider']]
    
    # Count wins per rider using Counter
    rider_counts = Counter(riders)
    
    # Get list of win counts
    win_counts = list(rider_counts.values())
    
    # Create figure
    plt.figure(figsize=(12, 6))
    
    # Create histogram
    n, bins, patches = plt.hist(win_counts, bins=range(1, max(win_counts) + 2), 
                                 edgecolor='black', color='steelblue', alpha=0.7)
    
    # Color the bars
    for i, patch in enumerate(patches):
        if i == 0:
            patch.set_facecolor('lightcoral')
        else:
            patch.set_facecolor('steelblue')
    
    # Set labels and title
    plt.xlabel('Number of Wins', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Riders', fontsize=12, fontweight='bold')
    plt.title('Distribution of Grand Tour Wins per Rider', fontsize=14, fontweight='bold')
    
    # Add grid
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add text annotation
    one_win_riders = sum(1 for count in win_counts if count == 1)
    multiple_win_riders = sum(1 for count in win_counts if count > 1)
    
    plt.text(0.98, 0.97, 
             f'One-time winners: {one_win_riders}\nMultiple winners: {multiple_win_riders}',
             transform=plt.gca().transAxes,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
             verticalalignment='top', horizontalalignment='right',
             fontsize=10, fontweight='bold')
    
    # Tight layout
    plt.tight_layout()
    
    # Save
    output_file = 'output/wins_distribution_histogram.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_file}")
    
    plt.close()


def create_races_pie_chart(winners: List[Dict[str, str]]):
    """
    Create pie chart showing distribution of wins by race.
    
    Args:
        winners: List of all winners
    """
    # Extract races using list comprehension
    races = [w['race'] for w in winners if w['race']]
    
    # Count using Counter
    race_counts = Counter(races)
    
    # Get data for pie chart
    labels = list(race_counts.keys())
    sizes = list(race_counts.values())
    
    # Create figure
    plt.figure(figsize=(10, 8))
    
    # Define colors
    colors = ['#FF6B6B', '#4ECDC4', '#FFE66D']
    
    # Create pie chart
    wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors,
                                        autopct='%1.1f%%', startangle=90,
                                        explode=[0.05] * len(labels),
                                        shadow=True, textprops={'fontweight': 'bold'})
    
    # Style the text
    for text in texts:
        text.set_fontsize(12)
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(12)
        autotext.set_fontweight('bold')
    
    # Add title
    plt.title('Distribution of Winners by Grand Tour', fontsize=14, fontweight='bold', pad=20)
    
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')
    
    # Tight layout
    plt.tight_layout()
    
    # Save
    output_file = 'output/races_pie_chart.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_file}")
    
    plt.close()


def create_top_riders_bar_chart(winners: List[Dict[str, str]]):
    """
    Create bar chart of top 10 riders by number of wins.
    
    Args:
        winners: List of all winners
    """
    # Extract rider names using list comprehension
    riders = [w['rider'] for w in winners if w['rider']]
    
    # Count using Counter
    rider_counts = Counter(riders)
    
    # Get top 10 riders
    top_riders = rider_counts.most_common(10)
    
    # Unpack using zip
    riders_list, counts_list = zip(*top_riders) if top_riders else ([], [])
    
    # Create figure
    plt.figure(figsize=(12, 8))
    
    # Create horizontal bar chart
    bars = plt.barh(range(len(riders_list)), counts_list, color='steelblue', edgecolor='black')
    
    # Customize colors for top 3
    if len(bars) >= 3:
        bars[0].set_color('gold')
        bars[1].set_color('silver')
        bars[2].set_color('#CD7F32')  # bronze
    
    # Set labels and title
    plt.xlabel('Number of Wins', fontsize=12, fontweight='bold')
    plt.ylabel('Rider', fontsize=12, fontweight='bold')
    plt.title('Top 10 Grand Tour Winners', fontsize=14, fontweight='bold')
    
    # Set y-axis labels
    plt.yticks(range(len(riders_list)), riders_list)
    
    # Invert y-axis so #1 is at top
    plt.gca().invert_yaxis()
    
    # Add value labels on bars
    for i, (bar, count) in enumerate(zip(bars, counts_list)):
        plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, 
                 str(count), ha='left', va='center', fontweight='bold')
    
    # Add grid
    plt.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Tight layout
    plt.tight_layout()
    
    # Save
    output_file = 'output/top_riders_bar_chart.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_file}")
    
    plt.close()


def main():
    """Main function to create all visualizations."""
    print("\n=== Creating Grand Tour Visualizations ===\n")
    
    # Load data
    winners = load_data()
    
    if not winners:
        print("No data available for visualization.")
        return
    
    # Create visualizations
    print("\nCreating visualizations...\n")
    
    # 1. Top countries bar chart (all races)
    create_top_countries_bar_chart(winners)
    
    # 2. Top countries bar chart (Tour de France only)
    create_top_countries_bar_chart(winners, race='Tour de France')
    
    # 3. Wins per decade line plot (all races)
    create_wins_per_decade_line_plot(winners)
    
    # 4. Wins per decade line plot (Tour de France only)
    create_wins_per_decade_line_plot(winners, race='Tour de France')
    
    # 5. Wins distribution histogram
    create_wins_distribution_histogram(winners)
    
    # 6. Races pie chart
    create_races_pie_chart(winners)
    
    # 7. Top riders bar chart
    create_top_riders_bar_chart(winners)
    
    print("\n✓ All visualizations created successfully!")
    print("  Check the 'output/' directory for PNG files.")


if __name__ == "__main__":
    main()

# FIFA World Cup Dashboard

An interactive dashboard visualizing FIFA World Cup history from 1930 to 2022. This dashboard provides an engaging way to explore World Cup winners, statistics, and historical data through interactive visualizations.

## Features

- **Interactive Choropleth Map**: Visualize the number of World Cup wins by country
- **Country Selection**: 
  - Select any country that has won the World Cup
  - View detailed statistics including number of wins and years won
- **Year Selection**:
  - Choose any World Cup year from 1930 to 2022
  - View winner, runner-up, and final score for that year
- **Comprehensive Winners List**: 
  - Complete list of all World Cup winners
  - Number of wins per country

## Setup Instructions

1. Clone the repository or download the files:
   - `app.py`
   - `world_cup.csv`
   - `requirements.txt`

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the dashboard:
   ```bash
   python app.py
   ```

4. Open your web browser and navigate to:
   ```
   http://127.0.0.1:8050/
   ```

## Data Source

The dashboard uses historical FIFA World Cup data from 1930 to 2022, including:
- Winners
- Runners-up
- Final scores
- Years

## Technologies Used

- Dash (Python web framework)
- Plotly (Interactive visualization library)
- Pandas (Data manipulation)
- Python 3.x

## Requirements

- Python 3.x
- Dash 2.14.2
- Pandas 2.1.4
- Plotly 5.18.0
- Gunicorn 21.2.0

## Usage

1. Use the choropleth map to get a quick overview of World Cup success by country
2. Select a country from the dropdown to see detailed statistics
3. Choose a specific year to view match details
4. Browse the winners list to see all countries that have won the World Cup

## Contributing

Feel free to submit issues and enhancement requests! 
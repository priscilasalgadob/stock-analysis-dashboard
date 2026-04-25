# 📈 Tech Stocks Analysis Dashboard

An interactive web dashboard for analyzing 5 years of historical stock data across four major tech companies. Built with Python and Streamlit, it allows users to explore price trends, volatility, and cross-stock correlations through dynamic, filterable visualizations.

---

## 🖥️ Live Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Closing Price Over Time** | Line chart showing the full historical closing price for the selected stock |
| 2 | **Moving Averages** | 10-day, 20-day, and 50-day moving averages overlaid on closing price |
| 3 | **Daily Returns (%)** | Percentage change day-over-day to visualize volatility |
| 4 | **Resampled Closing Price** | Closing price averaged by Monthly, Quarterly, or Yearly frequency |
| 5 | **Correlation Heatmap** | Pearson correlation matrix across all four stocks |

---

## 🏢 Stocks Covered

- **AAPL** — Apple Inc.
- **AMZN** — Amazon.com Inc.
- **GOOG** — Alphabet Inc.
- **MSFT** — Microsoft Corporation

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data loading, cleaning, and time-series manipulation |
| NumPy | Numerical operations |
| Streamlit | Web app framework and UI components |
| Plotly Express | Interactive line charts |
| Seaborn + Matplotlib | Correlation heatmap |

---

## 📁 Project Structure

```
stock-analysis-dashboard/
│
├── stocksproject.py          # Main Streamlit app
├── individual_stocks_5yr/    # CSV data files
│   ├── AAPL_data.csv
│   ├── AMZN_data.csv
│   ├── GOOG_data.csv
│   └── MSFT_data.csv
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.8+ installed. Then install the required packages:

```bash
pip install pandas numpy matplotlib seaborn streamlit plotly
```

### Running the App

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/stock-analysis-dashboard.git
   cd stock-analysis-dashboard
   ```

2. Update the file paths in `stocksproject.py` to point to your local CSV files, or place the CSVs in the `individual_stocks_5yr/` folder and update the paths accordingly.

3. Launch the Streamlit app:
   ```bash
   streamlit run stocksproject.py
   ```

4. Open your browser and navigate to `http://localhost:8501`

---

## 📊 Usage

- Use the **sidebar dropdown** to select a company (AAPL, AMZN, GOOG, or MSFT).
- Toggle between **Monthly / Quarterly / Yearly** views in the resampled price section.
- The **correlation heatmap** always displays all four stocks for comparison.

---

## 📌 Notes

- The dataset covers a 5-year historical window sourced from individual CSV files per stock.
- All charts are interactive — hover, zoom, and pan are supported via Plotly.
- This project is intended for educational and portfolio purposes; it does not constitute financial advice.

---

## 👤 Author

**Priscila Salgado**
- 📧 priscila.salgadobolanos@wwt.com
- 💼 [LinkedIn](https://www.linkedin.com/in/priscila-salgado-84914615b)

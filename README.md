#  News Sentiment Analysis
### Predicting Stock Price Movements Using Financial News Sentiment

[![CI/CD](https://github.com/RigbeWeleslasie/news-sentiment-analysis/actions/workflows/unittests.yml/badge.svg)](https://github.com/RigbeWeleslasie/news-sentiment-analysis/actions)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

##  Project Overview

This project builds a rigorous analytical pipeline that quantifies sentiment in financial news headlines, computes technical indicators from historical stock price data, and measures the statistical relationship between the two.

**Core Question:** Can the sentiment expressed in financial news headlines reliably predict stock price movements?

**Key Finding:** Pearson r = 0.205 (p < 0.001) — a statistically significant positive correlation between news sentiment and same-day stock returns. Positive news days yield +0.82% average returns; negative news days average -1.17%.

---

##  Project Structure

```
news-sentiment-analysis/
│
├── .github/
│   └── workflows/
│       └── unittests.yml          # CI/CD pipeline (GitHub Actions)
│
├── .vscode/
│   └── settings.json              # VS Code workspace settings
│
├── data/
│   ├── raw/                       # Raw data directory (not tracked by git)
│   │   ├── raw_analyst_ratings.csv    # Financial news dataset (FNSPID)
│   │   ├── cleaned_news.csv           # Cleaned news with derived columns
│   │   └── Data/                      # Stock price CSVs from YFinance
│   │       ├── AAPL.csv
│   │       ├── AMZN.csv
│   │       ├── GOOG.csv
│   │       ├── META.csv
│   │       └── NVDA.csv
│   └── processed/                 # Processed data with indicators
│       ├── AAPL_processed.csv
│       ├── AMZN_processed.csv
│       ├── GOOG_processed.csv
│       ├── META_processed.csv
│       ├── NVDA_processed.csv
│       └── sentiment_returns_merged.csv
│
├── notebooks/
│   ├── __init__.py
│   ├── README.md
│   ├── eda.ipynb                      # Task 1: Exploratory Data Analysis
│   ├── technical_analysis.ipynb       # Task 2: Technical Indicators
│   └── sentiment_correlation.ipynb    # Task 3: Sentiment & Correlation
│
├── src/
│   └── __init__.py                # Source modules (reusable functions)
│
├── tests/
│   └── test_data.py               # Unit tests (pytest)
│
├── scripts/
│   ├── __init__.py
│   └── README.md
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

##  Data Sources

### 1. Financial News Dataset (FNSPID)
- **File:** `data/raw/raw_analyst_ratings.csv`
- **Source:** [Kaggle — Massive Stock News Analysis DB](https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests)
- **Description:** 1,407,328 financial news headlines from Benzinga spanning 2009–2020
- **Fields:** `headline`, `url`, `publisher`, `date`, `stock`

### 2. Historical Stock Price Dataset
- **Files:** `data/raw/Data/AAPL.csv`, `AMZN.csv`, `GOOG.csv`, `META.csv`, `NVDA.csv`
- **Source:** [YFinance Python Library](https://github.com/ranaroussi/yfinance) — daily OHLCV data
- **Date Range:** 2009-01-02 to 2023-12-29
- **Fields:** `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume`

> **Note:** Raw data files are excluded from version control via `.gitignore`.
> Download from the sources above or request access via the project Google Drive:
> https://drive.google.com/drive/folders/1v8MRbbBuc2ee3dV6F1KZcpPsMEwhNamv

---

##  Environment Setup

### Prerequisites
- Python 3.10+
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/RigbeWeleslasie/news-sentiment-analysis.git
cd news-sentiment-analysis
```

### Step 2: Create and Activate Virtual Environment
```bash
python3 -m venv venv --without-pip
source venv/bin/activate          # Linux/Mac
# venv\Scripts\activate           # Windows

# Install pip inside venv
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Step 3: Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### Step 4: Register Jupyter Kernel
```bash
python -m pip install ipykernel
python -m ipykernel install --user --name=news-sentiment --display-name "Python (news-sentiment)"
```

### Step 5: Verify Installation
```bash
python -c "import pandas; import numpy; import matplotlib; import seaborn; import nltk; import textblob; import vaderSentiment; import yfinance; import ta; print('All packages OK!')"
```

---

##  How to Run

### Task 1 — Exploratory Data Analysis
```bash
jupyter notebook notebooks/eda.ipynb
```
**What it covers:**
- Headline length and word count distribution
- Publisher activity analysis (top 20 publishers)
- Keyword and topic analysis using CountVectorizer (unigrams + bigrams)
- Time series of news volume (2009–2020) with market event annotations
- News publication patterns by hour and day of week
- Most covered stock tickers

### Task 2 — Technical Indicator Analysis
```bash
jupyter notebook notebooks/technical_analysis.ipynb
```
**What it covers:**
- Loading and validating stock price CSVs (AAPL, AMZN, GOOG, META, NVDA)
- Computing SMA (20, 50-day), EMA (20-day), RSI (14-day), MACD (12/26/9)
- Visualizing price + indicators in 3-panel charts per stock
- Summary statistics for all five stocks

### Task 3 — Sentiment Analysis & Correlation
```bash
jupyter notebook notebooks/sentiment_correlation.ipynb
```
**What it covers:**
- VADER sentiment scoring on 1.4M headlines
- Date alignment (news → trading days, weekends forward-filled)
- Daily return calculation: `(Close_t - Close_{t-1}) / Close_{t-1} * 100`
- Pearson correlation analysis (overall + per stock)
- Scatter plot (sentiment vs returns) and bar chart (returns by sentiment category)

### Run All Tests
```bash
pytest tests/ -v
```

---

##  Key Results

| Metric | Value |
|--------|-------|
| Total news articles | 1,407,328 |
| Date range (news) | 2009 – 2020 |
| Stocks analyzed | AAPL, AMZN, GOOG, META, NVDA |
| Overall Pearson r | **0.205** (p < 0.001) |
| Positive sentiment avg return | **+0.82%** |
| Negative sentiment avg return | **-1.17%** |
| NVDA correlation | 0.2148  significant |
| GOOG correlation | 0.1895  significant |
| AAPL correlation | 0.1239  not significant |
| AMZN correlation | 0.1668  not significant |

---

## Technical Indicators

| Indicator | Parameters | Library | Interpretation |
|-----------|-----------|---------|----------------|
| SMA | 20-day, 50-day windows | `ta` | Trend direction; golden cross (SMA20 > SMA50) = bullish signal |
| EMA | 20-day window | `ta` | Faster trend signal; weights recent prices more heavily |
| RSI | 14-day window | `ta` | >70 = overbought (sell signal); <30 = oversold (buy signal) |
| MACD | 12, 26, 9-day EMAs | `ta` | Histogram sign change = momentum reversal signal |
| Daily Return | Pct change of Close | `pandas` | `(Close_t - Close_{t-1}) / Close_{t-1} * 100` |

All indicators computed using the **[`ta`](https://technical-analysis-library-in-python.readthedocs.io/)** library.

---

##  Sentiment Analysis Tool

**Tool Used:** VADER (Valence Aware Dictionary and sEntiment Reasoner)

| Criterion | VADER | TextBlob |
|-----------|-------|----------|
| Domain fit | Designed for short social-media text — matches financial headlines | General-purpose |
| Speed | Rule-based; processes 1.4M headlines in minutes | Comparable |
| Output | Compound score [-1, +1] | Polarity [-1, +1] + subjectivity |
| Training data | None required | None required |
| Financial jargon | Handles emphasis and punctuation | Less sensitive |

**Classification thresholds:**
- **Positive:** compound score ≥ 0.05
- **Negative:** compound score ≤ -0.05
- **Neutral:** -0.05 < score < 0.05

---

##  CI/CD Pipeline

GitHub Actions workflow (`.github/workflows/unittests.yml`) runs automatically on every push and pull request:

- Sets up Python 3.11
- Installs all dependencies from `requirements.txt`
- Runs `pytest tests/ -v`

View workflow runs: [GitHub Actions Tab](https://github.com/RigbeWeleslasie/news-sentiment-analysis/actions)

---

##  Git Branch Strategy

| Branch | Purpose | Status |
|--------|---------|--------|
| `main` | Stable, reviewed code |  Active |
| `task-1` | EDA and environment setup |  Merged |
| `task-2` | Technical indicator analysis |  Merged |
| `task-3` | Sentiment and correlation analysis |  Merged |

All task branches merged into `main` via Pull Requests.

---

##  Requirements
pandas
numpy
matplotlib
seaborn
plotly
scikit-learn
nltk
textblob
vaderSentiment
yfinance
ta
notebook
jupyterlab
pytest
python-dotenv
openpyxl
scipy
ipykernel

---

##  Limitations

- **Same-day alignment only** — lag effects (t+1, t+2) not yet tested
- **Publisher concentration** — 53% of articles from 5 Benzinga writers; may introduce editorial bias
- **Small matched sample** — only 1,566 matched news-price observations for 5 target stocks
- **VADER limitations** — does not fully understand financial jargon (e.g., "beats estimates")
- **Correlation ≠ causation** — reverse causality (prices moving before news) is possible

---

## Future Work

- Apply **FinBERT** for domain-specific financial sentiment scoring
- Conduct **lag analysis** to test t+1 and t+2 day predictive power
- Expand to **intraday data** for finer-grained analysis
- Build a **real-time sentiment dashboard** using live news feeds
- Test strategies in a **backtested trading simulation** with transaction costs

---

## Author

**Rigbe Weleslasie**
Nova Financial Solutions Analytics Challenge — May 2026
GitHub: [@RigbeWeleslasie](https://github.com/RigbeWeleslasie)

---

## References

- Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. *ICWSM*.
- Tetlock, P.C. (2007). Giving Content to Investor Sentiment. *Journal of Finance*, 62(3).
- [Investopedia: Stock Analysis](https://www.investopedia.com/terms/s/stock-analysis.asp)
- [TA Library Documentation](https://technical-analysis-library-in-python.readthedocs.io/)
- [VADER Sentiment](https://github.com/cjhutto/vaderSentiment)
- [YFinance](https://github.com/ranaroussi/yfinance)
- [FNSPID Dataset Paper](https://arxiv.org/abs/2402.06698)

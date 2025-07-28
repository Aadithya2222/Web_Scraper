# 🕸️ Web Scraper 🔍

A simple yet effective Python-based web scraping tool that allows you to extract and save data from any website directly into CSV format. Perfect for beginners learning web scraping and data collection!

---

## 🚀 Features

- 📥 Accepts any URL for scraping
- 🧹 Extracts data using BeautifulSoup
- 📄 Saves scraped data into `scraped_data.csv`
- 🧪 Includes a sample test script
- ✅ Lightweight and easy to use

---

## 🛠️ Tech Stack

- Python 🐍
- BeautifulSoup 🥣
- Requests 🌐
- Pandas 🐼

---

## 📁 Project Structure

```
web_scraper/
│
├── data/               # Output CSV files
│   ├── quotes.csv
│   └── scraped_data.csv
│
├── notebooks/          # (Optional) Jupyter notebooks
│
├── scraper/            # Main scraper code
│   ├── __init__.py
│   ├── scraper.py      # Primary script
│   ├── scraper1.py     # Alternate scraper version
│   └── utils.py        # Helper functions
│
├── tests/              # Unit tests
│   └── test_scraper.py
│
├── venv/               # Virtual environment
├── requirements.txt    # Python dependencies
├── README.md           # You're here!
└── config.py           # Configuration file (optional)
```

---

## 🧪 How to Run

### 🔹 1. Clone the Repo

```bash
git clone https://github.com/Aadithya2222/Web_Scraper.git
cd Web_Scraper
```

### 🔹 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 🔹 3. Activate the Virtual Environment

On Windows:
```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```

### 🔹 4. Install Requirements

```bash
pip install -r requirements.txt
```

### 🔹 5. Run the Scraper

```bash
python scraper/scraper.py
```

👉 Then enter the URL when prompted.

---

### 📤 Output

The scraped data will be saved in the `data/` folder as:

```
scraped_data.csv
```

---

## 🧪 Running Tests

```bash
python tests/test_scraper.py
```

---

## 🤝 Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---


🌟 Star the repo if it helped you!

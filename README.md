# Data Engineer Jobs Scraper & Interactive Dashboard

This project scrapes **Data Engineer job listings** from [Naukrigulf](https://www.naukrigulf.com) and provides an **interactive Streamlit dashboard** for analyzing job trends.  

Users can filter jobs by **location, company, or experience**, search by **keywords**, and visualize data through interactive charts.

---

## Project Structure

```

DataEngineerJobs/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── scraper/
│   └── job_scraper.py        # Selenium scraper
│
├── data/
│   └── Jobs.csv              # Scraped CSV
│
├── app/
│   └── app.py                # Streamlit dashboard
│
└── assets/                   # Optional images/screenshots

````

---

## Features

- Scrapes the first 3 pages of Data Engineer job listings.
- Extracts:
  - Job Title
  - Company Name
  - Job Location
  - Required Experience
  - Full Job Description
- Saves data as a structured CSV (`Jobs.csv`)
- Streamlit dashboard includes:
  - Filters by Location, Company, Experience
  - Keyword search in Job Description
  - Interactive charts (Jobs by Location & Company)
  - Expandable full job descriptions

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/DataEngineerJobs.git
cd DataEngineerJobs
````

2. **Create a virtual environment (optional but recommended)**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Run the Scraper

```bash
python scraper/job_scraper.py
```

* Generates `data/Jobs.csv` with the latest job listings.

### 2. Launch the Streamlit Dashboard

```bash
python -m streamlit run app/app.py
```

* Opens a browser window with the interactive dashboard.
* Use sidebar filters to explore job listings by location, company, or experience.

---

## Screenshots
<img width="1896" height="1025" alt="image" src="https://github.com/user-attachments/assets/7ffe47b4-db40-444d-bb1c-53bdb796a178" />


```markdown
![Dashboard Preview](assets/dashboard.png)
```

---

## Dependencies

* Python 3.8+
* Selenium
* Pandas
* Streamlit
* Matplotlib (optional for charts)

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## .gitignore Recommendations

* `__pycache__/`
* `*.pyc`
* `.env`
* `data/Jobs.csv`

---

## License

Educational and portfolio use only.

```


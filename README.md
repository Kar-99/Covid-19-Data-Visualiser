
# 🦠 COVID-19 Data Visualiser

This project is a Python-based data analysis and visualization tool that explores real or simulated COVID-19 data. It focuses on understanding the progression of COVID-19 in India using public datasets and creates visual reports to analyze total cases and deaths over time.

![Sample Plot](covid_india_realistic_simulated.png)

---

## 📚 Table of Contents

- [About](#about)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Extended Description](#extended-description)
- [Future Improvements](#future-improvements)

---

## 🧠 About

The **COVID-19 Data Visualiser** reads publicly available COVID-19 data, processes it using `pandas`, and generates both static and interactive plots using `matplotlib` and `plotly`.
By default, it analyzes data for **India**, but you can change the location to explore other countries as well.

---

## ✨ Features

- 📁 Load COVID-19 data from OWID CSV
- 🔍 Filter data by country (India by default)
- 📈 Visualize trends of:
  - Total confirmed cases
  - Total deaths
- 📊 Line charts using `matplotlib`
- 🌐 Interactive charts using `plotly`
- 🧹 Cleans and handles missing data
- 🖼 Saves plots as images

---

## 🔧 Technologies Used

- Python 3.x
- pandas
- matplotlib
- plotly
-  VS Code
- [OWID COVID-19 Dataset](https://covid.ourworldindata.org/data/owid-covid-data.csv)

---

## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/covid-visualiser.git
   cd covid-visualiser
   ```

2. **Install dependencies**
   ```bash
   pip install pandas matplotlib plotly
   ```

3. **Download the dataset**
   [Click here to download owid-covid-data.csv](https://covid.ourworldindata.org/data/owid-covid-data.csv)  
   Save it in the same folder as your script.

---

## 🚀 Usage

1. Run the Python script:
   ```bash
   python covid_visualiser.py
   ```

2. View the generated plots:
   - Static Matplotlib image
   - Interactive Plotly chart in browser

---

## 📷 Screenshots

### Static Matplotlib Line Chart  
![Static Chart](covid_india_realistic_simulated.png)

---

## 🧾 Extended Description

This project uses real-world COVID-19 data to generate clear and informative visualizations. It’s designed as a lightweight, educational, and customizable tool for students, analysts, and developers.

### Key Goals:
- Analyze pandemic trends in India
- Use real datasets to practice data wrangling and visualization
- Provide interactive and high-quality static graphs

### Use Case:
- Great for portfolios
- Beginner data science practice
- Teaching data visualization and cleaning

---

## 🔮 Future Improvements

- Add support for multiple countries
- Export plots and insights as PDF reports
- Integrate live API data (e.g., via RapidAPI or OWID JSON endpoint)
- Include more visual types: bar charts, pie charts, heatmaps
- GUI to select country/date range

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Kartik Pandey**  
📧 kartikpandey139.you@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/kartik-pandey-11429a25a)  
💻 [GitHub](https://github.com/yourusername)

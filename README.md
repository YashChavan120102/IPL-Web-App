# 🏏 IPL Web App (2008–2020)

This is a Streamlit-based web application that provides interactive visualizations and insights from Indian Premier League (IPL) match data from 2008 to 2020.

Live App 👉 [ipl-web-app.streamlit.app](https://ipl-web-app.streamlit.app)

---

## 📊 Features

- **Overall Analysis**: Top statistics, team wins, matches by city, toss decisions, and more.
- **Team-wise Comparison**: Compare head-to-head performance between any two teams.
- **Venue-wise Wins**: Analyze how teams performed at different venues with respect to toss decisions.
- **Static Stats**: Quick view of total matches won by each team.

---

## 🧠 Technologies Used

- [Streamlit](https://streamlit.io/) – Web app framework
- [Pandas](https://pandas.pydata.org/) – Data manipulation
- [Plotly](https://plotly.com/python/) – Interactive charts
- [Matplotlib & Seaborn](https://seaborn.pydata.org/) – Data visualization (optional)

---

## 🗂 Project Structure

```
├── app.py                  # Main Streamlit app
├── helper.py               # Helper functions for processing and filtering data
├── preprocessor.py         # Preprocessing logic (get_dummies, etc.)
├── IPL Matches 2008-2020.csv  # Main dataset
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🚀 Run Locally

### 🔧 Prerequisites
- Python 3.9 or newer
- pip

### 💻 Steps
```bash
git clone https://github.com/YashChavan120102/IPL-Web-App.git
cd IPL-Web-App
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Dataset Source

- [Kaggle IPL Dataset](https://www.kaggle.com/datasets)
- IPL Ball-by-Ball and Match Summary from 2008–2020

---

## 📌 Notes

- Currently optimized for display on **Streamlit Cloud**.
- Compatible with **Python 3.13+** environments.
- Make sure your `requirements.txt` does not pin old versions of `numpy`, `pandas`, etc. (for compatibility with newer Python).

---

## 📬 Contact

Made with ❤️ by [Yash Chavan](https://github.com/YashChavan120102)  
For feedback or improvements, feel free to create an issue or pull request.

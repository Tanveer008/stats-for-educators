📊 Statistics for Educators
Turning Data into Better Teaching — A Series by Tanvir Ali
![LinkedIn](https://img.shields.io/badge/Follow%20on-LinkedIn-0077B5?style=for-the-badge&logo=linkedin)
![GitHub](https://img.shields.io/badge/GitHub-Tanvir008-181717?style=for-the-badge&logo=github)
![Status](https://img.shields.io/badge/Series-Active-brightgreen?style=for-the-badge)
---
🎯 What Is This?
Most statistics courses teach you how to run a regression.  
This series teaches you how to use statistics to become a better teacher.
Statistics for Educators is a free, open-source content series designed for:
🏫 School and college teachers in Bangladesh (and beyond)
📊 Education researchers who want practical data skills
🎓 Anyone who wants to make evidence-based decisions in the classroom
Every episode includes:
A concept explained simply (no PhD required)
A real classroom dataset to practice with
Python / R / Excel code — you choose your tool
A LinkedIn post with key takeaways
---
📚 Episode List
#	Title	Concept	Dataset	Tools	Status
01	Why Teachers Need Statistics	Descriptive Stats	Class test scores	Excel, Python	✅ Published
02	Are My Students Actually Improving?	Paired t-test	Pre & Post test scores	Python, SPSS	✅ Published
03	Which Teaching Method Works Better?	ANOVA	Multi-class comparison	R, Python	🔄 In Progress
04	Who Is at Risk of Failing?	Logistic Regression	Student performance data	Python	📅 Coming Soon
05	Is There a Gender Gap in My Classroom?	Chi-Square Test	Assessment data	Python, Excel	📅 Coming Soon
06	What Really Predicts Student Success?	Correlation & Regression	Multi-variable data	Python	📅 Coming Soon
07	Visualizing Your Classroom Data	Data Viz	Any classroom dataset	Python (Matplotlib, Seaborn)	📅 Coming Soon
08	Building a Student Performance Dashboard	Streamlit App	Full dataset	Python, Streamlit	📅 Coming Soon
---
🗂️ Repository Structure
```
stats-for-educators/
│
├── README.md                  ← You are here
│
├── episodes/
│   ├── 01-why-teachers-need-statistics/
│   │   ├── README.md          ← Episode explanation
│   │   ├── notebook.ipynb     ← Full analysis (Python)
│   │   ├── data/              ← Sample dataset
│   │   └── linkedin_post.md   ← Ready-to-copy LinkedIn post
│   │
│   ├── 02-are-students-improving/
│   │   └── ...
│   └── ...
│
├── datasets/
│   └── sample_class_data.csv  ← Shared datasets
│
└── resources/
    └── recommended_reading.md
```
---
🚀 How to Get Started
Option 1 — Just read: Go to any episode folder and open `README.md`
Option 2 — Run the code:
```bash
git clone https://github.com/Tanveer008/stats-for-educators.git
cd stats-for-educators
pip install -r requirements.txt
jupyter notebook
```
Option 3 — Follow along on LinkedIn: Each episode has a LinkedIn post with the key insight summarized in plain language.
---
🧠 Who Is This For?
You are...	You will learn...
A school teacher with no stats background	How to read and interpret your own class data
A teacher who knows basic stats	How to apply it practically in classroom decisions
An education researcher	How to use Python/R for education data analysis
A data scientist interested in EdTech	How education data is structured and what questions matter
---
📖 Episode 01 — Sneak Peek
Question: "My students scored an average of 62% last month. Is that good or bad?"
Most teachers stop at the average. But the average alone is misleading.
```python
import pandas as pd
import matplotlib.pyplot as plt

scores = [45, 50, 55, 62, 62, 62, 70, 75, 90, 95]

print(f"Mean:   {pd.Series(scores).mean():.1f}")
print(f"Median: {pd.Series(scores).median():.1f}")
print(f"Std Dev:{pd.Series(scores).std():.1f}")

# Two classes can have the same average but very different realities
```
Output:
```
Mean:   66.6
Median: 62.0
Std Dev: 17.2
```
A standard deviation of 17.2 tells you the class is highly divided — some students are thriving, others are struggling. The average hid that completely.
➡️ See full Episode 01 →
---
🌍 Why Bangladesh?
Education data analysis is common in Western academia but rare in Bangladeshi classrooms. Most teachers here make decisions based on intuition alone — not because they lack intelligence, but because no one has shown them how accessible data analysis actually is.
This series bridges that gap. All examples use:
Datasets relevant to Bangladeshi school contexts
Tools that are free (Python, R, Excel)
Language that is jargon-free
---
🤝 Contribute
Have a dataset, a question, or a teaching story?  
Open an Issue or submit a Pull Request.  
All contributions welcome.
---
👨‍🏫 About the Author
Tanvir Ali  
MSc Statistics, Comilla University (CGPA: 3.73/4.00)  
Assistant Mathematics Teacher, Reaz Public School, Narayanganj  
National Science & Technology Fellowship Awardee — 2025  
IELTS: 7.0
Researcher in ML-based health prediction, education analytics, and psychological well-being.
📧 alitanvirislam008@gmail.com  
🔗 LinkedIn  
💻 GitHub
---
📄 License
This project is open source under the MIT License.  
Use it, share it, teach with it. Just give credit. 🙏
---
"Data does not replace teacher judgment — it informs it."

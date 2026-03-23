
# 🚀 placement-prediction-tool

## 📌 Overview

**placement-prediction-tool** is an AI-powered placement prediction and career guidance system designed to help students understand their placement chances, evaluate resume strength, and identify suitable companies and roles.

It combines **Machine Learning, Resume Analysis, and Job Matching Algorithms** to provide personalized insights and actionable suggestions.

---

## 🎯 Problem Statement

Students often:

* Don’t know their real placement probability
* Lack clarity on which companies/roles fit their profile
* Don’t understand what skills they are missing

**placement prediction tool solves this by providing data-driven predictions and recommendations.**

---

## ⚙️ Features

### 🔹 1. Placement Prediction (ML Model)

* Uses real campus recruitment dataset
* Predicts placement probability based on:

  * Academic scores
  * Degree background
  * Work experience
  * Aptitude scores

---

### 🔹 2. Resume Analysis (ATS Score)

* Extracts skills from resume (PDF/Text)
* Calculates ATS (Applicant Tracking System) score
* Identifies:

  * ✅ Matching skills
  * ❌ Missing skills

---

### 🔹 3. Company & Role Fit Prediction

#### Mode A:

👉 Enter **Company + Role**

* Predicts fit score
* Suggests missing skills
* Gives improvement roadmap

#### Mode B:

👉 No input

* Recommends **best companies & roles**
* Based on profile + resume

#### Mode C:

👉 Enter only **Role**

* Suggests companies where you can fit

---

### 🔹 4. Resume PDF Upload

* Upload resume directly
* Automatic text extraction
* Real-time analysis

---

### 🔹 5. User Authentication

* Login & Register system
* JWT-based authentication

---

### 🔹 6. MongoDB Integration

Stores:

* User data
* Prediction history
* Full resume text
* Results & scores

---

### 🔹 7. Prediction History

* Track previous analyses
* View improvement over time

---

## 🧠 Tech Stack

### Frontend

* React.js
* HTML, CSS, JavaScript
* Vite

### Backend

* Python (Flask)
* REST API Architecture

### Machine Learning

* Scikit-learn
* Logistic Regression Model

### Database

* MongoDB

### Other Tools

* PDF Processing (PyPDF2)
* NLP (Skill Matching)
* TF-IDF (Job Matching)

---

## 📂 Project Structure

```
placement prediction tool/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   ├── repositories/
│   │   └── utils/
│   ├── data/
│   ├── models/
│   ├── run.py
│   └── requirements.txt
│
├── frontend/
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   ├── api/
    │   └── styles/
    ├── package.json
    └── vite.config.js
```

---

## 🚀 How to Run

### 🔹 Backend Setup

```bash
cd backend
pip install -r requirements.txt
python train_model.py
python run.py
```

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## 📊 Dataset

* Campus Recruitment Dataset
* Jobs & Skills Dataset

These are used for:

* ML training
* Job-role matching

---

## 📈 Future Improvements

* Deep Learning model for better prediction
* Real-time company data scraping
* Interview question suggestions
* Personalized learning roadmap
* Deployment (Cloud + CI/CD)

---

## 💡 Use Cases

* Students preparing for placements
* Colleges for placement analytics
* Career guidance platforms

---

## 🏆 Highlights

✔ Real-world dataset
✔ AI-based predictions
✔ Resume + Job matching
✔ Modular enterprise architecture
✔ Full-stack implementation

---

## 👨‍💻 Author

**Bharath Veesam , akhil and saravan reddy**
B.Tech AIML Students
Passionate about AI, startups, and solving real-world problems.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share!

---

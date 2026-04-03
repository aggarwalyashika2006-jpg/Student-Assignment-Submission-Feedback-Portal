# 📚 Cloud-Based Student Assignment Submission & Feedback Portal

### 👩‍💻 Developed by: **Yashika Agarwal**

---

## 🚀 Project Overview

This project is a cloud-based web application that allows students to submit assignments and teachers to review, grade, and provide feedback efficiently.

The system also integrates basic AI functionality to calculate plagiarism similarity scores using a machine learning model.

---

## 🎯 Features

### 👨‍🎓 Student Features

* Submit assignments using Google Drive links
* Paste answer text for AI analysis
* View submission history with version tracking
* Check late submission status
* View teacher feedback and grades

---

### 👩‍🏫 Teacher Features

* View all student submissions
* Filter submissions by course and assignment
* Open submitted files via links
* Provide rubric-based grading
* Add feedback using comment threads
* Export data as CSV file

---

### 🤖 AI Features

* Plagiarism similarity detection using Sentence-BERT
* Basic auto-grade support (optional)

---

## 🧠 Tech Stack

* **Frontend:** React (Vite)
* **Backend Database:** Firebase Firestore
* **Authentication:** Firebase Authentication
* **AI Backend:** Flask (Python)
* **ML Model:** Sentence-BERT

---

## ⚙️ Important Notes

### ❗ File Upload Limitation

Originally, the project planned to use Firebase Storage for file uploads.
However, Firebase Storage requires a paid plan.

👉 **Solution:**
Assignments are submitted using:

* Google Drive links
* Text input

This ensures the project works fully on the free tier.

---

### ❗ AI Deployment Limitation

The AI backend could not be deployed on Cloud Run due to billing requirements.

👉 **Current Setup:**
AI runs locally on:

```
http://127.0.0.1:5000
```

---

## 🛠️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/student-portal.git
cd student-portal
```

---

### 2️⃣ Install Frontend Dependencies

```bash
npm install
npm run dev
```

---

### 3️⃣ Setup Firebase

* Create Firebase project
* Enable Authentication (Email/Password)
* Enable Firestore Database
* Add your Firebase config in `firebase.js`

---

### 4️⃣ Run AI Backend

```bash
cd ai_backend
pip install -r requirements.txt
python app.py
```

---

## 📊 Database Structure

### 📁 submissions collection

* userId
* email
* course
* assignmentId
* link
* text
* version
* isLate
* createdAt
* rubric

---

### 📁 feedback collection

* sid (submission ID)
* teacherUid
* comment
* grade
* createdAt

---

## 🧪 Testing

* Manual testing performed
* Verified:

  * Login system
  * Assignment submission
  * Version tracking
  * Late submission detection
  * Feedback system
  * AI integration

---

## 🚧 Limitations

* No file upload (due to Firebase Storage billing)
* AI backend runs locally
* Basic notifications (alert-based)

---

## 🔮 Future Improvements

* Add Firebase Storage for file uploads
* Deploy AI backend on Cloud Run
* Implement real-time notifications
* Improve UI/UX design
* Add analytics dashboard
* Enhance plagiarism detection with larger datasets
* Add email notifications

---

## 📌 Conclusion

This project demonstrates practical implementation of cloud computing concepts, database design, and AI integration while working within free-tier constraints.

---

# Employee Burnout Prediction System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

## 🔗 Live Demo
**[Try the Live Application](https://employee-burnout-prediction-qmmv.onrender.com/)**

## 📋 Project Overview

This project was developed during my **AI/ML Internship at Edunet Foundation** to predict employee burnout risk using machine learning algorithms. The system analyzes various workplace and personal factors to provide early warnings about potential burnout, helping organizations take proactive measures to maintain employee well-being.

## 🎯 Objective

To develop a predictive model that can identify employees at risk of burnout based on workplace factors, enabling organizations to:
- **Prevent burnout** before it occurs
- **Improve employee retention** and satisfaction
- **Create healthier work environments**
- **Reduce organizational costs** associated with employee turnover

## 📊 Dataset Information

The dataset contains employee information with the following features:

| Feature | Description | Data Type | Range/Values |
|---------|-------------|-----------|--------------|
| **Employee ID** | Unique identifier for each employee | String | e.g., fffe390032003000 |
| **Date of Joining** | Employee's joining date | DateTime | e.g., 2008-12-30 |
| **Gender** | Employee's gender | Categorical | Male/Female |
| **Company Type** | Type of organization | Categorical | Service/Product |
| **WFH Setup Available** | Work from home availability | Categorical | Yes/No |
| **Designation** | Employee's job level | Numerical | 0.0 - 5.0 (higher = senior) |
| **Resource Allocation** | Daily working hours | Numerical | 1.0 - 10.0 |
| **Mental Fatigue Score** | Employee's mental fatigue level | Numerical | 0.0 - 10.0 (0=no fatigue, 10=extreme) |
| **Burn Rate** | **Target Variable** - Burnout risk score | Numerical | 0.0 - 1.0 (higher = more burnout risk) |

## 🔧 Features Used for Prediction

After data preprocessing and cleaning, the following features are used:

1. **Gender** - Employee's gender (Male/Female)
2. **Company Type** - Service or Product company
3. **WFH Setup Available** - Remote work availability (Yes/No)
4. **Designation** - Job level/seniority
5. **Daily Working Hours** - Number of hours worked per day
6. **Mental Fatigue Score** - Current mental fatigue level (0.0-10.0)
7. **Company Tenure** - Years of experience with the company

## 🛠️ Technologies Used

- **Python** - Core programming language
- **Pandas & NumPy** - Data manipulation and analysis
- **Scikit-learn** - Machine learning algorithms
- **Matplotlib & Seaborn** - Data visualization
- **Flask** - Web framework
- **HTML5 & CSS3** - Frontend development
- **Render** - Deployment platform

## 📈 Model Performance

### **Algorithms Compared**
| Model | R² Score | Performance |
|-------|----------|-------------|
| **Linear Regression** ✅ | **0.92** | **Best Performance** |
| Random Forest Regressor | < 0.92 | Outperformed by Linear Regression |

### **Final Model Selection**
- **Algorithm Used**: **Linear Regression**
- **R² Score**: **0.92** (Excellent predictive accuracy)
- **Model Choice Rationale**: Linear Regression outperformed Random Forest, demonstrating that employee burnout has strong linear relationships with the selected features
- **Validation**: Cross-validation confirmed consistent performance across different data splits
## 🎯 Key Insights

### **Model Performance Insights**
- **Linear Regression superiority**: Despite being a simpler algorithm, Linear Regression achieved **92% accuracy**, outperforming Random Forest
- **Linear relationships**: The strong performance of Linear Regression indicates that employee burnout has clear linear correlations with workplace factors
- **Feature importance**: Mental fatigue score, working hours, and company tenure show strong predictive power

### **Burnout Risk Patterns**
- Employees with **higher mental fatigue scores** show significantly increased burnout risk
- **Longer working hours** correlate strongly with burnout probability
- **Work-from-home availability** reduces burnout risk
- **Company tenure** shows interesting patterns in burnout prediction

## 🚀 Project Workflow

### 1. **Data Import & Setup**

### 2. **Dataset Overview**
- Data exploration and initial analysis
- Understanding data structure and types
- Identifying missing values and outliers

### 3. **Data Cleaning**
- Handling missing values
- Removing duplicates
- Addressing outliers and inconsistencies

### 4. **Data Preprocessing**
- Feature selection and engineering
- Encoding categorical variables
- Creating derived features (tenure calculation)

### 5. **Exploratory Data Analysis (EDA)**
- Statistical analysis of features
- Correlation analysis
- Distribution analysis of target variable

### 6. **Data Visualization**
- Feature distributions
- Correlation heatmaps
- Burnout risk patterns across different categories

### 7. **Data Splitting**

### 8. **Standardization**

### 9. **Model Training**
- **Linear Regression** - Primary model
- **Random Forest Regressor** - Comparison model
- Model comparison and performance evaluation
- Cross-validation for robust performance

### 10. **Model Evaluation & Comparison**
- **Linear Regression**: R² = 0.92 ✅
- **Random Forest**: Lower performance than Linear Regression
- Model comparison and final selection
- Performance metrics calculation

### 11. **Web Application Development**
- Flask-based user interface
- Interactive form for predictions
- Real-time burnout risk assessment

### 12. **Deployment**
- Deployed on Render platform
- Live web application for public access

## 🎨 User Interface Features

### Risk Categories
The application categorizes burnout risk into three levels:

| Risk Level | Score Range | Background Color | Action Required |
|------------|-------------|------------------|-----------------|
| **🟢 Low Risk** | 0.0 - 0.4 | Green | Maintain current habits |
| **🟡 Moderate Risk** | 0.41 - 0.7 | Orange | Take preventive measures |
| **🔴 High Risk** | 0.71 - 1.0 | Red | Immediate intervention needed |

### Interface Highlights
- **Responsive Design** - Works on all devices
- **Modern UI/UX** - Gradient backgrounds and smooth animations
- **Interactive Forms** - User-friendly input fields
- **Real-time Results** - Instant burnout risk assessment
- **Actionable Insights** - Specific recommendations for each risk level


## 📁 Project Structure

```
employee-burnout-prediction/
│
├── dataset/
│   └── employee_burnout_analysis-AI.xlsx
├── models/
│   └── lr.pkl
│   └── scaler.pkl
├── notebook/
│   └── EMPLOYEES_BURNOUT_PREDICTION.ipynb   # Data analysis notebook
├── templates/
│   └── home.html       # Main webpage
├── app.py                 # Flask application
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## 🚀 How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/employee-burnout-prediction.git
cd employee-burnout-prediction
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open in browser**
```
http://localhost:5000
```

## 🙏 Acknowledgments

- **Edunet Foundation** - For providing the internship opportunity
- **Mentors and Peers** - For guidance and support throughout the project
- **Open Source Community** - For the amazing tools and libraries

---

⭐ **Star this repository if you found it helpful!** ⭐

**Live Demo**: [https://employee-burnout-prediction-qmmv.onrender.com/](https://employee-burnout-prediction-qmmv.onrender.com/)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Load the cleaned data
df = pd.read_csv('data/cleaned_student_scores.csv')

# 2. Setup Features (X) and Target (y)
X = df[['Hours_Studied']]
y = df['Exam_Score']

# 3. Split the data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict and Evaluate
predictions = model.predict(X_test)
print(f"Model Score (R^2): {model.score(X_test, y_test):.2f}")

# 6. Quick Prediction
hours = 5.5
predicted_score = model.predict([[hours]])
print(f"Predicted score for {hours} hours of study: {predicted_score[0]:.2f}")
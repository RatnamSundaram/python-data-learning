import pandas as pd

def clean_student_data(file_path):
    # Load the data
    df = pd.read_csv(file_path)
    
    print("--- Missing Values Before ---")
    print(df.isnull().sum())
    
    # Fill missing attendance with the average (mean)
    df['Attendance_Rate'] = df['Attendance_Rate'].fillna(df['Attendance_Rate'].mean())
    
    # Save the cleaned version
    df.to_csv('data/cleaned_student_scores.csv', index=False)
    print("\nData cleaned and saved to 'data/cleaned_student_scores.csv'")
    return df

if __name__ == "__main__":
    clean_student_data('data/student_scores.csv')
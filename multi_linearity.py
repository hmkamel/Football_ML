import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Load data (replace 'path/to/your/data.csv' with the actual path)
data = pd.read_csv('PL_Match_Stats.csv')
data = data.dropna()  # Drop rows with missing values (optional)

# Define target variable and features (excluding expected stats)
target_col = 'Win / Tie'
feature_cols = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
                79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 99,
                100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]

# Separate features (X) and target variable (y)
X = data.iloc[:, feature_cols].values
y = data[target_col].values

# Create a new column to store original labels (casting to string if necessary)
data['Original_Label'] = y.astype(str)  # Ensure y is a string to avoid conversion errors

# Split data into training and testing sets (ensure y is not encoded yet)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Define a function to decode one-hot encoded labels
def decode_one_hot(y_encoded, encoder):
  """
  Decodes one-hot encoded labels back to their original values.

  Args:
      y_encoded (numpy.ndarray): The one-hot encoded labels (2D array).
      encoder (OneHotEncoder): The OneHotEncoder object used for encoding.

  Returns:
      numpy.ndarray: The decoded original labels (1D array).
  """
  categories = encoder.inverse_transform(y_encoded)
  return categories.squeeze()  # Remove extra dimension if present

# One-hot encode the target variable (separately for train and test)
encoder = OneHotEncoder()
y_train_encoded = encoder.fit_transform(y_train.reshape(-1, 1))  # Reshape for 2D array
y_test_encoded = encoder.transform(y_test.reshape(-1, 1))  # Reshape for 2D array

# Select the first column of encoded labels (assuming class labels are in the first column)
y_train_encoded = y_train_encoded[:, 0]
y_test_encoded = y_test_encoded[:, 0]

# Train a Logistic Regression model
model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
model.fit(X_train, y_train_encoded)

# Make predictions on the test set
predicted_proba = model.predict_proba(X_test)

# Decode the test set labels
decoded_labels = decode_one_hot(y_test_encoded, encoder)

# Combine predicted probabilities with decoded labels
predictions_df = pd.DataFrame({'Original_Label': decoded_labels,
                               'Predicted_Probability': predicted_proba[:, 1]})  # Assuming class 1 is win

# Print the DataFrame with original labels and predicted win probabilities
print(predictions_df)

# # Optional: Plot predicted vs actual values (not applicable for classification)

from sklearn.linear_model import LinearRegression

# Training data
# X = Study Hours
X = [[1], [2], [3], [4],
     [5], [6], [7], [8]]

# y = Exam Scores
y = [40, 45, 50, 60,
     65, 75, 80, 90]

# Create the model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Give new data to the trained model
prediction = model.predict([[9]])

# Display the prediction
print("Predicted score for 9 hours of study:", prediction[0])

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    accuracy_score,
)
from django.db import connection
import pickle
from sklearn.tree import plot_tree
from app.models import Dataset
import ast
from app.models import ModelInfo
from datetime import datetime

class Tree:
    """ A decision tree class. """
    def __init__(self):
        pass

    def getDatasets(self):
        """ A method to get datasets using ORM object. Store it in array with dictionary. """

        data = Dataset.objects.all()
        array_data = []

        if len(data) > 0:
            for row in data:

                instance_data = {
                    "id": row.pk,
                    "anemometer": row.anemometer,
                    "rainfall": row.rainfall,
                    "humidity": row.humidity,
                    "is_storm_present": row.is_storm_present,
                }
                
                array_data.append(
                    instance_data
                )

        return array_data
    
    def predictAlgorithm(self, new_data):
        """ A method to predict using sensor values. """

        # Load the saved model from the .pkl file
        with open("decision_tree.pkl", "rb") as model_file:
            loaded_model = pickle.load(model_file)

        formatted_data = [
            [
                new_data["anemometer"],
                new_data["rainfall"],
                new_data["humidity"]
            ]
        ]

        # Convert string values to appropriate data types (if necessary)
        formatted_data = [
            [ast.literal_eval(val) if isinstance(val, str) else val for val in row]
            for row in formatted_data
        ]

        predictions = loaded_model.predict(formatted_data)
        return predictions  

    def decisionTree(self):
        """ A method to create decision tree. """

        independent_var = []
        correct_answer = []

        data = self.getDatasets()

        for item in data:
            independent_var.append(
                [
                    item["id"],
                    item["anemometer"],
                    item["rainfall"],
                    item["humidity"]
                ]
            )
            correct_answer.append(item["is_storm_present"])

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            independent_var, correct_answer, test_size=0.2, random_state=42
        )
        # To retain the primary key.
        X_test_original = [row[:] for row in X_test]
        X_train_original = [row[:] for row in X_train]

        # Modify the copied lists (removing the first element)
        for each_rows in X_test:
            each_rows.pop(0)

        for each_rows in X_train:
            each_rows.pop(0)

        # Initialize Decision Tree classifier
        dt_classifier = DecisionTreeClassifier(max_depth=5, random_state=42)

        # # Train the AdaBoost classifier
        dt_classifier.fit(X_train, y_train)

        # Predictions
        y_pred_train = dt_classifier.predict(X_train)
        y_pred_test = dt_classifier.predict(X_test)

        # Evaluate accuracy
        # train_accuracy = accuracy_score(y_train, y_pred_train)
        
        test_accuracy = round(accuracy_score(y_test, y_pred_test), 2) * 100
        precision = round(precision_score(y_test, y_pred_test), 2) * 100
        f1 = round(f1_score(y_test, y_pred_test), 2) * 100
        recall = round(recall_score(y_test, y_pred_test), 2) * 100

        print(precision, f1, recall, test_accuracy)

        ModelInfo.objects.all().update(
            last_trained_state = datetime.now(),
            accuracy = test_accuracy,
            precision = precision,
            recall = recall,
            f1_score = f1
        )

        # print("Train Accuracy Abnormal/Normal:", train_accuracy)
        # print("Test Accuracy Abnormal/Normal:", test_accuracy)

        # # Save the trained model to a file
        with open("decision_tree.pkl", "wb") as model_file:
            pickle.dump(dt_classifier, model_file)
            

        # Visualize the last tree in the AdaBoost model

        # TestingDataSet.objects.all().delete()

        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         "DELETE FROM sqlite_sequence WHERE name='app_testingdataset';"
        #     )

        # for i in range(len(y_test)):
        #     TestingDataSet.objects.create(
        #         training_id=TrainingDataSet.objects.get(id=X_train_original[i][0]),
        #         predicted_values=y_pred_test[i],
        #     )
        #     print(
        #         f"Primary Key: {X_test_original[i][0]} Sample {i+1}: Predicted: {y_pred_test[i]}, Actual: {y_test[i]}"
        #     )

        # self.evaluateMetrics(y_test, y_pred_test)

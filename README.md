# Music Genre Prediction using Decision Tree Classifier

This repository contains Python code that uses the Decision Tree Classifier from the scikit-learn library to predict music genres based on given input features.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

### Installation

1. Clone this repository to your local machine using the following command:

```
git clone <repository_url.git>
```

2. Install the required dependencies using pip:

```
pip install pandas scikit-learn
```

### Dataset

The music dataset is stored in a CSV file named 'music.csv', which should be present in the same directory as the Python script.

The dataset contains two columns:

- **'age'**: representing the age of the listener (numeric).
- **'gender'**: representing the gender of the listener (0 for male, 1 for female).

Each row in the dataset corresponds to a music genre label.

## Usage

Run the Python script 'music_genre_prediction.py' to predict music genres based on given input features. The script performs the following steps:

1. Reads the 'music.csv' dataset using pandas.
2. Prepares the input features (X) by dropping the 'genre' column from the dataset.
3. Prepares the target labels (Y) containing the 'genre' column.
4. Initializes the DecisionTreeClassifier model.
5. Fits the model using the input features (X) and target labels (Y) from the dataset.
6. Makes predictions for two sets of input features: [2, 0] and [22, 0].
7. Displays the predicted music genre labels for the input features.

To run the script, execute the following command in the terminal or command prompt:

```
python music_genre_prediction.py
```

The output will show the predicted music genre labels for the given input features.

## Customization

You can modify the 'music.csv' dataset or use a different dataset with similar structure to predict music genres based on different features.

You can also experiment with different machine learning models provided by scikit-learn or try various hyperparameters for the DecisionTreeClassifier to improve the prediction performance.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

Special thanks to scikit-learn and pandas libraries for providing the necessary tools to build this music genre prediction model.

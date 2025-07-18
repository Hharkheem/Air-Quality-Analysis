# Air Quality Analysis Project

## Overview
This project analyzes the Air Quality UCI dataset to explore air quality metrics and predict specific pollutant levels using machine learning techniques. The dataset contains hourly air quality measurements, including pollutants like CO, NMHC, C6H6, NOx, and NO2, along with meteorological data such as temperature (T), relative humidity (RH), and absolute humidity (AH).

The analysis is performed in a Jupyter Notebook (`main.ipynb`) using Python, leveraging libraries like Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn for data processing, visualization, and modeling. The final model is saved as a pickle file (`AQModel.pkl`) for future use.

## Project Structure
- **`main.ipynb`**: Jupyter Notebook containing the data analysis, cleaning, visualization, and modeling pipeline.
- **`AQModel.pkl`**: Saved machine learning model (ExtraTreesRegressor) for predicting air quality metrics.
- **`AirQualityUCI.csv`**: The dataset used for analysis (not included in the repository but referenced in the notebook).
- **`README.md`**: This file, providing an overview of the project.

## Dataset
The dataset (`AirQualityUCI.csv`) includes the following columns:
- **Date**: Date of measurement (format: DD-MM-YYYY).
- **Time**: Time of measurement (format: HH:MM:SS).
- **CO(GT)**: Carbon monoxide concentration.
- **PT08.S1(CO)**: Sensor response for CO.
- **NMHC(GT)**: Non-methane hydrocarbons concentration.
- **C6H6(GT)**: Benzene concentration.
- **PT08.S2(NMHC)**: Sensor response for NMHC.
- **NOx(GT)**: Nitrogen oxides concentration.
- **PT08.S3(NOx)**: Sensor response for NOx.
- **NO2(GT)**: Nitrogen dioxide concentration.
- **PT08.S4(NO2)**: Sensor response for NO2.
- **PT08.S5(O3)**: Sensor response for ozone.
- **T**: Temperature (°C).
- **RH**: Relative humidity (%).
- **AH**: Absolute humidity.
- **Unnamed: 15, Unnamed: 16**: Empty columns (dropped during cleaning).

The dataset contains 9471 rows, with some missing or invalid values (e.g., -200) that are handled during data cleaning.

## Requirements
To run the notebook, install the required Python packages:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Usage
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/air-quality-analysis.git
   cd air-quality-analysis
   ```

2. **Obtain the Dataset**:
   - Download the Air Quality UCI dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Air+Quality).
   - Place the `AirQualityUCI.csv` file in the project directory.

3. **Run the Notebook**:
   - Open `main.ipynb` in Jupyter Notebook or JupyterLab.
   - Execute the cells sequentially to perform data loading, cleaning, visualization, and modeling.
   - Ensure the dataset path in the notebook points to the correct location of `AirQualityUCI.csv`.

4. **Load the Saved Model**:
   - The trained ExtraTreesRegressor model is saved as `AQModel.pkl`.
   - To load and use the model:
     ```python
     import pickle
     with open('AQModel.pkl', 'rb') as file:
         model = pickle.load(file)
     ```

## Notebook Workflow
1. **Data Loading**:
   - The dataset is loaded using Pandas from `AirQualityUCI.csv`.
   - Initial exploration is performed using `data.head()` and `data.describe()`.

2. **Data Cleaning**:
   - Unnecessary columns (`Unnamed: 15`, `Unnamed: 16`) are dropped.
   - Missing or invalid values (e.g., -200) are handled as per the dataset's documentation.

3. **Data Visualization**:
   - Distribution plots compare actual vs. predicted values using Seaborn's `distplot`.
   - A linear regression plot (`lmplot`) visualizes the relationship between actual and predicted values.

4. **Modeling**:
   - An ExtraTreesRegressor model is trained to predict air quality metrics.
   - The model is evaluated, and predictions are visualized against actual values.

5. **Model Saving**:
   - The trained model is saved as `AQModel.pkl` using the `pickle` library.

## Visualizations
- **Distribution Plot**: Shows the distribution of actual vs. predicted values for the target variable.
- **Linear Regression Plot**: Displays the relationship between predicted and actual values, highlighting model performance.

## Results
- The notebook demonstrates the effectiveness of the ExtraTreesRegressor in predicting air quality metrics.
- Visualizations provide insights into the distribution and correlation of predictions with actual values.
- The saved model (`AQModel.pkl`) can be reused for predictions on new data.

## Future Improvements
- Incorporate additional data preprocessing steps (e.g., handling outliers, feature scaling).
- Experiment with other machine learning models (e.g., Random Forest, XGBoost) for comparison.
- Add cross-validation to improve model robustness.
- Include feature importance analysis to identify key predictors of air quality.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or contributions, please open an issue or contact the repository owner.
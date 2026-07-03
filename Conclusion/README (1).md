# OptiCrop - Smart Agricultural Production Optimization Engine

OptiCrop is an AI-powered agricultural recommendation system designed to optimize crop production using environmental and soil parameters. It uses machine learning algorithms (Random Forest) combined with a Flask web application to provide intelligent crop recommendations.

## Prerequisites
- Python 3.10+
- The required dependencies are listed in `requirements.txt`.

## Getting Started

Follow these steps to run the project on your local machine.

### 1. Open the Terminal
Navigate to the project directory:
```bash
cd "e:\Intern Project\App\OptiCrop"
```

### 2. Activate the Virtual Environment
Activate the pre-configured virtual environment (Windows):
```bash
venv\Scripts\activate
```
*(You should see `(venv)` appear at the beginning of your terminal prompt.)*

### 3. (Optional) Install Dependencies
If you haven't installed the dependencies yet or are setting this up on a new machine, run:
```bash
pip install -r requirements.txt
```

### 4. (Optional) Train the Machine Learning Model
If you ever want to re-train the model, run data analysis, or regenerate the evaluation plots, execute the training script:
```bash
python train_model.py
```
This will compare multiple models (Logistic Regression, KNN, Decision Tree, Random Forest), select the best one, and save it as `model.pkl`. It also generates analysis plots in the `plots/` folder.

### 5. Run the Web Application
Start the Flask development server:
```bash
python app.py
```
Once the server starts, open your web browser and navigate to:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Project Structure
- `app.py`: The Flask web application backend.
- `train_model.py`: The Machine Learning pipeline script (EDA, preprocessing, model training, and evaluation).
- `model.pkl`: The saved best-performing ML model (Random Forest).
- `label_encoder.pkl`: The saved label encoder to map predictions back to crop names.
- `Crop_recommendation.csv`: The dataset used for training the model.
- `templates/`: HTML files for the web interface.
- `static/`: CSS and Images used by the frontend.
- `plots/`: Generated data analysis and model evaluation charts.
- `predictions_history.json`: Local database storing past crop predictions.

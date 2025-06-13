# Email Spam Classifier

This project is an Email Spam Classifier built using FastAPI for the backend and React for the frontend. The application is designed to classify emails as spam or not spam using a trained machine learning model.

## Project Structure

```
email-spam-classifier/
├── backend/                     # 🧠 ML backend (FastAPI)
│   ├── app/                     
│   │   ├── __init__.py         # Initializes the app package
│   │   ├── main.py              # FastAPI app with predict endpoint
│   │   ├── model.py             # Loads and uses trained model
│   │   ├── train_model.py       # Script to train + save model
│   │   └── spam_classifier.pkl   # Saved ML model
│   └── requirements.txt         # Python dependencies
│
├── frontend/                    # 🎨 React dashboard frontend
│   ├── public/                  # Static assets
│   ├── src/
│   │   ├── components/          # Reusable React components
│   │   ├── App.js               # Main app logic
│   │   └── index.js             # Entry point for React app
│   └── package.json             # React project metadata
│
├── data/                        # 📊 Raw and cleaned datasets
│   ├── spam.csv                 # Original dataset
│   └── cleaned_data.csv         # Optional cleaned version
│
├── README.md                    # 📄 Project overview
├── .gitignore                   # Files to ignore in version control
└── notion-dashboard-link.txt    # Optional: your Notion planning link
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd email-spam-classifier
   ```

2. **Backend Setup:**
   - Navigate to the `backend` directory.
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

3. **Train the Model:**
   - Run the training script to train and save the model:
     ```
     python app/train_model.py
     ```

4. **Run the FastAPI Server:**
   - Start the FastAPI application:
     ```
     uvicorn app.main:app --reload
     ```

5. **Frontend Setup:**
   - Navigate to the `frontend` directory.
   - Install the required Node.js packages:
     ```
     npm install
     ```
   - Start the React application:
     ```
     npm start
     ```

## Usage

- Access the FastAPI documentation at `http://127.0.0.1:8000/docs` to interact with the prediction endpoint.
- Use the React frontend to send emails for classification.

## License

This project is licensed under the MIT License.
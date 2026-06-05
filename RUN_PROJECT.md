# RUN PROJECT

## Step 1: Open Project

```powershell
cd D:\StoreIntelligence
```

---

## Step 2: Activate Virtual Environment

```powershell
venv\Scripts\activate
```

Expected:

```text
(venv) PS D:\StoreIntelligence>
```

---

## Step 3: Install Dependencies (Only if Needed)

```powershell
pip install -r requirements.txt
```

---

## Step 4: Start FastAPI Backend

Open Terminal 1:

```powershell
uvicorn backend.api.main:app --reload
```

Open in browser:

```text
http://127.0.0.1:8000/docs
```

---

## Step 5: Start Streamlit Dashboard

Open Terminal 2:

```powershell
streamlit run dashboard/app.py
```

Open in browser:

```text
http://localhost:8501
```

---

## Step 6: Run Detection Pipeline

Open Terminal 3:

```powershell
python backend/run_pipeline.py
```

This processes videos and generates analytics data.

---

## Useful Git Commands

Check project status:

```powershell
git status
```

Get latest code:

```powershell
git pull
```

Push changes:

```powershell
git add .
git commit -m "message"
git push
```

---

## Project Structure

```text
StoreIntelligence/
│
├── backend/
│   ├── analytics/
│   ├── api/
│   ├── detection/
│   ├── tracking/
│   └── run_pipeline.py
│
├── dashboard/
│   └── app.py
│
├── data/
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── RUN_PROJECT.md
```

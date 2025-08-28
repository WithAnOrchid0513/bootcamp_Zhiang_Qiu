# Project Description
This project aims to use random prediction to forecast the changes in stock prices. Random forest is a machine learning ensemble method that is widely used. It is an improvement based on decision trees, where decision trees use a tree-like model to represent decisions and their possible outcomes for prediction. Although decision trees are a good starting point, they are very sensitive to changes in input. Random forest, by combining multiple decision trees, reduces overfitting and variance problems, thus making the results more reliable.

# Stakeholder Persona
The main users will be individual and institutional investors who wish to adopt quantitative investment methods. Investors can utilize this project to enhance the accuracy of predictions and strengthen their trading strategies and risk management.

# bootcamp\_Zhiang\_Qiu — Quick Start

## Setup

```bash
# 1) Clone
git clone https://github.com/WithAnOrchid0513/bootcamp_Zhiang_Qiu.git
cd bootcamp_Zhiang_Qiu

# 2) Install deps
pip install -r requirements.txt
```

## Repo Layout (what goes where)

* **homework/** — each HW in its own folder (`homework0`, `homework1`, ...). Include notebooks, data, and any `README.md` per HW.
* **project/** — capstone files and notebooks with clear comments

## Use From a Fresh `git pull`

```bash
# for a local copy
git pull origin main

pip install -r requirements.txt

cd homework/homeworkN
jupyter lab
```

## Example for Flask API

```bash
cd project
def run_flask():
    app.run(port=5000)

# Launch Flask in a separate thread
threading.Thread(target=run_flask).start()
```

**Shut down a stuck server**

```bash
lsof -i :5000
kill -9 
```

## Assumptions, Risks, Next Steps

* **Assumptions**: `requirements.txt` contains all the libraries needed for this project.
* **Risks**: Data leakage (look‑ahead bias), non‑stationarity in finance data, inconsistent envs across machines.
* **Next Steps**: Sensitivity analysis and try on different models.
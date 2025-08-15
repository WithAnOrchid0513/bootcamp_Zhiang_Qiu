# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Volatility forecasting is an important task in risk management, as it helps financial institutions control their risk exposure and regulators monitor these exposures. Furthermore, volatility is also a key input in valuing options, as it determines how expensive the option is. A wide range of models can be applied to forecast volatility, such as econometric models like Generalized AutoRegressive Conditional Heteroskedasticity (GARCH) and machine learning models like Long Short-Term Memory (LSTM). 

## Stakeholder & User
The main users are financial institutions and regulators. Financial institutions use it for a wide range of purposes, and it can be mainly separated into profit-making or hedging. For example, A portfolio manager may implement a short straddle strategy when he believes volatility is likely to decrease, or purchase call/put options to hedge risk. A regulator can monitor the volatility and determine how much reserve a financial institution should hold.
## Useful Answer & Decision
Volatility forecasting is predictive in nature. It uses past data to predict the future. There are lots of models that can be implemented, like GARCH, RNN, LSTM, etc. Metrics like RMSE can be used to measure how these models perform. 

## Assumptions & Constraints
Assumptions and constraints differ between the models. Some common ones include the assumption that past data can be used to predict the future and that the data is stationary. Some constraints are data quality and availability. High-quality financial data is hard to find, especially for higher frequency ones. 

## Known Unknowns / Risks
Models generally have a hard time predicting sudden changes in volatility, like what happened during the financial crisis in 2008. However, it is these extreme tail risks that cause banks to fail. 

## Lifecycle Mapping
Goal → Stage → Deliverable
Data Collection -> Data Preprocessing -> Workable Data
Exploratory Data Analysis (EDA) -> Find important statistical properties
Modeling with various models -> Some baseline models that can be used
Backtesting -> Ensuring the robustness of the models
Hyperparameter search -> Improve model quality
Evaluation of models -> Compare the performance and present the best model

## Repo Plan
/data/ stores raw data, /src/ source, /notebooks/ python implementations, /docs/ documentations; cadence for updates depends on the freqency of data (e.g. daily)

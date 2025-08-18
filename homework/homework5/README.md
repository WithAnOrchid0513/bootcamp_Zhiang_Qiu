Folder structure: 
data/raw/ — raw data
data/processed/ — processed data
src/, notebooks/, README.md — code, experiments, and documentation.

Format:
CSV: easy to understand and human readable.
Parquet: more efficient but requires an engine to read. Columnar, compressed, preserves types.

The code reads using Pathlib instead of hard-coded path. It reads using load_dotenv() and it helps keep the API key secret.

import pandas as pd
import os

# First, see where Python is looking
print("Current directory:", os.getcwd())

# List all files in current directory
print("Files here:", os.listdir())

df = pd.read_csv('Sources/csv_files/brief.csv')
latex_code = df.to_latex(index=True)

# Save with UTF-8 encoding
with open('annotated_bib/table_output.tex', 'w', encoding='utf-8') as f:
    f.write(latex_code)

# \input{table_output.tex}
# this document exports the information from experimental.csv to a latex table to use in the .tex document
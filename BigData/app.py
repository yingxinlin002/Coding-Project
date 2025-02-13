from flask import Flask, render_template, send_file
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    dfA = pd.read_csv('tableA.csv')
    dfB = pd.read_csv('tableB.csv')

    return render_template('table.html', 
                           dataA = dfA.to_html(index=False), 
                           dataB = dfB.to_html(index=False))
    
CSV_DATA_DIR = "."

@app.route('/download_table_a')
def download_table_a():
    file_path = os.path.join(CSV_DATA_DIR, 'tableA.csv')
    return send_file(
        file_path, 
        mimetype='text/csv', 
        as_attachment=True, 
        download_name='tableA.csv'
    )

@app.route('/download_table_b')
def download_table_b():
    file_path = os.path.join(CSV_DATA_DIR, 'tableB.csv')
    return send_file(
        file_path, 
        mimetype='text/csv', 
        as_attachment=True, 
        download_name='tableB.csv'
    )

@app.route('/download_source_code')
def download_source_code():
    file_path = os.path.join(CSV_DATA_DIR, 'Homework1.py')
    return send_file(
        file_path, 
        mimetype='text/x-python', 
        as_attachment=True, 
        download_name='source_code.py'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

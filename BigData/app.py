from flask import Flask, render_template, send_file
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assignment1/')
def assignment1():
    dfA = pd.read_csv('tableA.csv')
    dfB = pd.read_csv('tableB.csv')

    return render_template('assignment1.html', 
                           dataA = dfA.to_html(index=False), 
                           dataB = dfB.to_html(index=False))

@app.route('/assignment2/')
def assignment2():
    return render_template('assignment2.html')

@app.route('/assignment3/')
def assignment3():
    return render_template('assignment3.html')
    
CSV_DATA_DIR = "."
PDF_DATA_DIR = "."

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

@app.route('/download_table_c')
def download_table_c():
    return send_file('static/tableC.csv', 
                     mimetype='text/csv', 
                     as_attachment=True, 
                     download_name='tableC.csv')

@app.route('/download_pdf')
def download_pdf():
    file_path = os.path.join(PDF_DATA_DIR, 'Assignment2Report.pdf')
    return send_file(
        file_path, 
        mimetype='application/pdf', 
        as_attachment=True, 
        download_name='Assignment2Report.pdf'
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
from flask import Flask, render_template, request, send_file
import csv
from FlipkartMobile import run

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index3.html')

# Define the route to handle form submission
@app.route('/scrape', methods=['POST'])
def scrape():
    # Get the starting and ending page numbers from the form
    start_page = int(request.form['start_page'])
    end_page = int(request.form['end_page'])

    # Calling existing scraping function here
    scraped_data = run(start_page, end_page)
    file_path = 'PhonesInfoPage{}to{}.csv'.format(start_page,end_page)
    scraped_data.to_csv(file_path,index=False)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import csv

def OpenLibraryData(soup, book_data):
    book_elements = soup.find_all('li', class_='searchResultItem')

    for book_element in book_elements:
        title = ""
        author = ""
        rating = ""

        title_element = book_element.find('h3', itemprop='name', class_='booktitle')
        if title_element:
            title_link = title_element.find('a', class_='results')
            if title_link:
                title = title_link.text.strip()

        author_element = book_element.find('span', itemprop='author', class_='bookauthor')
        if author_element:
            author_link = author_element.find('a')
            if author_link:
                author = author_link.text.strip()

        rating_element = book_element.find('span', itemprop='aggregateRating', class_='ratingsByline')
        if rating_element:
            rating_value_element = rating_element.find('span', itemprop='ratingValue')
            if rating_value_element:
                rating = rating_value_element.text.strip().split(' ')[0] # Extract only the number part
                try:
                    rating = float(rating)  # Convert to float if possible
                except ValueError:
                    rating = None # Handle cases where rating is not a number

        book_data.append({
            'title': title,
            'author': author,
            'rating': rating,
        })

def OpenLibraryCrawler():
    link = "https://openlibrary.org/search?subject=Horror"

    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")

    book_data = []
    OpenLibraryData(soup, book_data)

    for i in range(49):
        # Each web page contains 20 book information, needs 49 more pages
        links = (link + "&page=" + str(i+2))

        response = requests.get(links)
        soup = BeautifulSoup(response.content, "html.parser")

        OpenLibraryData(soup, book_data)
        print(book_data)

    return book_data

def save2csv(filename, data, header=None):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        if header:
            writer.writerow(header)  # Write the header row

        if isinstance(data[0], dict):  # Check if data is a list of dictionaries
            # Write data rows using dictionary keys as header if no explicit header
            if not header:
              writer.writerow(data[0].keys())
            for row in data:
                writer.writerow(row.values())
        elif isinstance(data[0], list) or isinstance(data[0], tuple):  # Check if it's a list of lists or tuples
            for row in data:
                writer.writerow(row)
        else:
            raise TypeError("Data must be a list of dictionaries or lists/tuples.")

def goodreadData(soup, book_data):
    book_elements = soup.find_all('tr', itemscope=True, itemtype="http://schema.org/Book")

    for book_element in book_elements:
        title = ""
        author = ""
        rating = ""

        title_element = book_element.find('a', class_='bookTitle')
        if title_element:
            title = title_element.find('span', itemprop='name').text.strip()  # Get title from span

        author_element = book_element.find('span', itemprop='author')
        if author_element:
            author_link = author_element.find('a', class_='authorName')
            if author_link:
                author = author_link.find('span', itemprop='name').text.strip() # Author's name is in a nested span

        rating_element = book_element.find('span', class_='minirating')
        if rating_element:
            rating_text = rating_element.text.strip()
            try:
                rating = float(rating_text.split(" ")[0])  # Extract number part of rating string
            except (ValueError, IndexError):
                rating = None  # Handle cases where rating is not a number

        book_data.append({
            'title': title,
            'author': author,
            'rating': rating
        })

def goodreadsCrawler():

    link = "https://www.goodreads.com/list/show/2455.The_Most_Disturbing_Books_Ever_Written" # 100 book list in this web page
    # response = requests.get(link) blocked

    # get html through selenium
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get(link)

    element_present = EC.presence_of_all_elements_located((By.CLASS_NAME, 'bookTitle'))
    WebDriverWait(driver, 20).until(element_present)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    book_data = []
    goodreadData(soup, book_data)

    driver.quit()  # Close the browser

    for i in range(9):
        # Each web page contains 100 book information, needs 9 more pages
        links = (link + "?&page=" + str(i+2))

        # get html through selenium
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.get(links)

        element_present = EC.presence_of_all_elements_located((By.CLASS_NAME, 'bookTitle'))
        WebDriverWait(driver, 20).until(element_present)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        goodreadData(soup, book_data)

        driver.quit()  # Close the browser
        print(book_data)

    return book_data

#save2csv('OpenLibraryData.csv', OpenLibraryCrawler())
def save2csv2(file_name, goodreadsData):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = goodreadsData[0].keys()  # Get the keys (column names) from the first dictionary
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write the header row
        for row in goodreadsData:
            writer.writerow(row)  # Write each row of data

def add_id_to_csv(input_filename, output_filename):

    try:
        with open(input_filename, 'r', encoding='utf-8') as infile, \
                open(output_filename, 'w', newline='', encoding='utf-8') as outfile:

            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            header = next(reader)  # Read the header row
            header.insert(0, 'id')   # Insert 'id' at the beginning of the header
            writer.writerow(header)  # Write the updated header

            row_id = 1  # Start ID from 1 (you can change this if you want to start from 0)
            for row in reader:
                row.insert(0, row_id)  # Insert ID at the beginning of each row
                writer.writerow(row)
                row_id += 1

        print(f"ID column added. File saved as {output_filename}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



#save2csv2('goodreadsData.csv', goodreadsCrawler())
input_file = "goodreadsData.csv"
output_file = "tableA.csv"
#add_id_to_csv(input_file, output_file)

save2csv('OpenLibraryData.csv', OpenLibraryCrawler())
input_file = "OpenLibraryData.csv"
output_file = "tableB.csv"
add_id_to_csv(input_file, output_file)
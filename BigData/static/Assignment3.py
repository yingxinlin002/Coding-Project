# Table C will have the following columns in csv format:
# 1. ID (int)
# 2. Itable_id (int)
# 3. rtable_id (int)
# 4. Itable_title (str)
# 5. rtable_title (str)
# 6. Itable_author (str)
# 7. Itable_rating (float)

from math import floor

# time complexity: O(len(s1)*len(s2))
def jaro_distance(s1, s2):
     # If the strings are equal
    if s1 == s2:
        return 1.0
    
    # Length of the strings
    Len1 = len(s1)
    Len2 = len(s2)

    # Maximum distance upto which matching is allowed
    max_dist = floor(max(Len1, Len2) / 2) - 1

    # Count of matches
    match = 0

    # Hash for matches
    hash_s1 = [0] * Len1
    hash_s2 = [0] * Len2

    # Traverse through the first string
    for i in range(Len1):

        # check for matches
        for j in range(max(0, i - max_dist), min(Len2, i + max_dist + 1)):
            
            # if there is no match
            if s1[i] == s2[j] and hash_s2[j] == 0:
                hash_s1[i] = 1
                hash_s2[j] = 1
                match += 1
                break
    
    # If there is no match
    if match == 0:
        return 0.0
    
    # Number of transpositions
    t = 0
    point = 0

    # Count of transpositions
    for i in range(Len1):
        if hash_s1[i]:

            # Find the next match
            while hash_s2[point] == 0:
                point += 1
            
            if s1[i] != s2[point]:
                t += 1
            point += 1

    t /= 2

    # Return the Jaro Similarity
    return (match / Len1 + match / Len2 + (match - t) / match) / 3.0

# Jaro Winkler Similarity
def jaro_Winkler(s1, s2):
    # Jaro Similarity
    jaro = jaro_distance(s1, s2)

    # If the jaro similarity is above a threshold
    if (jaro > 0.7):

        # Find the length of common prefix
        prefix = 0

        for i in range(min(len(s1), len(s2))):

            # If the characters are equal
            if s1[i] == s2[i]:
                prefix += 1
            # If the characters are not equal
            else:
                break

        # Maximum length of common prefix
        prefix = min(4, prefix)

        # Return the Jaro Winkler Similarity
        jaro += 0.1 * prefix * (1 - jaro)

    return jaro
    

import csv

def matcher(tableA_path, tableB_path, tableC_path):
    tableA = []
    tableB = []

    # read csv files
    with open(tableA_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tableA.append(row)
    with open(tableB_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tableB.append(row)

    matches = []
    match_id = 0
    row_count = 0

    for row_a in tableA:

        # Counter
        row_count += 1
        if row_count % 100 == 0:
            print(f"Matching row {row_count}")

        for row_b in tableB:

            # Jaro Winkler Similarity
            jaro_winkler_title = jaro_Winkler(row_a['title'], row_b['title'])

            # If the similarity is above a threshold
            if jaro_winkler_title > 0.90:
                match = {
                    'ID': match_id,
                    'ltable_id': 'a' + row_a['id'],
                    'rtable_id': 'b' + row_b['id'],
                    'ltable_title': row_a['title'],
                    'rtable_title': row_b['title'],
                    'ltable_author': row_a['author'],
                    'ltable_rating': row_a['rating'],
                }
                matches.append(match)
                match_id += 1

    # Save the matches to a csv file
    with open(tableC_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['ID', 'ltable_id', 'rtable_id', 'ltable_title', 'rtable_title' ,'ltable_author', 'ltable_rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in matches:
            writer.writerow(row)

tableA_path = 'C:\\Users\\yingx\\OneDrive\\Documents\\Coding\\BigData\\tableA.csv'
tableB_path = 'C:\\Users\\yingx\\OneDrive\\Documents\\Coding\\BigData\\tableB.csv'
matcher(tableA_path, tableB_path, 'tableC.csv')
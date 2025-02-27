library(readxl)
tableA <- read_excel("tableA.xlsx")
View(tableA)

df <- data.frame(tableA)

# Function to calculate and report missing values
report_missing <- function(data) {
  missing_summary <- data.frame(
    Column = names(data),
    Missing_Count = colSums(is.na(data)),
    Total_Rows = nrow(data)
  )
  
  missing_summary <- missing_summary %>%
    mutate(
      Missing_Percentage = (Missing_Count / Total_Rows) * 100,
      Missing_Fraction = Missing_Count / Total_Rows
    )
  
  return(missing_summary)
}

# Using dplyr for cleaner code
library(dplyr)
missing_report <- report_missing(df)
print(missing_report)

# Function to analyze textual column
analyze_text_column <- function(data, column_name) {
  if (!is.character(data[[column_name]])) {
    stop("Column must be textual (character type).")
  }
  
  lengths <- nchar(data[[column_name]])
  average_length <- mean(lengths)
  min_length <- min(lengths)
  max_length <- max(lengths)
  
  return(data.frame(
    Column = column_name,
    Average_Length = average_length,
    Min_Length = min_length,
    Max_Length = max_length
  ))
}

# Analyze the 'title' column
title_analysis <- analyze_text_column(df, "title")
print(title_analysis)

# Analyze the 'author' column
author_analysis <- analyze_text_column(df, "author")
print(author_analysis)

# plot the histogram
plot_histogram <- function(data, column_name, title) {
  values <- data[[column_name]]
  
  if (is.numeric(values)) {
    hist(values, 
         main = title,
         xlab = column_name,
         col = "lightblue",
         border = "darkblue")
    
  } else if (is.character(values)) {
    lengths <- nchar(values)
    hist(lengths,
         main = title,
         xlab = paste("Length of", column_name),
         col = "lightgreen",
         border = "darkgreen")
  } else {
    print(paste("Cannot create histogram for column of type:", class(values)))
  }
}

# Plot histograms 
plot_histogram(df, "id", "Histogram of Prices")
plot_histogram(df, "title", "Histogram of Title Lengths")
plot_histogram(df, "author", "Histogram of Author Name Lengths")
plot_histogram(df, "rating", "Histogram of Ratings")


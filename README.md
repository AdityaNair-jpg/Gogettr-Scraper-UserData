# Gettr User Data Scraper

This Python script is designed to scrape posts from a specified user's profile on the social media platform Gettr. It utilizes the `gogettr` library to fetch the user's activity feed and saves the collected data into a structured JSON file for further analysis.

## Features

-   **Targeted Scraping:** Scrape posts from any public Gettr user profile by simply specifying their username.
-   **Data Export:** All scraped data is saved in a clean, human-readable JSON format.
-   **Configurable Depth:** Easily set the maximum number of posts you wish to retrieve.
-   **Error Handling:** Includes basic error handling to skip malformed posts and continue the scraping process.
-   **Console Feedback:** Provides real-time progress updates and a final summary directly in your terminal.

## Prerequisites

Before running the script, you need to have Python 3 installed on your system.

## Installation

You will need to install the `gogettr` library. You can install it using pip:

```bash
pip install gogettr
```

## How to Use

1.  **Configure the Script:** Open the `scrape_gettr.py` file in a text editor and modify the configuration variables at the top:
    -   `TARGET_USERNAME`: Set this to the Gettr username you want to scrape (e.g., `"gatewaypundit"`).
    -   `MAX_POSTS`: Define the maximum number of posts to fetch.
    -   `OUTPUT_FILE`: The script will automatically name the output file based on the `TARGET_USERNAME`. You can change this logic if needed.

2.  **Run the Script:** Execute the script from your terminal using the following command:

    ```bash
    python scrape_gettr.py
    ```

3.  **Find the Output:** Once the script finishes, it will create a new JSON file (e.g., `gettr_user_gatewaypundit.json`) in the same directory. This file contains all the scraped post data.

## Output Data Structure

The output JSON file contains a list of post objects. Each object represents a single post and includes various data points, such as:

-   `_id`: The unique identifier for the post.
-   `uid`: The user ID of the post's author.
-   `txt`: The raw text content of the post.
-   `cdate`: The creation date of the post (Unix timestamp).
-   `udate`: The last updated date of the post (Unix timestamp).
-   `lkbpst`: The number of likes.
-   `cm`: The number of comments.
-   `shbpst`: The number of shares (reposts).
-   `prevsrc`: URL for any link preview included in the post.
-   `vid`: Link to video content, if present.
-   And other metadata related to the post and user activity.

For concrete examples, you can inspect the provided `gettr_user_gatewaypundit.json` and `gettr_user_gettr.json` files.

## Disclaimer

This tool is intended for educational and research purposes only. The developer of this script is not responsible for any misuse.

## README: News Quiz Generator with ChatGPT

### Description

This Python program utilizes OpenAI's ChatGPT API, alongside web scraping tools, to generate multiple-choice reading comprehension quizzes based on articles from the NHK Easy News website. These quizzes are tailored for JLPT N2 level students. The program selects a random news article, extracts its content, and then leverages ChatGPT to create a relevant quiz.

### Prerequisites

To run the program, ensure you have the following Python libraries installed:
- openai
- chardet
- requests
- BeautifulSoup (bs4)

You can install these using `pip`:

```bash
pip install openai chardet requests beautifulsoup4
```

### Configuration

1. **API Key:** Ensure you have a valid OpenAI API key. Store the key in a separate file named `openai_key.py` in the format:
```python
api_key = "YOUR_API_KEY_HERE"
```

2. Make sure that the `openai_key.py` file is in the same directory as the main program file.

### Usage

To generate a quiz:

1. Navigate to the program's directory.
2. Run the main Python script:
```bash
python main_program_name.py
```

3. The program will display:
   - A link to the selected NHK Easy News article.
   - The article's title, date, and content.
   - The generated reading comprehension quiz.

### Functions Overview

- `get_random_news_url()`: Retrieves a random news article URL from NHK Easy News.
  
- `get_news_article(url: str)`: Extracts the title, date, and content of the provided NHK Easy News article URL.
  
- `main()`: Orchestrates the entire process - fetching a random news article, generating the quiz using ChatGPT, and displaying the results.

### Notes

- The program fetches the latest four news articles from NHK Easy News and randomly selects one for the quiz generation.
  
- Please note that while the program is designed to operate seamlessly, occasional issues may arise due to changes in the NHK Easy News website's structure. Regular maintenance and updates to the web scraping logic may be necessary.

# LLM Analysis Quiz Solver

A FastAPI-based automation service designed to solve dynamic quiz tasks by rendering web pages, extracting task information, processing PDF-based data, and submitting computed answers within a configurable time limit.

## Overview

This project demonstrates an end-to-end automation workflow combining:

- FastAPI
- Asynchronous Python programming
- Playwright browser automation
- Web-page rendering and scraping
- PDF table extraction
- Data processing with Pandas
- HTTP API communication
- Docker-based deployment
- Environment-based configuration

The application exposes an API endpoint that accepts a quiz task URL and processes the task automatically.

## Architecture

```text
Client
  |
  v
FastAPI Application
  |
  v
Quiz Worker
  |
  +-- Playwright
  |     +-- Render dynamic web pages
  |
  +-- URL / task extraction
  |
  +-- PDF Downloader
  |
  +-- PDF Processing
        +-- Pandas + pdfplumber
  |
  v
Answer Submission
```
## Project Structure

```text
llm-analysis-quiz/
│
├── app/
│   ├── config.py
│   ├── main.py
│   ├── processing.py
│   ├── prompt_tester.py
│   ├── scraping.py
│   ├── utils.py
│   └── worker.py
│
├── prompts/
│   ├── system_prompts.txt
│   └── user_prompts.txt
│
├── Dockerfile
├── playwright.install.sh
├── requirements.txt
└── .gitignore
```
## Key Components
## FastAPI API

The application provides the following endpoints:

- `GET /` — basic service status
- `GET /health` — service health and timeout information
- `POST /solve` — starts the quiz-solving workflow

## Browser Automation

Playwright is used to render JavaScript-driven pages and extract the relevant page content required for the automated workflow.

## Task and URL Extraction

The application identifies relevant download and submission URLs from rendered page content and follows the task workflow programmatically.

## PDF Processing

PDF files are downloaded and processed using:

- `pdfplumber` for PDF text and table extraction
- `Pandas` for tabular data processing
- Regular expressions for extracting numerical information

The processing workflow includes extracting relevant numerical data from PDF tables and calculating aggregate values required by the task.

## Asynchronous Processing

The workflow uses Python asynchronous programming with:

- `asyncio`
- `aiohttp`
- Asynchronous Playwright APIs

A configurable timeout helps prevent an individual task from running indefinitely.

## Configuration

Application configuration is provided through environment variables rather than hardcoded sensitive values.

Example:

QUIZ_SECRET=<your-secret>
QUIZ_TIMEOUT=170
PLAYWRIGHT_HEADLESS=1

Create the required environment variables according to your local setup.

Never commit API keys, secrets, passwords, or `.env` files to source control.

## Running Locally

## 1. Clone the Repository

git clone https://github.com/SimiImmaculate/llm-analysis-quiz.git
cd llm-analysis-quiz

## 2. Create a Virtual Environment
python -m venv .venv

## Activate it on Windows:

.venv\Scripts\Activate.ps1
## 3. Install Dependencies

pip install -r requirements.txt

## 4. Install Playwright Browser Dependencies

Run the project's Playwright installation script as required by your environment.

## 5. Configure Environment Variables

Set the required environment variables before starting the application.

For example:

$env:QUIZ_SECRET="<your-secret>"
$env:QUIZ_TIMEOUT="170"
$env:PLAYWRIGHT_HEADLESS="1"

## 6. Start the FastAPI Application

uvicorn app.main:app --reload

The API will be available at:

http://localhost:8000

Interactive API documentation is available at:

http://localhost:8000/docs

## Example API Request

A request to the `/solve` endpoint can be structured as:

{
  "email": "your-email@example.com",
  "secret": "your-secret",
  "url": "https://example.com/quiz"
}

Send the request to:

POST /solve 

Use your own valid task URL, email, and secret when running the application.

## Technologies Used

| Category           | Technologies     |
| ------------------ | ---------------- |
| Programming        | Python           |
| API                | FastAPI          |
| Async Programming  | asyncio, aiohttp |
| Browser Automation | Playwright       |
| Data Processing    | Pandas           |
| PDF Processing     | pdfplumber       |
| Server             | Uvicorn          |
| Containerization   | Docker           |
| Version Control    | Git, GitHub      |

## Skills Demonstrated
- Python application development
- REST API development
- Asynchronous programming
- Browser automation
- Web scraping
- PDF data extraction
- Data processing
- Error handling
- Timeout management
- Environment-based configuration
- Docker fundamentals
- Git and GitHub workflow

## Project Workflow

The application follows a multi-stage automated workflow:

1. Receive a quiz task through the API.
2. Render the task page using Playwright.
3. Extract relevant task information and URLs.
4. Download required PDF resources.
5. Extract structured information from the PDF.
6. Process the extracted data using Python and Pandas.
7. Calculate the required result.
8. Submit the computed answer through the appropriate endpoint.

This workflow demonstrates how browser automation, document processing, data analysis, and API communication can be integrated into a single Python application.

## Project Purpose

This project was developed as a practical exercise in building an automated, API-driven data-processing workflow involving dynamic web content, document processing, asynchronous programming, and programmatic answer submission.

It demonstrates how multiple Python technologies can be combined to build a structured automation pipeline.

## Security

Sensitive configuration is intentionally separated from the source code.

The repository:

- Uses environment variables for sensitive configuration.
- Excludes environment files from version control.
- Excludes local virtual environments from version control.
- Does not include API credentials or other private secrets.

When deploying or running the application, provide sensitive values through the appropriate environment configuration rather than hardcoding them in source files.

## Author

**Simi Immaculate**

M.Sc. Mathematics | Data Science & Machine Learning

GitHub: [SimiImmaculate](https://github.com/SimiImmaculate)

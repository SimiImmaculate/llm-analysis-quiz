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
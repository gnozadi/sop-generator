# Automated Statement of Purpose (SOP) Generator

## Table of Contents

1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [How to Run the Project](#how-to-run-the-project)
4. [Implementation Details](#implementation-details)
5. [References](#references)

## Introduction

This project creates a customized Statement of Purpose (SOP) based on user inputs and data gathered from university datasets. By inputting details like university name, program, GPA, and relevant experience, the program generates a tailored SOP for the user's specific application.

## Project Overview

The SOP Generator performs the following tasks:

1. **User Input Collection**: Takes the target university and program from the user, along with relevant keywords like GPA, past education, and work experience.
2. **Keyword Expansion**: Searches a dataset of university information to add relevant keywords, such as program-specific terms and university ranking.
3. **SOP Generation**: Utilizes the online tool [Moonbeam](https://www.gomoonbeam.com/) to create an SOP that includes the input keywords directly or indirectly.

The project includes **web crawling**, **text preprocessing**, and **automated text generation**.

## How to Run the Project

1. **Setup**:

   - Ensure you have Python installed along with the necessary libraries (`selenium`).
   - Install libraries via pip if needed:
     ```bash
     pip install selenium
     ```

2. **Crawling Setup**:

   - Register an account on [Moonbeam](https://www.gomoonbeam.com/) and save your credentials.
   - Configure the Selenium browser profile path to avoid re-login with each execution.

3. **Run the Project**:
   ```bash
   python crawl.py
   ```

## Implementation Details

- **Web Crawling**: Uses `selenium` to gather data from Moonbeam. Implements scroll and wait techniques to handle dynamic page loading.
  - To reduce detection, the crawler includes random `sleep` intervals and uses a persistent browser profile.
- **Text Preprocessing**:
  - **Steps**: Text cleaning, stop-word removal, tokenization, stemming/lemmatization.
  - Generates a list of keywords based on program requirements, university rank, tuition, and prerequisites. The keywords are visualized with a word cloud.
- **SOP Generation**: Keywords are fed into Moonbeam’s "Student Essay" wizard, which generates an SOP draft with relevant terms.

## References

- [Getting Started with Text Preprocessing - Kaggle](https://www.kaggle.com/code/sudalairajkumar/getting-started-with-text-preprocessing#Introduction)
- [Moonbeam SOP Generator](https://app.gomoonbeam.com/headstart/template?collection=student)

---

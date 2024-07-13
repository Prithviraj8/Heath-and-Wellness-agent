# Health and Wellness Coach - Local Setup

This repository contains the local setup for the AI agents used in the Health and Wellness Coach project. It allows you to test and develop the AI agents independently before integrating them into the backend API.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Setup and Installation](#setup-and-installation)
3. [Usage](#usage)
4. [Contributing](#contributing)

## Project Overview

The Health and Wellness Coach project leverages AI agents to generate personalized fitness, nutrition, and mental health plans. This repository provides the local setup for these agents, allowing for independent testing and development.

## Setup and Installation

### Prerequisites

- Python 3.9+
- Virtual Environment

### Installation Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Prithviraj8/Health-and-Wellness-agent.git
    cd Health-and-Wellness-agent
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
    # Or set up a conda env
    conda create -n venv python=3.9
    conda activate venv
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    # or 
    pip3 install -r requirements.txt
    ```

4. **Setup Environment Variables**:
    ```bash
    export OPENAI_API_KEY=<your_openai_api_key>
    export TAVILY_API_KEY=<your_tavily_api_key>
   ```

## Usage

1. **Run the Local Agents**:
    - Execute the `main.py` script to test the AI agents locally.
    ```bash
    python main.py
    ```

2. **Input User Data**:
    - The script will prompt you to enter user data. Follow the prompts to input the necessary information.

3. **Review the Generated Plans**:
    - The AI agents will generate personalized fitness, nutrition, and mental health plans based on the provided user data.

## Contributing

1. **Fork the Repository**:
    - Click on the "Fork" button at the top right of this repository's page.

2. **Clone Your Fork**:
    ```bash
    git clone https://github.com/your-username/Health-and-Wellness-agent.git
    cd Health-and-Wellness-agent
    ```

3. **Create a Feature Branch**:
    ```bash
    git checkout -b feature-branch-name
    ```

4. **Make Changes**:
    - Implement your changes in the feature branch.

5. **Commit Changes**:
    ```bash
    git add .
    git commit -m "Your commit message"
    ```

6. **Push Changes**:
    ```bash
    git push origin feature-branch-name
    ```

7. **Create a Pull Request**:
    - Go to your forked repository on GitHub and click on the "Pull Request" button to submit your changes for review.

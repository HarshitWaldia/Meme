# Mood-Based Recommender System 🎵😂🎮🍕

This project is a Python-based console application that analyzes a user's mood and provides personalized recommendations for activities like listening to music, viewing memes, playing games, or ordering food. It also logs user interactions in a MySQL database for potential future analysis.

## 🌟 Key Features

-   **Interactive Mood Analysis**: Asks the user for their name, basic details, and current mood.
-   **Personalized Suggestions**:
    -   Feeling **sad**? Get suggestions for motivational audio, music, or funny memes.
    -   Feeling **happy**? Enhance your mood with upbeat music, games, or memes.
    -   In a **gaming** mood? Jump straight into online games or listen to a gaming playlist.
    -   Feeling **hungry**? Tell the app what you crave, and it will open a relevant food delivery website.
-   **Data Logging**: Securely stores the user's mood and basic, non-identifiable information in a MySQL database.
-   **Built-in Media Players**:
    -   A GUI-based music player built with Tkinter and Pygame.
    -   A web-based meme viewer using a local HTML file.

## ⚙️ How It Works

The application follows a simple command-line flow:

1.  **User Input**: The script `project_meme.py` prompts the user for their name, age, gender, city, and current mood.
2.  **Mood Validation**: The entered mood is cross-referenced with a comprehensive dictionary of synonyms (`module_Mood.py`) to understand the user's feelings.
3.  **Database Entry**: The user's details and mood are recorded in a `moodlog` table within a MySQL database named `healthsys`.
4.  **Recommendation Engine**: Based on the identified mood, the application presents a menu of choices.
5.  **Action Execution**:
    -   **Music**: Launches a Tkinter-based music player or plays a specific track using `playsound`.
    -   **Memes**: Opens the `Untitled-1.html` file in the default web browser to display a collection of memes.
    -   **Games**: Opens `poki.com` in a new browser tab for instant gaming.
    -   **Food**: Opens the website for a specific food item (e.g., `dominos.co.in` for pizza).

## 🛠️ Tech Stack

-   **Backend**: Python 3
-   **Database**: MySQL
-   **Python Libraries**:
    -   `mysql-connector-python` (for database interaction)
    -   `pygame` (for audio playback)
    -   `playsound` (for simple audio playback)
    -   `Pillow` (for image handling)
    -   `tkinter` (for the music player GUI)
-   **Frontend (Meme Viewer)**: HTML & JavaScript

## 🚀 Setup and Installation

### Prerequisites

-   Python 3.x
-   MySQL Server

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Meme.git
cd Meme
```

### 2. Install Dependencies

Install the required Python packages using pip.

```bash
pip install mysql-connector-python pygame playsound Pillow
```

### 3. Set Up the Database

You need to create the database and table for the application to store its data.

1.  Open your MySQL client.
2.  Create the database:
    ```sql
    CREATE DATABASE healthsys;
    ```
3.  Use the new database:
    ```sql
    USE healthsys;
    ```
4.  Create the `moodlog` table:
    ```sql
    CREATE TABLE moodlog (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255),
        Age INT,
        Gender VARCHAR(50),
        City VARCHAR(255),
        Mood VARCHAR(255),
        Health VARCHAR(50),
        LogTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```

### 4. Configure the Application

#### **Critical Step: Update Paths and Credentials**

The current code uses **hardcoded absolute paths and database credentials**. You **must** change these for the application to work on your machine.

1.  **Database Connection (`project_meme.py`)**:
    Open `project_meme.py` and update the `mysql.connector.connect()` block with your MySQL credentials.

    ```python
    # Lines 13-17 in project_meme.py
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "your_mysql_user",      # CHANGE THIS
        password = "your_mysql_password", # CHANGE THIS
        database ="healthsys"
    )
    ```

2.  **File Paths (`Untitled-1.html` & `project_meme.py`)**:
    The code uses absolute file paths which will prevent it from running on other machines. Search the project for paths like `C:\Users\harsh\mini_project_2\...` and replace them with **relative paths**.

    -   **Example in `Untitled-1.html`**:
        -   **Find:** `src='/C:/Users/harsh/mini_project_2/memes/img1.jpg'`
        -   **Replace with:** `src='memes/img1.jpg'`
    -   **Example in `project_meme.py`**:
        -   **Find:** `html_file_path = r"C:\Users\harsh\mini_project_2\Untitled-1.html"`
        -   **Replace with:** `html_file_path = "Untitled-1.html"`

## ▶️ How to Run

Once the setup and configuration are complete, run the main script from your terminal:

```bash
python project_meme.py
```

Follow the on-screen prompts to interact with the application.

## 📁 Project Structure

```
├── AUDIO/                  # Audio files for the project
├── IMAGES/                 # Image assets (potentially for a different feature)
├── memes/                  # Meme images displayed in the HTML viewer
├── __pycache__/            # (Should be in .gitignore)
├── Project_Report.pdf      # Project documentation
├── docx_report_mood_analysis.docx # Project documentation
├── Untitled-1.html         # Local webpage for displaying memes
├── module_Mood.py          # Defines dictionaries of mood-related keywords
├── module_img.py           # Module to display images
├── module_music.py         # Module for playing specific audio tracks
├── music_3.py              # A GUI-based music player using Tkinter and Pygame
└── project_meme.py         # The main entry point of the application
```

## 📈 Areas for Improvement

This project is a great proof-of-concept with several opportunities for enhancement:

-   **Fix Hardcoded Paths**: The most critical improvement is to replace all absolute file paths with relative paths to make the project portable.
-   **Use Environment Variables**: Database credentials should be stored in environment variables or a `.env` file instead of being hardcoded.
-   **Refactor Repetitive Code**: The functions in `module_music.py` and the logic in `project_meme.py` have a lot of repetition and can be simplified into more generic, reusable functions.
-   **Improve Meme Logic**: The HTML file currently shows the same set of memes for all categories. This can be updated to display category-specific images.
-   **Web Framework Integration**: A lightweight web framework like **Flask** or **FastAPI** could be used to serve the meme viewer, which would solve pathing issues and provide more flexibility.
-   **Create a `.gitignore` File**: A `.gitignore` file should be added to the repository to exclude `__pycache__` directories and other non-essential files.

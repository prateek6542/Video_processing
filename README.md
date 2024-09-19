# Fatmug Video Processing Project

## Overview

This project is a Django-based web application for uploading videos, processing them to extract subtitles, and providing search functionality for those subtitles. The project also includes video playback with subtitles and is containerized using Docker.

## Project Setup

### Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### Install Dependencies

pip install -r requirements.txt

### Migrate Database

python manage.py migrate

### Run the development server

python manage.py runserver

### Docker Setup (Optional)
If you prefer to use Docker, follow these steps:

### Build the Docker Image

docker build -t fatmug_project .

### Run Docker Compose

docker-compose up

## Usage
1. Upload a Video: Navigate to /upload/ to upload a video file.
2. Process Video: After uploading, the video will be processed in the background. Subtitles will be extracted and stored.
3. Search Subtitles: Use the search functionality to find specific phrases within the video subtitles. The search form can be accessed from the video list page.
4. View Videos: Visit /videos/ to view and play the list of uploaded videos with their subtitles.

## Troubleshooting
1. File Not Found (404) Errors: Ensure that media files are correctly saved in the media/videos/ directory and that the MEDIA_URL and MEDIA_ROOT settings in settings.py are correctly configured.
2. Subtitle Extraction Issues: Make sure ffmpeg is properly installed and configured. Check if subtitles are extracted and stored correctly in the database.

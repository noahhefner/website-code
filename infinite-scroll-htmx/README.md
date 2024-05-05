# Infinite Scroll with HTMX

This directory contains example code for my article *Infinite Scroll with HTMX, Python, and MongoDB*. 

## Setup Instructions

### Install Tooling

Installation instructions will differ depending on your operating system, but you should have the following installed and available:

- Python + pip
- MongoDB
- Optional: MongoDB Compass for browsing the database

*Note: Make sure that the MongoDB process is running on your system before proceeding. How you do this will depend on your operating system. I am on Ubuntu and I have MongoDB installed through the official apt repository, so my command is `sudo systemctl start mongod`.*

### Clone the Repo

Clone this repository and `cd` into this directory:

```
git clone https://github.com/noahhefner/website-code.git
cd website-code/infinite-scroll-htmx
```

### Install Python Packages

Install Python dependencies: `pip install -r requirements.txt`

### Populate MongoDB Database

Run the `build_database.py` Python script to populate the database with dummy data. **Make sure the MongoDB process is running before you execute this script.** If you have MongoDB Compass installed, you should see something that looks like this:

![compass](/infinite-scroll-htmx/compass.png)

*Note: If you don't see the collection immediately appear, you may have to click the refresh icon in the left sidebar.*

### Start Web Server

Start Uvicorn server: `uvicorn app.main:app --reload`

![demo](/infinite-scroll-htmx/demo.gif)
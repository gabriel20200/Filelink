# Filelink - A homebrew file cloud storage.

Filelink is a simple web application that allows you to host a personal cloud file storage server from the comfort of your own home! Tired of having to email yourself that photo you want on your computer? Well with Filelink, now you'll be able to transfer files from your phone and onto your computer (or the other way around) within seconds! 

<br>

<h3 align="center">Folders Preview</h3>
<p align="center">
  <img src="https://user-images.githubusercontent.com/79603829/143728783-a017fd9c-fc0c-453e-8beb-bc4af0bd1616.PNG"/>
</p>

<br>
<br>

<h3 align="center">Folder Files Preview</h3>
<p align="center">
  <img src="https://user-images.githubusercontent.com/79603829/143728795-e3eaf9ef-dad9-4a24-b7a2-6bd296e4b340.PNG"/>
</p>

<br>

## Getting Started

1) Make sure you have ``Python 3.9`` and ``pip3`` installed on your system.
2) Clone the GitHub repository onto your system.
3) Change directory into the cloned repository's folder, and run ``pip3 install -r requirements.txt`` in the command terminal.
4) Once all the required liberaries are downloaded, run ``flask run`` into the command terminal.
5) Make sure to run ``flask run -h 0.0.0.0 -p 80`` into the command terminal if you're gonna be hosting the server on a VPS

## Features

- Folders for files
- Folder deletion (deletes all the files within the folder upon deletion)
- File deletion
- File icons
- Nice and simple UI

## Programming Languages

- Filelink's database was written in Sqlite via the SQLAlchemy liberary
- Filelink's back-end was written in Python Flask (Python 3.9.2)
- Filelink's front-end was written in HTML & CSS
- Filelink's private constants are stored in a JSON file 

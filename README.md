# WebViz: Web Visualization using Django and Plotly
This is a simple Django app for web visualization which allows users to upload csv file and visualize the data. 

### Package Structure Overview:
    django-webviz
        data
        docs
        webviz/  (project name)
            __init__.py
            webviz/
                __init__.py
                asgi.py
                settings.py
                urls.py
                wsgi.py
            viz/     (app name)
                migrations
                static/
                    app.css  (css styling files)
                templates/
                    (all html templates)
                __init__.py
                admin.py
                apps.py
                forms.py
                models.py
                tests.py
                views.py               
            static
            media
            db.sqlite3
            manage.py
        LICENSE.txt
        README.md
        requirements.txt    

## Installation and Deployment

### Environment setup using Anaconda
- Anaconda installation and setup :
    - [Anaconda](https://docs.anaconda.com/anaconda/navigator/install/) ([Windows](https://docs.anaconda.com/anaconda/install/windows/)/[Linux](https://docs.anaconda.com/anaconda/install/linux/)/[MacOS](https://docs.anaconda.com/anaconda/install/mac-os/))
    - [Miniconda](https://docs.conda.io/en/latest/miniconda.html) ([Windows](https://docs.conda.io/en/latest/miniconda.html#windows-installers)/[Linux](https://docs.conda.io/en/latest/miniconda.html#linux-installers)/[MacOS](https://docs.conda.io/en/latest/miniconda.html#macosx-installers))
- Programming language: Python (version 3.7)
- Using the terminal or an Anaconda Prompt, create a new environment – **$ conda create –n webviz python=3.7**
- Activate new environment - **$ conda activate webviz**
- Clone this repository from Github:
    – open terminal and select a project path - **$ cd PATH**
    - To clone type - **$ git clone https://github.com/JagritiG/django-webviz.git**
- Install requirements.txt  using pip - **$ pip install –r requirements.txt**

        
### Deployment
- Navigate to project webviz  (project name)
- Run command ls to check the right path: 
[__init__.py  db.sqlite3  manage.py  media  static  viz  webviz]
- Run following command to run the server:
    **$ python3 manage.py runserver** 
    
- Open localhost **localhost:8000** to see the pages
- Go to **Upload File**, **localhost:8000/upload/** and upload a csv file and plot the figure
- To navigate to **admin** open **localhost:8000/admin/** 
(admin name: admin and password: webviz123)



# Books project  - Installation guide
## 1.	Tools/ Libraries
-   Python V 3.8.2
-   Flask==2.2.2
-   Flask-MySQLdb==1.0.1
-   mysqlclient==2.1.1


## 2.	Installation

-   To clone the repository from https://github.com/jorgeeliecerpalacios/project_books.git
-   To create a virtual enviroment
``` python -m venv .venv ```
-   To activate the virtual enviroment (WINDOWS)
``` source .venv/scripts/activate ```
    To install the dependencies
``` pip install -r requirements.txt ```


## 3. Database mysql
-   To install the database, you need to run the query script that has the database structure and some populated data, located at:


``` ./query_books_project.sql ```

- you need to change your own mysql credentials in app.py lines from 7 to 11

## 4. run the project
-   To run the project
``` python app.py ```


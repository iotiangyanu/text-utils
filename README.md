# Text Utils 📝

Text Utils is a Django-based web application designed to perform basic text analysis and transformation operations through a clean and responsive user interface. This project is built for learning and demonstrates core Django concepts along with frontend integration using Bootstrap.

---

## ✨ Features

- Convert user-entered text into **UPPERCASE**
- Count the total number of characters in the input text
- Simple and intuitive user interface
- Responsive design using Bootstrap
- Separate result pages for each operation
- Easy to extend with additional text-processing features

---

## 🧰 Technology Stack

- **Programming Language:** Python  
- **Framework:** Django  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite (default Django database)

---

## 📁 Project Structure

text-utils/
│── manage.py

│
├── textutils/

│ ├── init.py

│ ├── settings.py

│ ├── urls.py

│ ├── views.py

│ ├── asgi.py

│ └── wsgi.py

│

├── templates/

│ ├── index.html

│ ├── about.html

│ ├── uppercase.html

│ └── countchar.html

│
├── .gitignore

└── README.md

---

## ⚙️ How to Run the Project Locally

1. Clone the repository
   ```bash
   git clone https://github.com/iotiangyanu/text-utils.git

   cd text-utils
   
   python -m venv venv
   venv\Scripts\activate
   
   pip install django
   
   python manage.py runserver
   
   http://127.0.0.1:8000/
bash```

🌐 Application Routes
/ or /index → Home page for text input

/uppercase → Displays the uppercase converted text

/countchar → Displays the total character count

/about → About page of the application

🚀 Future Enhancements
Word count and sentence count

Remove extra spaces from text

Text formatting utilities

Download processed text

Cloud deployment for live access

👨‍💻 Author
Gyanesh Dwivedi
An engineering student learning Django and web development.

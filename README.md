# Finance Tracker

Finance Tracker is a simple web-based application designed to help users manage their income, expenses, and overall financial health efficiently.

## Features
- Add and categorize expenses and income
- Track financial trends with visual charts
- User authentication for secure access
- Generate financial reports

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3
- Django
- Git

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/finance_tracker.git
   cd finance_tracker
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Open `http://127.0.0.1:8000/` in your browser.
- Register/Login to start tracking your finances.

## Contributing
If you want to contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m "Added new feature"`
4. Push to your branch: `git push origin feature-name`
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

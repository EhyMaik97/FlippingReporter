# FlippingReporter

**FlippingReporter** is a Django application for managing the buying and selling of items, recording purchases and sales, and providing detailed profit statistics.

## Features

- Record purchases with details like name, category, purchase channel, date, price, and notes.
- Record sales with details like purchase reference, sale date, sale channel, fees, shipping costs, and sale price.
- Calculate and display profit for each sale.
- Mark purchases as sold once they are included in a sale.
- Display statistics and visualizations for purchases and sales.
- Admin interface with enhanced views and actions.

## Installation
### Clone the repository:

    git clone https://github.com/EhyMaik97/flippingmanager.git
    cd flippingmanager


### Create and activate a virtual environment:

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`


### Install dependencies:

    pip install -r requirements.txt


### Set up the database:

    python manage.py migrate


### Create a superuser:

    python manage.py createsuperuser

### Run the development server:

    python manage.py runserver

### Access the admin interface:

Open a web browser and go to http://127.0.0.1:8000/admin/, then log in with the superuser credentials.

## Usage
### Admin Interface

- Manage Purchases: Add, edit, and delete purchase records. Each purchase includes name, category, channel, date, price, and notes.
- Manage Sales: Add, edit, and delete sales records. Each sale links to a purchase and includes sale date, channel, fees, shipping costs, and sale price.
- Track Profit: Automatically calculate profit for each sale.
Mark Purchases as Sold: Once a purchase is included in a sale, it is marked as sold.

### View Statistics

Access the statistics page to view various analytics, such as:
- Percentage distribution of purchase channels and categories.
- Percentage distribution of sale channels.
- Total purchase costs, sale revenues, and profits.

### Code Structure

- models.py: Defines the data models for Channel, Category, Purchase, and Sale.
- admin.py: Customizes the admin interface for better data management.
- management/commands/import_data.py: Implements the import command for reading data from Excel files.
- templates/: Contains HTML templates for the admin interface and statistics page.
- views.py: Implements the views for rendering statistics.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Implement your changes.
4. Commit and push your changes to the branch.
5. Create a pull request.

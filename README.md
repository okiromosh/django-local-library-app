# django-local-library-app
A library app built with python using the Django Framework

This is a simple Django web application for managing books and authors. It allows you to view a list of books and authors, see book details, and perform various actions such as borrowing books and renewing book loans.

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone <repository_url>
```

2. Install the required dependencies. It is recommended to use a virtual environment for this:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
pip install -r requirements.txt
```

3. Run the Django development server:

```bash
python manage.py runserver
```

4. Open your web browser and go to `http://localhost:8000/` to access the application.

## Features

### Home Page
- Provides an overview of the library, including the total number of books, book instances, available book instances, and authors.
- Keeps track of the number of visits using session data.

### Book Listing
- Displays a paginated list of all books in the library.
- You can navigate through pages using the pagination controls.

### Book Detail
- Shows detailed information about a specific book, including its title, author, summary, and more.

### Author Listing
- Lists all authors in the library with pagination support.
- You can click on an author to view their details.

### Author Detail
- Displays information about a specific author, including their name, date of birth, and a list of books they have written.

### User Actions (Login Required)
- **Borrowed Books:** Lists books borrowed by the logged-in user, including due dates. Allows pagination.
- **Renew Book:** Allows librarians to renew the due date for a borrowed book.
- **Create Author:** Allows librarians to add new authors to the library.
- **Update Author:** Allows librarians to edit author information.
- **Delete Author:** Allows librarians to delete authors from the library.
- **Create Book:** Allows librarians to add new books to the library.
- **Update Book:** Allows librarians to edit book information.
- **Delete Book:** Allows librarians to delete books from the library.

## Contributing

If you'd like to contribute to this Django app, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch from the `main` branch for your changes.
3. Make your changes and ensure they are well-documented and tested.
4. Push your changes to your forked repository.
5. Create a pull request to the original repository's `main` branch.

## License

This Django app is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

This app was created as a learning project and is based on the Django framework. Special thanks to the Django community for their excellent documentation and resources.

Feel free to explore and enhance this Django app according to your needs. Enjoy managing your library!

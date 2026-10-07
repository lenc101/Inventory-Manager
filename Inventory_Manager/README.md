# Inventory Manager

A command-line inventory management application built with Python.

The program allows users to manage products, update stock quantities, search for products, delete products, and calculate the total value of the inventory.

## Features

- Add new products
- View all products in the inventory
- Search for products by name
- Update product stock quantities
- Delete products
- Calculate total inventory value
- Input validation for prices and quantities
- Handles invalid numeric input
- Handles products that cannot be found
- Prevents empty product names
- Interactive command-line menu

## Technologies

- Python 3
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- `try` / `except`
- Boolean flags
- User input handling

## How It Works

The inventory is stored in a list of dictionaries.

Example:

    products = [
        {
            "name": "Keyboard",
            "price": 1200,
            "quantity": 5
        }
    ]

Each product contains:

- `name` — product name
- `price` — product price
- `quantity` — amount currently in stock

The program provides a menu where the user can choose which inventory operation to perform.

## Menu

    1. Add product
    2. View inventory
    3. Search product
    4. Update stock
    5. Delete product
    6. Calculate inventory value
    7. Exit

## Input Validation

The application validates user input to prevent invalid data.

For example:

- Product names cannot be empty.
- Prices must be greater than 0.
- Quantities cannot be negative.
- Non-numeric values are rejected when numbers are required.
- Searching, updating, or deleting a product that does not exist returns an error message.

## Example

    1. Add product
    2. View inventory
    3. Search product
    4. Update stock
    5. Delete product
    6. Calculate inventory value
    7. Exit

    Enter an option: 6

    Total inventory value: 16100

## Project Structure

    inventory-manager/
    │
    ├── main.py
    └── README.md

## What I Practiced

This project helped me practice:

- Working with lists of dictionaries
- Creating and using functions
- Iterating through data with `for` loops
- Updating dictionary values
- Adding and removing items from lists
- Searching through structured data
- Using boolean flags to track search results
- Handling invalid user input with `try` / `except`
- Basic data validation
- Building a multi-option CLI application

## Future Improvements

Possible improvements for a future version:

- Save inventory data to a file
- Load inventory data when the program starts
- Add product categories
- Prevent duplicate products
- Improve terminal formatting
- Add sorting and filtering
- Replace in-memory storage with SQLite

## Author

Built as part of my Python learning journey, focusing on practical programming, automation, and building projects that can later be used as a foundation for freelance work.
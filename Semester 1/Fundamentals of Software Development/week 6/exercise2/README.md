# Shop Management System

This project implements a simple shop management system that allows tracking product inventory and cash register operations.

## Class Structure and Interactions

The system consists of three main classes:

### 1. Product Class
- **Purpose**: Manages information about a single product
- **Properties**:
  - `type`: The name of the product (e.g., "Cap")
  - `price`: The unit price of the product
  - `stock`: The quantity available
- **Key Methods**:
  - `has(stock)`: Checks if there's enough stock available
  - `sold(stock)`: Decreases stock and calculates revenue
  - `stocked(stock)`: Increases stock and calculates cost
  - `cash(stock)`: Calculates the monetary value of a quantity

### 2. CashRegister Class
- **Purpose**: Tracks the shop's available cash
- **Properties**:
  - `cash`: The current cash amount
- **Key Methods**:
  - `gain(amount)`: Adds money when selling products
  - `pay(amount)`: Removes money when purchasing stock
  - `has(amount)`: Checks if there's enough cash available

### 3. Shop Class
- **Purpose**: Coordinates the entire system
- **Properties**:
  - `product`: A Product instance
  - `register`: A CashRegister instance
- **Key Methods**:
  - `sell()`: Handles the sale of products
  - `restock()`: Handles purchasing new inventory
  - `view()`: Displays product and cash status
  - `menu()`: Main interactive loop for the program

## Workflow Diagram

```
+----------------+          +----------------+
|      Shop      | contains |    Product     |
|----------------|--------->|----------------|
| product        |          | type           |
| register       |          | price          |
| sell()         |          | stock          |
| restock()      |          | sold()         |
| view()         |          | stocked()      |
| menu()         |          | has()          |
+----------------+          +----------------+
       |
       | contains
       v
+----------------+
|  CashRegister  |
|----------------|
| cash           |
| gain()         |
| pay()          |
| has()          |
+----------------+
```

## Step-by-Step Execution Flow

1. **Program Start**:
   - The `main()` function creates a `Shop` instance
   - Shop initializes with a Product (Cap, $10, 7 units) and an empty CashRegister

2. **Menu Interaction**:
   - User is presented with options: Sell, Restock, View, or Exit
   - Each option triggers a different method in the Shop class

3. **Selling Process** (when user selects 's'):
   - User inputs quantity to sell
   - Program checks if enough stock exists using `product.has()`
   - If yes:
     - Cash register gains money via `register.gain()`
     - Product stock is reduced via `product.sold()`
     - User sees confirmation message
   - If no: "Not enough stock" message appears

4. **Restocking Process** (when user selects 'r'):
   - User inputs quantity to restock
   - Program checks if enough cash exists using `register.has()`
   - If yes:
     - Cash register pays money via `register.pay()`
     - Product stock is increased via `product.stocked()`
     - User sees confirmation message
   - If no: "Not enough funds" message appears

5. **Viewing Status** (when user selects 'v'):
   - Displays current product stock and price
   - Displays current cash register balance

## How to Use

1. Run the shop.py file:
   ```
   python shop.py
   ```

2. Follow the menu prompts:
   - `s` - Sell products
   - `r` - Restock products
   - `v` - View current status
   - `x` - Exit the program

3. For sell and restock operations, enter the quantity when prompted.

## Implementation Details

- The shop starts with a predefined product (Cap) and an empty cash register
- All monetary values are displayed with 2 decimal places
- When selling, the cash register gains money and stock decreases
- When restocking, the cash register pays money and stock increases
- Operations are only performed if there is enough stock (for selling) or cash (for restocking)

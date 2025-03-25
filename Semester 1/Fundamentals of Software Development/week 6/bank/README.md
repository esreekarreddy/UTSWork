# Simple Banking System

This is a simple banking system that simulates basic banking operations like deposits, withdrawals, and transfers between accounts.

## System Structure

The system consists of three main classes:

1. **Account**: Represents a bank account with functionality to deposit, withdraw, and transfer money
2. **Customer**: Represents a bank customer who has a savings account and a loan account
3. **Bank**: Main interface that handles user interaction

## How It Works

When you run `bank.py`, the system:
1. Creates a Customer named "John Smith"
2. Asks for initial balances for both Savings and Loan accounts
3. Provides a menu of options for banking operations

### Available Commands

- **d** - Deposit money to savings account
- **w** - Withdraw money from savings account
- **t** - Transfer money from savings to loan account (pay off loan)
- **s** - Show all account details
- **x** - Exit the system

## Key Concepts

- **Savings Account**: Holds the customer's money and should generally have a positive balance
- **Loan Account**: Represents money owed to the bank
  - When transferring money to the loan account, it's like paying off a loan
  - A positive balance in the loan account means you've overpaid your loan
  - A negative balance means you still owe money

## Debugging Tips

If you encounter issues:
1. Check that you're entering valid numeric values (not text or empty values)
2. Ensure you have sufficient funds when withdrawing or transferring
3. Use the 's' command to verify your account balances before and after operations

## Common Issues

- **Value Error**: Occurs when you enter text instead of numbers for amounts
- **Insufficient Funds**: Appears when you try to withdraw or transfer more than your savings balance

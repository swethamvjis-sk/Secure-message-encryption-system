# Secure Message Encryption System

A Python-based message encryption system that allows users to register with a PIN, log in, encrypt messages, decrypt messages using a secret key, and view stored encrypted messages.

## Features

* User registration with PIN confirmation
* PIN-based login
* Three login attempts
* Message encryption
* Message decryption using a secret key
* View stored encrypted messages
* Stores data using Python `pickle`
* Menu-based interface

## How It Works

1. The user registers by creating and confirming a PIN.
2. The registered PIN is stored in `Login.dat`.
3. The user logs in using their registered PIN.
4. After successful login, the user can:

   * Encrypt a message
   * Decrypt a message
   * View encrypted messages
   * Exit
5. During encryption, each character is shifted by 3 positions and the encrypted message is stored in `Encrypt.dat`.
6. A secret key is stored in `Secret.dat`.
7. During decryption, the secret key is verified before the encrypted message is converted back to the original message.

## Files Used

| File          | Purpose                   |
| ------------- | ------------------------- |
| `Login.dat`   | Stores registered PINs    |
| `Encrypt.dat` | Stores encrypted messages |
| `Secret.dat`  | Stores secret keys        |

## Encryption Method

The program uses a simple character-shifting technique:

* Each character is shifted **3 positions forward** during encryption.
* Each character is shifted **3 positions backward** during decryption.

## Technology Used

* Python
* `pickle` module

## Concepts Used

* Functions
* File handling
* `pickle`
* `if-elif-else`
* `for` and `while` loops
* User input
* String manipulation
* Exception handling
* Character encoding using `ord()` and `chr()`

## Purpose

This beginner-level project was created to practice Python functions, file handling, loops, conditional statements, exception handling, and basic message encryption concepts.

## Author

Swetha Sivakumar


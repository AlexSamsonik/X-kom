# X-kom
Get price for item in internet-shop www.x-kom.pl

**Polish recourse:** https://www.x-kom.pl/

How to use on LINUX/MAC:
1. Clone the repository;
2. Install Virtual Environment (venv):
    ```bash
    python -m venv venv
    ```
3. Activate venv:
    ```bash
    source venv/bin/activate
    ```
4. Install poetry
    ```bash
    pip install poetry
    ```
5. Install dependencies via poetry
    ```bash
    poetry install
    ```
6. Run main.py:
    ```bash
    python main.py -k x-kom-kod
    ```
'x-kom-kod' could be found in UI https://www.x-kom.pl/ for specified item.
For example `python main.py -k 735703`
![kod-x-kom](https://github.com/user-attachments/assets/c04daf93-404e-432a-b139-78eaf2ceb9c1)

Note: You can see only price after execute command `python main.py -k x-kom-kod`, but you can modify output message
because response contains all information about product.

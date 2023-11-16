# autojohn
This is an automation of John the Ripper to test different wordlists. The results are stored in two created files:
- possible_passwords: Stores the possible cracked passswords
- used_wordlists: Stores all the used wordlists
  
## Usage
It's necessary to change 3 global variables:
- **directory path**: Change it for your own directory path where you have stored the wordlists that you want to test.
- **hash_file**: Change it for the file that contains the hash that you want to crack.
- **selected_format**: Change it for the hash format.

### Execution
```bash
python3 script.py
```

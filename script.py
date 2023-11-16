import os
import subprocess

directory_path = "" # change for your directory path
hash_file = "" # change for your hash file
selected_format = "" # change for the hash format that you want to crack

possible_passwords = []
used = []
cracked = 0


# you need to have all the wordlists that you want to use in the same directory
def add_wodlists():
    wordlists = []

    files = os.listdir(directory_path)
        
    # Adds the files found on the path directory that have a txt extension
    wordlists = [file for file in files if file.endswith("txt")]
        
    return wordlists


def john(w):
    global cracked
    wordlist = w
    command = f"john {hash_file} --wordlist={wordlist} --format={selected_format}"
    command2 = f"john --show --format={selected_format} {hash_file}"

    crack = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
    result = subprocess.run(command2, shell=True, capture_output=True, text=True, check=True)
        
    if "password hash cracked" in result.stdout:
        first_line = result.stdout.strip().splitlines()[0]
        if first_line not in possible_passwords:
            possible_passwords.append(first_line)
            cracked = cracked + 1

    used.append(wordlist)


def main():
    wordlists = add_wodlists()

    for wordlist in wordlists:
        john(directory_path+wordlist)

    with open("positive_john", 'w') as pf:
        pf.write("\n".join(possible_passwords))
        print(f"Passwords cracked with john: {cracked}")
    
    with open("used_wordlists", 'w') as uw:
        uw.write("\n".join(used))

if __name__ == '__main__':
    main()
# Password-nostore
PNS is the idea of a password manager without storing the passwords themselves. The password is obtained by hashing a string consisting of a resource address, a user name and a universal password, that is, there are practically no differences from classic password managers in the execution. The difference is that there is no way to understand directly in the password manager whether the universal password is specified correctly, which can be both a disadvantage and an advantage. Also, the difference is that it's not scary to lose a file with passwords (because there is no such file, but there is something instead of them), it's enough to remember the address, login and universal password. since you have to have different passwords for each site, and there can be many logins, this program can store the address, login and additional hashing iterations (if you need to change the password without changing the universal password) in your home directory.

## How to use
Just run the program and specify everything you need

    > ./main.py
    Input target or url: github.com
    Input username: n2b4f
    Enter the number of additional iterations (default is 100000): 
    Input password (the input is not visible): 
    8238fdaae5b1c6800f0695ddd241a61e5d2234700dfa46fffaefbab0f3626ef2

The hash is the password we wanted to get. It can be used on the website. (the example is not real, don't try it)

### Additional functions

Number of additional iterations - by default, the password is hashed in 100000 iterations, you can enter 1 for 100001 iterations etc.

The number of additional iterations can be specified in the configuration file, which should be in ~/.config/password-nostore/config 

    use_default_iterations = y
    default_add_iterations = 10


Help also avaliable

    usage: main.py [-h] [-f FILE] [-s] [-c]

    options:
     -h, --help            show this help message and exit
     -f FILE, --file FILE  Load file with info
     -s, --save            Add to storage
     -c, --clipboard       Copy password to clipboard instead on std::out
     -l LENGTH, --length LENGTH
                        set lenght to hashed password



The program can store records, usage examples are below

    > ./main.py -f test/test1 -s
    Input target or url: test.test
    Input username: someone
    Enter the number of additional iterations (default is 100000): 2
    Input password (the input is not visible): 
    What from this data you want to save to file? 
     [1]target [2]username [3]additional iterations [4]all of them: 4
    bf7baa186193156b76a1b98450a6db08c62970d45619a74f32117310397532d4
    > cat test/test1 
    {"target": "test.test", "username": "someone", "additional_iterations": 2}

    > ./main.py -f test/test1 -s
    File already exist. Do you want to overwrite your file?: [y/N] y
    Input target or url: test.test
    Input username: someone
    Enter the number of additional iterations (default is 100000): 3
    Input password (the input is not visible): 
    What from this data you want to save to file? 
    [1]target [2]username [3]additional iterations [4]all of them: 1 2
    c4110e1d7f3a63d26c5d605ac7b5ac71d17547d395f25c746e0a7456edc55957
    > cat test/test1 
    {"target": "test.test", "username": "someone"}

    > ./main.py -f test/test1
    Enter the number of additional iterations (default is 100000): 3
    Input password (the input is not visible): 
    c4110e1d7f3a63d26c5d605ac7b5ac71d17547d395f25c746e0a7456edc55957

    > ./main.py -f test/test1 -c
    Input password (the input is not visible): 
    Our password copied to clipboard!

## Installation
Make sure that you installed python 3 and pip. Then run install.sh script.

    bash install.sh

or

    chmod u+x install.sh
    ./install.sh
Then make sure that $HOME/.local/bin is in our $PATH.

## After install user like that
    pns -f .password-nostore/myfolders/myfiles

For using clipboard you need to install xclip or xsel or wl-clipboard (for wayland) to your system.
You can do this like `sudo apt-get install xclip` or `sudo apt-get install xsel` or `sudo apt install wl-clipboard`




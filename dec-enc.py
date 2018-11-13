import subprocess
import termcolor
from subprocess import run
from subprocess import check_output
from termcolor import colored

print(colored("""

    ██████╗  ██████╗ ████████╗ ██╗██████╗
    ██╔══██╗██╔═══██╗╚══██╔══╝███║╚════██╗
    ██████╔╝██║   ██║   ██║   ╚██║ █████╔╝
    ██╔══██╗██║   ██║   ██║    ██║ ╚═══██╗
    ██║  ██║╚██████╔╝   ██║    ██║██████╔╝
    ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═╝╚═════╝

    """, "green"))

print(colored("""
Type e to encrypt or d to decrypt. Press CTRL-C to quit.

For info on rot13 type info.
""", "blue"))

enc_dec_opt = input(colored("> : ", "yellow"))

def INFO():
    print("""

                            #### DESCRIPTION ####


ROT13 (rotate by 13 places", sometimes hyphenated ROT-13) is a simple letter
substitution cipher that replaces a letter with the 13th letter after it, in the
alphabet. ROT13 is a special case of the Caesar cipher which was developed in
ancient Rome.

Because there are 26 letters (2×13) in the basic Latin alphabet, ROT13 is its
own inverse; that is, to undo ROT13, the same algorithm is applied, so the same
action can be used for encoding and decoding. The algorithm canonical example of
weak encryption.

ROT13 is used in online forums as a means of hiding spoilers, punchlines, puzzle
solutions, and offensive materials from the casual glance. ROT13 has inspired a
variety of letter and word games on-line, and is frequently mentioned in
newsgroup conversations.

Applying ROT13 to a piece of text merely requires examining its alphabetic
characters and replacing each one by the letter 13 places further along in the
alphabet, wrapping back to the beginning if necessary. A becomes N, B becomes O,
and so on up to M, which becomes Z, then the sequence continues at the beginning
of the alphabet: N becomes A, O becomes B, and so on to Z, which becomes M. Only
those letters which occur in the English alphabet are affected; numbers,
symbols, whitespace, and all other characters are left unchanged. Because there
are 26 letters in the English alphabet and 26 = 2 × 13, the ROT13 function is
its own inverse:

In other words, two successive applications of ROT13 restore the original text
(in mathematics, this is sometimes called an involution; in cryptography, a
reciprocal cipher).

The transformation can be done using a lookup table, such as the following:


    Input 	ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    Output      NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm


                               #### USAGE ####


ROT13 was in use in the net.jokes newsgroup by the early 1980s. It is used to
hide potentially offensive jokes, or to obscure an answer to a puzzle or other
spoiler. A shift of thirteen was chosen over other values, such as three as in
the original Caesar cipher, because thirteen is the value for which encoding and
decoding are equivalent, thereby allowing the convenience of a single command
for both. ROT13 is typically supported as a built-in feature to newsreading
software. Email addresses are also sometimes encoded with ROT13 to hide them
from less sophisticated spam bots. It is also used to circumvent email screening
and spam filtering. By obscuring an email's content, the screening algorithm is
unable to identify the email as, for instance, a security risk, and allows it
into the recipient's in-box.

ROT13 is an example of the encryption algorithm known as a Caesar cipher,
attributed to Julius Caesar in the 1st century BC.

In encrypted, normal, English-language text of any significant size, ROT13 is
recognizable from some letter/word patterns. The words "n", "V" (capitalized
only), and "gur" (ROT13 for "a", "I", and "the"), and words ending in "yl"
("ly") are examples.

ROT13 is not intended to be used where secrecy is of any concern—the use of a
constant shift means that the encryption effectively has no key, and decryption
requires no more knowledge than the fact that ROT13 is in use. Even without this
knowledge, the algorithm is easily broken through frequency analysis Because of
its utter unsuitability for real secrecy, ROT13 has become a catchphrase to
refer to any conspicuously weak encryption scheme; a critic might claim that
"56-bit DES is little better than ROT13 these days". Also, in a play on real
terms like "double DES", the terms "double ROT13", "ROT26", or "2ROT13" crop up
with humorous intent, including a spoof academic paper "On the 2ROT13 Encryption
Algorithm". As applying ROT13 to an already ROT13-encrypted text restores the
original plaintext, ROT26 is equivalent to no encryption at all. By extension,
triple-ROT13 (used in joking analogy with 3DES) is equivalent to regular ROT13.

In December 1999, it was found that Netscape Communicator used ROT13 as part of
an insecure scheme to store email passwords. In 2001, Russian programmer Dimitry
Sklyarov demonstrated that an eBook vendor, New Paradigm Research Group (NPRG),
used ROT13 to encrypt their documents; it has been speculated that NPRG may have
mistaken the ROT13 toy example—provided with the Adobe eBook software
development kit—for a serious encryption scheme. Windows XP uses ROT13 on some
of its registry keys. ROT13 is also used in the Unix fortune program to conceal
potentially offensive dicta."

""")

def CIPHER():
    print(colored("\nEnter path to file > :\n", "blue"))
    enc_input = input(colored("> : ", "yellow"))
    print(colored("\nencrypted text > :\n", "blue"))
    encrypt = f"cat {enc_input} | tr \'A-Za-z\' \'N-ZA-Mn-za-m\'"
    enc_f = f"cat {enc_input} | tr \'A-Za-z\' \'N-ZA-Mn-za-m\' > ~/encrypt.txt"
    run(encrypt, shell=True)
    run(enc_f, shell=True)
    print(colored("""
###########################################
enrypted data written to file ~/encrypt.txt
###########################################
exiting >>>................................
    """, "blue"))
    ## Debug
    #enc_out = subprocess.check_output(f"cat {enc_input} | tr \'A-Za-z\' \'N-ZA-Mn-za-m\'", shell=True)
    #print(colored(f"raw output for debugging > :\n\n{enc_out}\n", "red"))

def DECIPHER():
    print(colored("\nEnter path to rot13 encoded data > :\n", "blue"))
    dec_input = input(colored("> : ", "yellow"))
    print(colored("\ndecrypted text > :\n", "blue"))
    decrypt = f"cat {dec_input} | tr \'A-Za-z\' \'N-ZA-Mn-za-m\'"
    dec_f = f"cat {dec_input} | tr \'A-Za-z\' \'N-ZA-Mn-za-m\' > ~/decrypt.txt"
    run(decrypt, shell=True)
    run(dec_f, shell=True)
    print(colored("""
############################################
decrypted data written to file ~/decrypt.txt
############################################
exiting >>>.................................
    """, "blue"))
    ## Debug
    #dec_out = subprocess.check_output(f"cat {dec_input} | tr \'A-Za-z\' \'N-ZA-Mn-za-m\'", shell=True)
    #print(colored(f"raw output for debugging > :\n\n{dec_out}\n", "red"))

def ROT13():
    if enc_dec_opt == "e":
        CIPHER()
    elif enc_dec_opt == "d":
        DECIPHER()
    elif enc_dec_opt == "info":
            INFO()
            cmd = input(colored("Type c to continue or type CTRL-C to quit > : ", "blue"))
            if cmd == "c":
                print(colored("\nType e to encrypt or d to decrypt. Press CTRL-C to quit.", "blue"))
                enc_dec_opt2 = input(colored("\n> : ", "yellow"))
                if enc_dec_opt2 == "e":
                    CIPHER()
                elif enc_dec_opt2 == "d":
                    DECIPHER()

ROT13()

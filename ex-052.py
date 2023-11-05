def is_palindrome(word):
    return word == word[::-1]
def main():
    string = input('Digite uma frase: ').lower()
    words = string.split()

    palindromes = [word for word in words if is_palindrome(word)]

    if palindromes:
        print('Palavras palindromas encontradas na frase:')
        for word in palindromes:
            print(word)
    else:
        print('Nnenhuma palavra palindroma encontrada na frase.')
if __name__ == "__main__":
    main()

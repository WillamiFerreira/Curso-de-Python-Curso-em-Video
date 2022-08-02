#Crie um lista com palavras e mostre quais as vogais que estão em cada uma.
def main():
    palavras = ('Estudar', 'Aprender', 'Conquistar', 'Dominar')
    for palavra in palavras:
        print(f'\nNas palavra {palavra.upper()} temos ', end=' ') #a cada início de laço para palavra printamos essa mensagem com um \n para quebrar a linha e um end =' ', pois um print será feito a seguir e deve ser na mesma linha
        for letra in palavra: #criaremos uma repetição onde cada laço verificará uma letra da palavra, sendo ela par ou não
            if letra.upper() in 'AEIOU': #caso seja par...
                print(letra, end=' ') #a letra é imprimida com um end= ' ' para o caso de haver ortras vogais na palavra não ser quebrado linha.


if __name__ == "__main__":
    main()
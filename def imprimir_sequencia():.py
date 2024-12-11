def imprimir_sequencia():
    """Imprimeix la sèrie de números de l'1 al 15."""
    for i in range(1, 16):
        print(i, end=' ')
    print()  

def main():
    for _ in range(5):
        imprimir_sequencia()
if __name__ == "__main__":
    main()

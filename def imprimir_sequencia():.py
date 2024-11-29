def imprimir_sequencia():
    """Imprimeix la sèrie de números de l'1 al 15."""
    for i in range(1, 16):
        print(i, end=' ')
    print()  # Salta a la següent línia

def main():
    # Imprimir la sèrie cinc vegades
    for _ in range(5):
        imprimir_sequencia()

# Executar el programa
if __name__ == "__main__":
    main()
import requests

# Dicionário com algumas moedas mais usadas
moedas_nomes = {
    "BRL": "Real Brasileiro",
    "USD": "Dólar Americano",
    "EUR": "Euro",
    "JPY": "Iene Japonês",
    "GBP": "Libra Esterlina",
    "AUD": "Dólar Australiano",
    "CAD": "Dólar Canadense",
    "CHF": "Franco Suíço",
    "CNY": "Yuan Chinês",
    "ARS": "Peso Argentino",
    "MXN": "Peso Mexicano",
    "CLP": "Peso Chileno"
}

def obter_taxas():
    url = 'https://open.er-api.com/v6/latest/USD'
    response = requests.get(url)
    data = response.json()
    return data['rates']

def converter_moedas(valor, moeda_origem, moeda_destino, taxas):
    if moeda_origem in taxas and moeda_destino in taxas:
        taxa_origem = taxas[moeda_origem]
        taxa_destino = taxas[moeda_destino]
        valor_em_usd = valor / taxa_origem
        valor_convertido = valor_em_usd * taxa_destino
        return valor_convertido
    else:
        return None

def listar_moedas():
    print("\n=== Moedas Disponíveis ===\n")
    for i, (moeda, nome) in enumerate(moedas_nomes.items(), start=1):
        print(f"{moeda} - {nome}", end="   ")
        if i % 3 == 0:  # quebra de linha a cada 3 moedas
            print()
    print("\n" + "-" * 40)

# Programa principal
if __name__ == '__main__':
    taxas = obter_taxas()

    while True:
        print("\n=== Conversor de Moedas ===")
        print("1. Listar moedas disponíveis")
        print("2. Converter moedas")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_moedas()

        elif opcao == "2":
            valor = float(input("Qual o valor a ser convertido: "))
            moeda_origem = input("Qual é a moeda de origem (ex: USD, BRL): ").upper()
            moeda_destino = input("Qual é a moeda de destino (ex: EUR, JPY): ").upper()

            valor_convertido = converter_moedas(valor, moeda_origem, moeda_destino, taxas)

            if valor_convertido is not None and moeda_origem in moedas_nomes and moeda_destino in moedas_nomes:
                print(f"\n{valor:.2f} {moeda_origem} ({moedas_nomes[moeda_origem]}) "
                      f"= {valor_convertido:.2f} {moeda_destino} ({moedas_nomes[moeda_destino]})")
            else:
                print("Moeda inválida. Use a opção 1 para ver as moedas disponíveis.")

        elif opcao == "3":
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida, tente novamente.")

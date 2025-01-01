#SISTEMA CARGA ONIBUS ESPACIAL, NICOLAS OLIVEIRA
nomes_itens = []
pesos_itens = []
while True:
    print("\n=== Menu principal ===")
    print("1. Adicionar Item à carga")
    print("2. Remover item da carga")
    print("3. Listar itens da carga")
    print("4. Exibir informações de voo")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")
    s = sum(pesos_itens)
    c = 100 # consumo base
    d = 768800 # distancia terra lua
    if opcao == "1":
        while True:
            item = input("Digite o nome do item (ou 'Sair' para cancelar.): ").strip().title()
            if item == "Sair":
                break
            while True:
                try:
                    peso = float(input("Digite o peso do item (em kg): "))
                    if peso <= 0:
                        print("Erro: O peso deve ser maior que 0. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Erro: Insira um valor numérico válido.")
            nomes_itens.append(item)
            pesos_itens.append(peso)
            print("Item adicionado com sucesso!")
            break
    elif opcao == "2":
        if not nomes_itens:
            print("Não há itens na carga para remover.")
        else: 
            while True:
                remover = input("Digite o nome do item a ser removido (ou 'Sair' para cancelar.): ").title().strip()
                if remover == "Sair":
                    break
                if remover not in nomes_itens:
                    print("Item não encontrado. Tente novamente!")
                    continue
                indices = [i for i, nome in enumerate(nomes_itens) if nome == remover] #criar lista com indices dos duplicados
                if len(indices) > 1: # avisar usuario de nomes duplicados
                    print(f"Existem {len(indices)} itens chamados '{remover}':")
                    for i, idx in enumerate(indices, start=1): # mostrar itens duplicados
                        print(f"{i}. {nomes_itens[idx]} - {pesos_itens[idx]} kg")
                    escolha = int(input("Escolha o número do item a ser removido: ")) - 1 # -1 já que o indice começa em 0
                    ind = indices[escolha]
                else:
                    ind = nomes_itens.index(remover) # caso nao seja duplicado, apenas encontra o indice com index()
                pesos_itens.pop(ind)
                nomes_itens.pop(ind)
                print("Item removido com sucessso!")
                break
    elif opcao == "3":
        if not nomes_itens:
            print("Nenhum item na carga.")
        else:
            s = sum(pesos_itens)
            print("Itens a bordo:")
            for i, (nome, peso) in enumerate(zip(nomes_itens, pesos_itens), start=1): # utiliza zip, que cria um par do nome do item e seu peso entre as duas listas
                print(f"{i}. {nome} - {peso} kg")
            print(f"Peso total: {s} kg")
    elif opcao == "4":
        if not nomes_itens:
            print("Nenhum item na carga. Consumo base é 100 km/l.")
        else:
            c_ajustado = max(1,c - (s/100)) #consumo minimo 1km/l
            c_necessario = d/c_ajustado
            print(f"Peso total da carga: {s} kg")
            print(f"Consumo ajustado: {c_ajustado} km/l ({100 - c_ajustado} litro(s) abaixo do consumo base)")
            print(f"Distância para ida e volta à Lua: {d:,} km")
            print(f"Combustível necessário: {c_necessario:.2f} litros")
    elif opcao == "5":
        print("\nSaindo do sistema. Obrigado por usar o sistema de controle de carga do ônibus espacial!") 
        break
    else:
        print("Erro: Opção inválida. Tente novamente.")   

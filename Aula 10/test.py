def perguntar(texto):
    resposta = input(texto + " (sim/nao): ").strip().lower()
    while resposta not in ["sim", "nao"]:
        resposta = input("Por favor, responda 'sim' ou 'nao'. " + texto + " (sim/nao): ").strip().lower()
    return resposta == "sim"


def verificar_direito_heranca():
    print("Bem-vindo ao verificador de direito à herança.")

    if perguntar("Você é descendente direto do falecido (filho, filha, neto, neta)?"):
        if perguntar(
                "Você está respondendo por um descendente direto falecido (seu pai/mãe ou avô/avó era filho/filha do falecido)?"):
            print("Você tem direito à herança por representação como descendente.")
        else:
            if perguntar("O falecido deixou um cônjuge sobrevivente?"):
                print("Você tem direito à herança como descendente, em concorrência com o cônjuge sobrevivente.")
            else:
                print("Você tem direito à herança como descendente.")
        return

    if perguntar("Você é cônjuge do falecido?"):
        if perguntar("O falecido deixou descendentes?"):
            print("Você tem direito à herança em concorrência com os descendentes.")
        elif perguntar("O falecido deixou ascendentes?"):
            print("Você tem direito à herança em concorrência com os ascendentes.")
        else:
            print("Você tem direito à herança como cônjuge.")
        return

    if perguntar("Você é ascendente direto do falecido (pai, mãe, avô, avó)?"):
        if perguntar("O falecido deixou um cônjuge sobrevivente?"):
            print(
                "Você tem direito à herança como ascendente, em concorrência com o cônjuge sobrevivente, na ausência de descendentes.")
        else:
            print("Você tem direito à herança como ascendente, na ausência de descendentes.")
        return

    if perguntar("Você é irmão/irmã do falecido?"):
        if perguntar("Você está respondendo por um irmão/irmã falecido(a) (você é sobrinho/sobrinha do falecido)?"):
            print("Você tem direito à herança por representação como sobrinho/sobrinha.")
        else:
            print("Você tem direito à herança como irmão/irmã, na ausência de descendentes, ascendentes e cônjuge.")
        return

    if perguntar("Você é sobrinho/sobrinha do falecido?"):
        print(
            "Você tem direito à herança como sobrinho/sobrinha, na ausência de descendentes, ascendentes, cônjuge e irmãos.")
        return

    if perguntar("Você é tio/tia ou primo/prima do falecido?"):
        if perguntar("Você está respondendo por um tio/tia falecido(a) (você é primo/prima do falecido)?"):
            print("Você tem direito à herança por representação como primo/prima.")
        else:
            print(
                "Você tem direito à herança como tio/tia ou primo/prima, na ausência de descendentes, ascendentes, cônjuge, irmãos e sobrinhos.")
        return

    print("Você não tem direito à herança conforme a legislação brasileira.")


# Executa o programa interativo
verificar_direito_heranca()

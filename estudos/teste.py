def limpar_cpf(cpf_sujo):
    if cpf_sujo is None or cpf_sujo == "" :
        return None      
    cpf_limpo = cpf_sujo.strip().replace(".", "").replace("-", "")
    if len(cpf_limpo) != 11:
            return None
    return (cpf_limpo)


resultado = limpar_cpf(" 123.456.789-09 ")

if resultado is None:
    print("CPF Inválido")
else:
    print(f"CPF Limpo: {resultado}")

resultado_ruim = limpar_cpf(None)

if resultado_ruim is None:
    print("CPF Inválido")
else:
    print(f"CPF Limpo: {resultado_ruim}")

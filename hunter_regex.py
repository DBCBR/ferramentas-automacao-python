import re
import time
from robo_investigador_cnpj import consultar_cnpj

texto_sujo = """
RESULTADO DA LICITAÇÃO:
1. Vencedora do Lote1: MAGAZINE LUIZA S/A (CNPJ: 47.960.950/0001-21) valor R$ 500,00.
2. Para o Lote 2, a empresa AMAZON SERVICOS (01.543.694/0001-83) foi desclassificada.
3. Contrato firmado com DAVID BARCELLOS CARDOSO TI - 57.929.932/0001-30.
"""

print("--- TEXTO ORIGINAL ---")
print(texto_sujo)
print("-" * 30)

# O PADRÃO (A 'Mira' do Sniper)
# \d = dígito (número)
# {2} = quantidade exata
# \. = ponto literal
# O padrão de CNPJ é: XX.XXX.XXX/XXXX-XX
padrao_cnpj = r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}"

# 1. Encontrar TODAS as ocorrências desse padrão no texto
# O comando é re.findall(padrao, texto)
lista_cnpjs = re.findall(padrao_cnpj, texto_sujo)

print(f"Encontrei {len(lista_cnpjs)} CNPJs no texto!")

# 2. Processar cada um
for cnpj_encontrado in lista_cnpjs:
    print(f"\nCapturado: {cnpj_encontrado}")

    # HIGIENE: Limpar para usar na API
    cnpj_limpo = cnpj_encontrado.replace(
        ".", "").replace("/", "").replace("-", "")
    print(f"Pronto para API: {cnpj_limpo}")

    consultar_cnpj(cnpj_limpo)

    print("Aguardando 3 segundos para não bloquear a API...")
    time.sleep(3)

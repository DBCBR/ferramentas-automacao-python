class ValidadorCPF:
    def __init__(self, documento_bruto):
        self.documento = documento_bruto

    def limpar(self):
        if self.documento is None or self.documento == "": return None
        limpo = str(self.documento).strip().replace(".", "").replace("-", "")
        if len(limpo) != 11: return None
        return limpo

    def formatar(self):
        self.limpar()
        if self.documento is None or len(self.documento) != 11:
            return None
        return f"{self.documento[:3]}.{self.documento[3:6]}.{self.documento[6:9]}-{self.documento[9:]}"


class ValidadorCNPJ:
    def __init__(self, documento_bruto):
        self.documento = documento_bruto
        
    def limpar(self):
        if self.documento is None or self.documento == "": return None
        limpo = str(self.documento).strip().replace(".", "").replace("/", "").replace("-", "")
        if len(limpo) != 14: return None
        return limpo
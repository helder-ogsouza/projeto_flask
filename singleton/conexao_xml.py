import xml.etree.ElementTree as ET

class ConexaoXML:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._carregar_xml()
        return cls._instancia

    def _carregar_xml(self):
        self.tree = ET.parse('dados/banco.xml')
        self.root = self.tree.getroot()

    def get_xml(self):
        return self.root

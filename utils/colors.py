from simple_colors import *
        
class InformationMessages:
    def succesMessage(self, string: str):
        print(green(f"[~] {string}"))
    
    def errorMessage(self, string: str):
        print(red(f"[!] {string}"))

    def information(self, string: str):
        print(yellow(f"[#] {string}"))

    def otherMessage(self, string: str):
        print(blue(f"[:] {string}"))

class HeadersMessages:
    def title(self, string: str):
        print(magenta(f"[+] {string}"))
        
    def subTittle(self, string: str):
        print(cyan(f"[-] {string}"))
        
    def option(self, string: str):
        print(f"      {string}")
    
    def text(self, string: str):
        print(black(f"      {string}"))
        
    def inputMode(self, string: str):
        return blue(f"[:] {string}")
    
class DefaultMessages:
    def errorSelection(self):
        print(red("[!] Selección errónea! Inténtelo de nuevo"))
        
    def errorValue(self):
        print(red("[!] Valor inválido! Por favor inténtelo de nuevo"))
class Edades :
    def calcular_edalber(edjuan):
        # En Python, la division con / siempre devuelve un decimal (float)
        return (2 * edjuan) / 3
    def calcular_edana(edjuan):
        return (4 * edjuan) / 3
    def calcular_edmama (edjuan, edalber, edana):
        return edjuan + edalber + edana
    
edjuan = 9
edalber = Edades.calcular_edalber(edjuan)
edana = Edades.calcular_edana(edjuan)
edmama = Edades.calcular_edmama(edjuan, edalber, edana)

# Resultado formateado

print ( f"Las edades son: Alberto = {edalber:.2f}, Juan = {edjuan:.2f}, Ana = {edana:.2f}, Mamá = {edmama:.2f}")

    

    
 
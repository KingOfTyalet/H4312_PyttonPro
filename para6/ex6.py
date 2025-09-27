class MathError(Exception):
    def __str__(self):
        return f""


def check(namber_1,nomber_2):
    if now_material >= min_material:
        print("Enough!")
    else:
        raise MathError

material_user = float(input("Enter material: "))
check_material(material_user, 300)
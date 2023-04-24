contraseña = "contraseña" # Cambia "contraseña" por la contraseña que desees

entrada_contraseña = input("Ingrese la contraseña: ")

if entrada_contraseña.lower() == contraseña.lower():
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")
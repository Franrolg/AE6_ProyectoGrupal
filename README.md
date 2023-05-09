# Módulo 6 - Django Grupal 5

## Instalar el aplicativo

1. git clone https://github.com/Franrolg/AE5_ProyectoGrupal.git
2. python -m venv .env
3. source .env/Scripts/activate
4. pip install -r requirements.txt
5. python manage.py runserver

## Usuario sin registrar

- Solo podrá ver la página de login y al registro de usuarios.
- Las secciones de usuarios (listado) y proveedores, no podrán ser accesibles mientrar no esté logueado.


## Usuario registrado

- Podrá iniciar sesión y así consultar el listado de usuarios, como también registrar proveedores en la BD.

# Administrador
- Todos los permisos.
- Puede ver, crear, eliminar y editar usuarios admin
- Puede ver, crear, eliminar y editar usuarios staff
- Puede ver, crear, eliminar y editar usuarios normales
- Puede ver, crear, eliminar y editar proveedores

# Staff
- Tienen acceso al administrador de django
- Puede ver usuarios admin
- Puede ver usuarios staff
- Puede ver y editar usuarios normales
- Puede ver, crear y editar proveedores

# Usuario normal
- Puede visualizar los datos solamente.
- Se le denegará el acceso al registro de usuarios y proveedores cuando está logeado.

# Usuario no registrado
- No puede visualizar nada.
- Solo se puede registrar como usuario normal.
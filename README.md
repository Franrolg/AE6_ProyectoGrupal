# Módulo 6 - Django Grupal 6

## Instalar el aplicativo

1. git clone https://github.com/Franrolg/AE6_ProyectoGrupal.git
2. python -m venv .env
3. source .env/Scripts/activate
4. pip install -r requirements.txt
5. python manage.py runserver

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
- Puede ver usuarios normales
- Puede ver, crear y editar proveedores

# Usuario normal
- Puede visualizar los datos solamente.
- Se le denegará el acceso al registro de usuarios y proveedores cuando está logeado.

# Usuario no registrado
- Solo podrá ver la página de login y al registro de usuarios.
- Solo se puede registrar como usuario normal.
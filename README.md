Configurações ASGI e WSGI: Esses arquivos permitem que o aplicativo Django se comunique com o servidor web. Eles especificam o módulo de configurações para o aplicativo Django.

Configurações: Este arquivo contém configurações para o projeto Django. Inclui a chave secreta, modo de depuração, aplicativos instalados, middleware, configurações de banco de dados, validadores de senha e muito mais.

URLs: Este arquivo define os padrões de URL para o aplicativo. Inclui caminhos para registro de usuário, login e redefinição de senha.

Views: Este arquivo contém a lógica para lidar com solicitações e respostas. Inclui views para registro de usuário, login e redefinição de senha.

Templates: Os templates para as páginas de login e redefinição de senha foram compartilhados. Eles estendem um template base e incluem folhas de estilo específicas e conteúdo para cada página.

Models e Admin: Embora não tenham sido compartilhados, eles são uma parte essencial de qualquer aplicativo Django. Eles são usados para definir a estrutura de dados e a interface de administração.

Arquivo de Gerenciamento: Este é o utilitário de linha de comando do Django para tarefas administrativas. Ele define o módulo de configurações e executa o comando fornecido.


INSTALAÇÃO E CONFIGURAÇAO

PARA FAZER A INSTALAÇÃO COLOQUE ISSO NO TERMINAL

-python -m venv venv
-venv/Scripts/activate
-pip install requirements.txt
-pip install asgiref==3.7.2
-pip install Django==5.0
-pip install Pillow==10.1.0
-pip install sqlparse==0.4.4
-pip install tzdata==2023.3
-pip freeze > requirements.txt
-python manage.py makemigrations
-python manage.py migrate
-python manage.py createsuperuser - define o admin
-python manage.py runserver - roda o site

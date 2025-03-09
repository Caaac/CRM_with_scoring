import os
from django.db import connection
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def db_control(request, mode, module):
    if (module not in ['main', 'crm']):
        return HttpResponse(f"Module '{module}' does not exist", 500)

    db_type = 'mysql'
    path_tmpl = f'{module}/{mode}/db/sql/{db_type}/'
    sql_file_path = os.path.join(
        os.getcwdb().decode('utf-8'), path_tmpl, f'{mode}.sql')

    if os.path.isfile(sql_file_path):
        with open(sql_file_path, 'r') as file:
            sql_script = file.read()
            sql_script = sql_script.replace('\n', ' ')
            sql_script = [script.lstrip().rstrip().replace(
                '     ', '') + ';' for script in sql_script.split('; ') if script.replace(' ', '')]
        with connection.cursor() as cursor:
            try:
                for script in sql_script:
                    cursor.execute(script)
            except Exception as e:
                return HttpResponse(e, 400)
        return HttpResponse("SQL file executed successfully", 200)
    else:
        return HttpResponse(f"File '{sql_file_path}' does not exist", 500)


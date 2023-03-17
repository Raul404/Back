import csv
from datetime import datetime as dt

from .data_base_access import get_db_connection


def write_to_db(file_content: str):
    try:
        conn, cursor = get_db_connection()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados (
                cpf character varying(20) NOT NULL,
                cnpj character varying(20) NOT NULL,
                data date NOT NULL
            );
        ''')

        query = 'INSERT INTO dados(cpf, cnpj, data) VALUES '

        query_values = []
        values = []

        lines = csv.reader(file_content.splitlines())
        headers = next(lines)

        cpf_idx = headers.index('cpf')
        cnpj_idx = headers.index('cnpj')
        date_idx = headers.index('data')

        cpf_replacements = str.maketrans('-.', '')
        cnpj_replacements = str.maketrans('-./', '')
        date_format = '%d/%m/%Y'

        for line in lines:
            cpf, cnpj, date_str = [line[i] for i in [cpf_idx, cnpj_idx, date_idx]]
            cpf = cpf.translate(cpf_replacements)
            cnpj = cnpj.translate(cnpj_replacements)
            date = dt.strptime(date_str, date_format).date().isoformat()
            query_values.append('(%s, %s, %s)')
            values += [cpf, cnpj, date]

        query += ', '.join(query_values)

        cursor.execute(query, values)

        conn.commit()
    except Exception as e:
        print("ERROR ao escrever db ", str(e))
        return False
    finally:
        cursor.close()
        conn.close()

    return True

if __name__ == '__main__':
    start = time.time()
    read_csv('catalog.csv')
def save_salary_data2(salary_data):
    db_session.bulk_insert_mappings(Salary, salary_data)
    db_session.commit()
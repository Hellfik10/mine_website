from requests import get, post

print(get('http://127.0.0.1:8080/api/jobs').json())
print(get('http://127.0.0.1:8080/api/jobs/1').json())
print(get('http://127.0.0.1:8080/api/jobs/4').json())
print(get('http://127.0.0.1:8080/api/jobs/abs').json())
print(post('http://127.0.0.1:8080/api/jobs',
           json={'team_leader': 1,
                 'job': 'Текст новости',
                 'work_size': 10,
                 'collaborators': '12334, 2',
                 'is_finished': False}).json())
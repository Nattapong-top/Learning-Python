'''
ฝึกเขียนโปรแกรมโดยใช้ if-else ร่วมกับการวนลูป for กับดิกชันนารี (dictionary) แบบง่าย ๆ

'''

user_configs = {
        'tom.cat': {'status': 'active', 'role': 'admin', 'last_login': 5},
        'jerry.mouse': {'status': 'inactive', 'role': 'user', 'last_login': 30},
        'spike.dog': {'status': 'active', 'role': 'admin', 'last_login': 1},
        'tyke.dog': {'status': 'active', 'role': 'guest', 'last_login': 60},
        'butch.cat': {'status': 'inactive', 'role': 'user', 'last_login': 90},
        }


def user_access():
     
     for username, config in user_configs.items():
          
            status = config['status']
            role = config['role']
            last_login = config['last_login']
            
    

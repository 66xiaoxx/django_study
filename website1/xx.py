import  os
a=[{'a':1,'b':1},{'a':3,'b':4}]
items=[{'id': 1, 'account': 'xxx1', 'name': '糖糖1', 'password': '123456', 'birthday': '0',
'sex': '女', 'phone': '18986002624', 'mobile': None, 'email': None, 'address': None, 'create_time': None, 'status': None, 'update_time': None, 'update_user_id': None, 'create_user_id': None, 'agent_id': None, 'agent_phone': None, 'agent_last_login_time': None, 'user_icon': None, 'role_type': None, 'staff': 'SA', 'user_zw': None, 'task_notice_min': None, 'org_id': None, 'task_message_min': None, 'agent_pwd': None, 'config_status': None, 'night_account': None, 'submit_status': None, 'marry_date': None, 'kids_born_date': None, 'marital_status': None
, 'bearing_status': None, 'politics_status': None, 'census_register_type': None, 'native_place': None, 'nation': None, 'oa_account': None,
 'oa_account_status': None, 'platform_id': None, 'department_name': None, 'department_path': None, 'modify_password_lasttime': None},
       {'id': 1, 'account': 'xxx1', 'name': '糖糖1', 'password': '123456', 'birthday': '0',
        'sex': '女', 'phone': '18986002624', 'mobile': None, 'email': None, 'address': None, 'create_time': None,
        'status': None, 'update_time': None, 'update_user_id': None, 'create_user_id': None, 'agent_id': None,
        'agent_phone': None, 'agent_last_login_time': None, 'user_icon': None, 'role_type': None, 'staff': 'SA',
        'user_zw': None, 'task_notice_min': None, 'org_id': None, 'task_message_min': None, 'agent_pwd': None,
        'config_status': None, 'night_account': None, 'submit_status': None, 'marry_date': None, 'kids_born_date': None,
        'marital_status': None
           , 'bearing_status': None, 'politics_status': None, 'census_register_type': None, 'native_place': None,
        'nation': None, 'oa_account': None,
        'oa_account_status': None, 'platform_id': None, 'department_name': None, 'department_path': None,
        'modify_password_lasttime': None}
       ]
for i in items:
    print(i['account'])
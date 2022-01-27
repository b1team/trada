# from .test_connect import client
# from .test_register import TestCreateUser
# import json


# class TestLogin(TestCreateUser.test_create_user):
#     def test_login(self):
#         data = {
#             'username': 'falcol',
#             'password': '12345678'
#         }
#         response = client.post('/token', data=json.dumps(data))
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json()['token_type'], "bearer")
#         self.assertIsInstance(response.json()['access_token'], str)
#         # assert response.json()['access_token'] == '' # lay token o day

#     def test_get_profile(self):
#         headers = {
#             'Authorization':
#             'Bearer '+'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZhbGNvbCIsInVzZXJfaWQiOiI2MWQzYzlkYTI4MGFiMTMzM2RlMmI0ZjQiLCJleHAiOjE2NDEyNzMzMjJ9.kvZtVTCFC2jeS0Hyt_VBJWu5av_SFuIHx678BNIjfyY'
#         }

#         response = client.get("/users/me", headers=headers)
#         self.assertEqual(response.status_code, 200)
#         self.assertIsInstance(response.json(), dict)
#         self.assertEqual(response.json()['username'], 'falcol')

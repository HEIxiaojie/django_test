import requests
import unittest

class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/users'
        self.auth=('111','111')

    def test_get_user(self):
        r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['username'],'111')
        self.assertEqual(result['email'],'111@163.com')

    # def test_add_user(self):
    #     form_data={'username':'1222','email':'122@163.com','groups':'http://127.0.0.1:8000/groups/6/'}
    #     r=requests.post(self.base_url+'/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['username'],'1122')
    #     self.assertEqual(result['email'],'z1122@163.com')

    #
    # def test_update_user(self):
    #     form_data={'email':'118@163.com'}
    #     r=requests.patch(self.base_url+'/6/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['email'],'z11@163.com')

    # def test_delete_user(self):
    #     r=requests.delete(self.base_url+'/4/',auth=self.auth)
    #
    #     self.assertEqual(r.status_code,204)

    # def test_no_auth(self):
    #     r=requests.get(self.base_url)
    #     result=r.json()
    #
    #     self.assertEqual(result['detail'],'Authentication credentials were not provided.')


class GroupTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/groups'
        self.auth=('11','z118')

    def test_group_developer(self):
        r=requests.get(self.base_url+'/7/',auth=self.auth)
        result=r.json()

        self.assertEqual(result['name'],'Developer')

    # def test_add_group(self):
    #     form_data={'name':'Pm'}
    #     r=requests.post(self.base_url+'/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['name'],'Pm')

    # def test_update_group(self):
    #     form_data={'name':'Boss'}
    #     r=requests.patch(self.base_url+'/6/',data=form_data,auth=self.auth)
    #     result=r.json()
    #
    #     self.assertEqual(result['name'],'Boss')

    # def test_delete_group(self):
    #     r=requests.delete(self.base_url+'/6/',auth=self.auth)
    #     self.assertEqual(r.status_code,204)

if __name__ == '__main__':
    unittest.main()

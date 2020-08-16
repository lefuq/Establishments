from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.catering.models.establishments import Establishment
from apps.catering.models.dish import Dish
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UnitTests(APITestCase):
    def setUp(self):
        """
        Создание двух пользователей, создание токенов для них, присвоение
        первому заведения и блюда. Создание тестовых инстансов.
        """
        self.user = User.objects.create(username='firstUser')
        self.user.set_password('passwd')
        self.user.save()
        self.token = Token.objects.create(user=self.user)

        self.user2 = User.objects.create(username='secondUser')
        self.user2.set_password('passwd')
        self.user2.save()
        self.token2 = Token.objects.create(user=self.user2)

        self.est = Establishment.objects.create(
            name='firstPlace',
            work_time='С 10 до 20',
            address='Красноярск, Мира, 157',
            owner=self.user,
            )

        self.dish = Dish.objects.create(
            name='firstDish',
            cost=540,
            place=self.est,
            )
        self.dish.save()
        self.dish.ingredients.set([200, 201])

        self.new_user_test_instance = {
            'username': 'newUser',
            'password': 'newpasswd',
             }
        self.new_est_test_instance = {
            'name': 'newplace',
            'work_time': 'С 10 до 12',
            'address': 'Красноярск, Калинина, 8',
            }
        self.new_dish_test_instance= {
            'name': 'newDish',
            'cost': 500,
            'place': self.est.id,
            'ingredients': [200, 201],
            }

    def test_post_return_token(self):
        """
        Проверка возврата токена при POST-запросе во время создания
        пользователя.
        """
        url = reverse('users-list')
        response = self.client.post(url, self.new_user_test_instance, format='json')

        self.assertTrue('token' in response.data)

    def test_post_on_apitoken_return_token(self):
        """
        Проверка возврата токена при POST-запросе на api/auth/token при
        отправке учетных данных.
        """
        url = reverse('token')
        data = {'username':'firstUser', 'password':'passwd'}
        response = self.client.post(url, data, format='json')

        self.assertTrue('token' in response.data)

    def test_post_on_apitoken_do_not_return_token_if_login_failed(self):
        """
        Проверка возврата 400 ошибки при POST-запросе на api/auth/token при
        отправке неверных учетных данных.
        """
        url = reverse('token')
        response = self.client.post(url, self.new_user_test_instance, format='json')

        self.assertEqual(response.status_code, 400)

    def test_est_return_201_if_authorized_via_token(self):
        """
        Проверка создания заведения при POST-запросе, если в заголовке указано
        'Authorization: Token <token>'.
        """
        url = reverse('establishments-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        response = self.client.post(url, self.new_est_test_instance, format='json')

        self.assertEqual(response.status_code, 201)

    def test_est_do_not_return_201_if_not_authorized_via_token(self):
        """
        Проверка создания заведения при POST-запросе, если в заголовке не
        указано 'Authorization: Token <token>'.
        """
        url = reverse('establishments-list')
        response = self.client.post(url, self.new_est_test_instance, format='json')

        self.assertFalse(response.status_code==201)

    def test_est_owner_allowed_put_establishment(self):
        """
        Проверка изменения заведения при PUT-запросе, если пользователь является
        владельцем заведения.
        """
        url = reverse('establishments-detail', kwargs={'pk': self.est.id})
        data = {'name': 'newName'}
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, 200)

    def test_not_owner_not_allowed_put_establishment(self):
        """
        Проверка отказа в изменении заведения при PUT-запросе, если пользователь
        не является владельцем заведения.
        """
        url = reverse('establishments-detail', kwargs={'pk': self.est.id})
        data = {'name': 'newName'}
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token2.key))
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_est_owner_allowed_patch_establishment(self):
        """
        Проверка изменения заведения при PATCH-запросе, если пользователь
        является владельцем заведения.
        """
        url = reverse('establishments-detail', kwargs={'pk': self.est.id})
        data = {'name': 'newName'}
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, 200)

    def test_not_owner_not_allowed_patch_establishment(self):
        """
        Проверка отказа в изменении заведения при PATCH-запросе, если
        пользователь не является владельцем заведения.
        """
        url = reverse('establishments-detail', kwargs={'pk': self.est.id})
        data = {'name': 'newName'}
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token2.key))
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_est_owner_allowed_delete_establishment(self):
        """
        Проверка возможности удаления заведения, если пользователь
        является владельцем заведения.
        """
        url = reverse('establishments-detail', kwargs={'pk': self.est.id})
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, 204)

    def test_not_owner_not_allowed_delete_establishment(self):
        """
        Проверка возможности удаления заведения, если пользователь
        не является владельцем заведения.
        """
        url = reverse('establishments-detail', kwargs={'pk': self.est.id})
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token2.key))
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, 403)

    def test_est_owner_allowed_post_dish(self):
        """
        Проверка возможности создания блюда, если пользователь
        является владельцем заведения.
        """
        url = reverse('dishes-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        response = self.client.post(url, self.new_dish_test_instance, format='json')

        self.assertEqual(response.status_code, 201)

    def test_est_owner_allowed_put_dish(self):
        """
        Проверка возможности изменения блюда через PUT-запрос, если пользователь
        является владельцем заведения.
        """
        url = reverse('dishes-detail', kwargs={'pk': self.dish.id})
        data = {'name': 'newName', 'place': self.est.id, 'ingredients': [200, 201]}
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, 200)

    def test_not_owner_not_allowed_put_dish(self):
        """
        Проверка возможности изменения блюда через PUT-запрос, если пользователь
        не является владельцем заведения.
        """
        url = reverse('dishes-detail', kwargs={'pk': self.dish.id})
        data = {'name': 'newName', 'place': self.est.id, 'ingredients': [200, 201]}
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token2.key))
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_est_owner_allowed_patch_dish(self):
        """
        Проверка возможности изменения блюда через PATCH-запрос, если
        пользователь является владельцем заведения.
        """
        url = reverse('dishes-detail', kwargs={'pk': self.dish.id})
        data = {'name': 'newName'}
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, 200)

    def test_not_est_owner_not_allowed_patch_dish(self):
        """
        Проверка возможности изменения блюда через PATCH-запрос, если
        пользователь не является владельцем заведения.
        """
        url = reverse('dishes-detail', kwargs={'pk': self.dish.id})
        data = {'name': 'newName'}
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token2.key))
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, 403)

    def test_est_owner_allowed_delete_dish(self):
        """
        Проверка возможности удаления блюда через DELETE-запрос, если
        пользователь является владельцем заведения.
        """
        url = reverse('dishes-detail', kwargs={'pk': self.dish.id})
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, 204)

    def test_not_est_owner_not_allowed_delete_dish(self):
        """
        Проверка возможности удаления блюда через DELETE-запрос, если
        пользователь не является владельцем заведения.
        """
        url = reverse('dishes-detail', kwargs={'pk': self.dish.id})
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token2.key))
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, 403)

    def test_other_users_only_get_or_list_on_dishes(self):
        """
        Проверка остальных пользователей на возможность отправлять только GET
        и LIST запросы в блюдах.
        """
        url = reverse('dishes-list')
        response = self.client.post(url, self.new_dish_test_instance, format='json')
        self.assertEqual(response.status_code, 401)

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

        url = reverse('dishes-detail', kwargs={'pk': self.dish.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_other_users_only_get_or_list_on_establishments(self):
        """
        Проверка остальных пользователей на возможность отправлять только GET
        и LIST запросы в заведениях.
        """
        url = reverse('establishments-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

        url = reverse('establishments-detail', kwargs={'pk': self.est.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_ingredients_only_get(self):
        """
        Проверка ингредиентов на предоставление данных только через GET запросы.
        """
        url = reverse('ingredients-list')
        data = {'name': 'newIngr', 'callories': 480}

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401)

        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 405)

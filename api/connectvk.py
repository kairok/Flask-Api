import vk_api



from settings import  login, password
vk_session = vk_api.VkApi(login, password)

try:
        vk_session.auth()
except vk_api.AuthError as error_msg:
        print(error_msg)
vk = vk_session.get_api()
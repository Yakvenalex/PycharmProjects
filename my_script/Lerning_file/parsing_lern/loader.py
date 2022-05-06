import instaloader

ig = instaloader.Instaloader()
dp = input('Введите имя пользователя')

ig.download_profile(dp, profile_name=True)
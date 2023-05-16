import instaloader

l = instaloader.Instaloader()
profile = instaloader.Profile.from_username(l.context, 'sinapirzadeh_')

print(profile.followers)

from fastapi import FastAPI
from typing import Dict, List
from random import choice
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

images = [
    "https://images.prom.ua/3633715315_w640_h640_shtora-velyur-temno-seraya.jpg",
    "https://podushka.com.ua/upload/catalogue/shtora_s_podkhvatom_provans_bella_rozy_s_kruzhevom_1570405512.jpg",
    "https://images.prom.ua/1075328978_shtora-blekaut-green.jpg"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def generate_jsons() -> List[Dict[str, str]]:
    jsons = []
    for i in range(10):
        title = "Щтора " + str(choice(range(i+1)))
        description = "Гардина " + str(i+1)
        image = choice(images)
        jsons.append({"title": title, "description": description, "image": image})
    return jsons

APP_ID=531078899236306
REDIRECT_URI='https://wladarius.github.io/vlada/shtory.html'
INSTAGRAMM_URL=f'https://api.instagram.com/oauth/authorize?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&scope=user_profile,user_media&response_type=code'

#https://api.instagram.com/oauth/authorize?client_id=531078899236306&redirect_uri=https://wladarius.github.io/vlada/shtory.html&scope=user_profile,user_media&response_type=code



# https://wladarius.github.io/vlada/shtory.html?code=AQDb106VyWpCisYynNvW155ZXr_Th0SLXmH6xVybsl23f2kRjZ87epmqIGT3EU-GeRQfT87QS7GGMoFiuupuXCoVh8lYj7LXrkGBFPxL10rlXCeFm2hwa0tyNLemkj8S238gBwRbctOhqgK3p2QBFQcGX4UsUZTslRz6kr_R42WWw5G0LwGaJc2DEeb7a8HmDp3TF6GGE4pSwFMjmSqNq1ImJ3CBVpxLo9LZCVP_wetrjA#_


# curl -X POST \
#   https://api.instagram.com/oauth/access_token \
#   -F client_id=531078899236306 \
#   -F client_secret=67e017b33763acf786084b185e3bade3 \
#   -F grant_type=authorization_code \
#   -F redirect_uri=https://wladarius.github.io/vlada/shtory.html \
#   -F code=AQDb106VyWpCisYynNvW155ZXr_Th0SLXmH6xVybsl23f2kRjZ87epmqIGT3EU-GeRQfT87QS7GGMoFiuupuXCoVh8lYj7LXrkGBFPxL10rlXCeFm2hwa0tyNLemkj8S238gBwRbctOhqgK3p2QBFQcGX4UsUZTslRz6kr_R42WWw5G0LwGaJc2DEeb7a8HmDp3TF6GGE4pSwFMjmSqNq1ImJ3CBVpxLo9LZCVP_wetrjA#_

# {"access_token": "IGQVJVNEczRUhJVzNLaUNIQ1E1R0tFWXRrVWNzQzgzZAF9rbHZADTWdfUDkzeFk4Q050UWN3Qm5hWXJaTFlDWUdqVGlzSVNHcVFlVlpfRGdlTFlWU1YyRWxMMlFrNkxQNjkzVlhodHlsU0NKajhrbkh2RFRQZA2ZA3aDlWRUVn", "user_id": 17841445544215336}%

# curl -X GET \
#   'https://graph.instagram.com/17841445544215336?fields=id,username&access_token=IGQVJVNEczRUhJVzNLaUNIQ1E1R0tFWXRrVWNzQzgzZAF9rbHZADTWdfUDkzeFk4Q050UWN3Qm5hWXJaTFlDWUdqVGlzSVNHcVFlVlpfRGdlTFlWU1YyRWxMMlFrNkxQNjkzVlhodHlsU0NKajhrbkh2RFRQZA2ZA3aDlWRUVn'


# curl -X GET \
#   'https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url&access_token=IGQVJVNEczRUhJVzNLaUNIQ1E1R0tFWXRrVWNzQzgzZAF9rbHZADTWdfUDkzeFk4Q050UWN3Qm5hWXJaTFlDWUdqVGlzSVNHcVFlVlpfRGdlTFlWU1YyRWxMMlFrNkxQNjkzVlhodHlsU0NKajhrbkh2RFRQZA2ZA3aDlWRUVn'

#   caption
# id
# media_type
# The Media's type. Can be IMAGE, VIDEO, or CAROUSEL_ALBUM.
# media_url

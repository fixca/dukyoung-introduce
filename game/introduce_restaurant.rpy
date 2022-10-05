

image restaurant_1:
    im.FactorScale("images/introduce_restaurant/restaurant_1.png", 0.31746031746031746031746031746032)
    xalign 0.0
    yalign 0.0

image restaurant_2:
    im.FactorScale("images/introduce_restaurant/restaurant_2.png", 0.31746031746031746031746031746032)
    xalign 0.0
    yalign 0.0

image restaurant_3:
    im.FactorScale("images/introduce_restaurant/restaurant_3.png", 0.31746031746031746031746031746032)
    xalign 0.0
    yalign 0.0

image restaurant_4:
    im.FactorScale("images/introduce_restaurant/restaurant_4.png", 0.31746031746031746031746031746032)
    xalign 0.0
    yalign 0.0

image restaurant_cafe_1:
    im.FactorScale("images/introduce_restaurant/restaurant_cafe_1.png", 0.31746031746031746031746031746032)
    xalign 0.0
    yalign 0.0

image restaurant_cafe_2:
    im.FactorScale("images/introduce_restaurant/restaurant_cafe_2.png", 0.31746031746031746031746031746032)
    xalign 0.0
    yalign 0.0


label introducing_restaurant:
    "덕영 고등학교의 교내 식당은 2020년에 새로 시공하여 학생들이 쾌적한 환경에서 식사를 할 수 있도록 마련되어 있습니다."

    "그럼, 바로 교내 식당으로 안내해드리겠습니다."

    scene restaurant_1 with fade

    "이 곳이 덕영 고등학교의 교내 식당입니다."

    "교내 식당 바깥 쪽엔 야외에서 식사를 할 수 있는 카페 테리아가 있습니다."

    scene restaurant_cafe_1 with fade

    "이 곳이 교내 식당의 카페 테리아입니다."

    "야외에서 식사를 하고 싶은 학생 들을 위한 공간입니다."

    scene restaurant_2 with Fade(0.5, 0.0, 4.0)

    scene restaurant_3 with Fade(0.5, 0.0, 4.0)

    scene restaurant_cafe_2 with Fade(0.5, 0.0, 4.0)

    scene restaurant_4 with Fade(0.5, 0.0, 4.0)
    

    return
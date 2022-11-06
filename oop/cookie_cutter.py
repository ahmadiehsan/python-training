class FiveStarCookieCutter:
    def __init__(self):
        self.cookie_type = 'five_start'


class FlexibleStarCookieCutter:
    def __init__(self, cookie_type):
        if cookie_type not in ['five_start', 'six_start', 'eight_start']:
            raise ValueError()

        self.cookie_type = cookie_type


five_start_cookie_1 = FiveStarCookieCutter()
five_start_cookie_2 = FiveStarCookieCutter()

six_start_cookie = FlexibleStarCookieCutter('six_start')
eight_start_cookie = FlexibleStarCookieCutter('eight_start')

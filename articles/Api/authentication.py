from rest_framework.authentication import TokenAuthentication as BTA

class TokenAuthentication(BTA):
    keyword = 'Bearer' 
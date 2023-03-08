from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import jwt
class JWTQueryParamsAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        if not token:
            raise AuthenticationFailed({"code": 401, "error": "登录成功后才能访问"})
        salt = settings.SECRET_KEY
        try:
            payload = jwt.decode(jwt=token, key=salt, algorithm=["HS256"])
            return (payload,token)
        except jwt.exceptions.ExpiredSignatureError:
            error = "token已失效"
            raise AuthenticationFailed({"code": 401, "error": error})
        except jwt.exceptions.DecodeError:
            error = "token已认证失败"
            raise AuthenticationFailed({"code": 401, "error": error})
        except jwt.exceptions.InvalidTokenError:
            error = "非法的token"
            raise AuthenticationFailed({"code": 401, "error": error})


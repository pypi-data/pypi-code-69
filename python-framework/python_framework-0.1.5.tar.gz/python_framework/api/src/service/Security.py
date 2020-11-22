from flask_jwt_extended import get_current_user
from flask_jwt_extended import (
    JWTManager, jwt_required, get_jwt_identity,
    create_access_token, create_refresh_token,
    jwt_refresh_token_required, get_raw_jwt
)
from python_helper import Constant, log
import datetime
from python_framework.api.src.annotation.MethodWrapper import FunctionThrough

BLACK_LIST = set()

KW_JTI = 'jti'
KW_USER_CLAIMS = 'user_claims'
KW_IDENTITY = 'identity'
KW_FRESH = 'fresh'
KW_EXPIRATION = 'exp'
KW_NFB = 'nbf'
KW_IAT = 'iat'


KW_JWT_SECRET_KEY = 'JWT_SECRET_KEY'
KW_JWT_BLACKLIST_ENABLED = 'JWT_BLACKLIST_ENABLED'

DOT_SPACE_CAUSE = f'''{Constant.DOT_SPACE}{Constant.LOG_CAUSE}'''

@FunctionThrough
def getRawJwt(*arg,**kwargs) :
    return get_raw_jwt(*arg,**kwargs)

@FunctionThrough
def jwtRequired(*arg,**kwargs) :
    return jwt_required(*arg,**kwargs)

@FunctionThrough
def getJti(*arg,**kwargs) :
    return getRawJwt(*arg,**kwargs)[KW_JTI]

@FunctionThrough
def getRole(*arg,**kwargs) :
    return getRawJwt(*arg,**kwargs)[KW_USER_CLAIMS]

@FunctionThrough
def getIdentity(*arg,**kwargs) :
    return getRawJwt(*arg,**kwargs)[KW_IDENTITY]

@FunctionThrough
def addUserToBlackList() :
    BLACK_LIST.add(getJti())

@FunctionThrough
def getJwtMannager(appInstance, jwtSecret) :
    if not jwtSecret :
        log.warning(JWTManager, f'Not possible to instanciate jwtManager{DOT_SPACE_CAUSE}Missing jwt secret')
    else :
        jwtMannager = JWTManager(appInstance)
        appInstance.config[KW_JWT_SECRET_KEY] = jwtSecret
        appInstance.config[KW_JWT_BLACKLIST_ENABLED] = True
        return jwtMannager

@FunctionThrough
def addJwt(jwtInstance) :
    @jwtInstance.token_in_blacklist_loader
    def verifyAuthorizaionAccess(decriptedToken) :
        return decriptedToken[KW_JTI] in BLACK_LIST

    @jwtInstance.revoked_token_loader
    def invalidAccess() :
        return {'message': 'Access denied'}, HttpStatus.UNAUTHORIZED

@FunctionThrough
def createAccessToken(user, deltaMinutes=None) :
    ###- datetime.datetime.utcnow()
    if deltaMinutes :
        deltaMinutes = datetime.timedelta(minutes=deltaMinutes)
    return create_access_token(
        identity = user.id,
        fresh = False,
        expires_delta = deltaMinutes,
        user_claims = user.role,
        headers = None
    )

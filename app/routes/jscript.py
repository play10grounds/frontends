from fastapi import APIRouter
from starlette.requests import Request
from starlette.templating import Jinja2Templates

# 라우터 생성
jscript_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

# 라우트 설정
@jscript_router.get('/')
async def flex(req: Request):
    return templates.TemplateResponse('js/index.html', {'request': req})

@jscript_router.get('/hello')
async def flex(req: Request):
    return templates.TemplateResponse('js/01hello.html', {'request': req})

@jscript_router.get('/type')
async def flex(req: Request):
    return templates.TemplateResponse('js/02type.html', {'request': req})

@jscript_router.get('/operator')
async def flex(req: Request):
    return templates.TemplateResponse('js/03operator.html', {'request': req})

@jscript_router.get('/condition')
async def flex(req: Request):
    return templates.TemplateResponse('js/04condition.html', {'request': req})

@jscript_router.get('/loop')
async def flex(req: Request):
    return templates.TemplateResponse('js/05loop.html', {'request': req})

@jscript_router.get('/array')
async def flex(req: Request):
    return templates.TemplateResponse('js/06array.html', {'request': req})

@jscript_router.get('/while')
async def flex(req: Request):
    return templates.TemplateResponse('js/07while.html', {'request': req})

@jscript_router.get('/function')
async def flex(req: Request):
    return templates.TemplateResponse('js/08function.html', {'request': req})

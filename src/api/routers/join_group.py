from src.services.crud.groups import group_join
from fastapi import APIRouter
import datetime
from ..basemodels import join_info
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/join_group", tags=["join_group"])

@router.post("/join/", tags=["join_group"])
def join_group(join_gr: join_info):
    if join_gr.username is None:
        member_name = "vuonglv"
    if join_gr.group_name is None:
        member_name = "vuonglv"
    member_name = join_gr.username
    group_name = join_gr.group_name

    group = group_join.to_join_group(member_name, group_name)
    if group:
        res = {"username": member_name,
                "group_name": group_name,
                "success": True,
                "join_at": datetime.datetime.utcnow.strftime("%m/%d/%Y, %H:%M:%S")}

        return JSONResponse(res)

    return {"success": False}

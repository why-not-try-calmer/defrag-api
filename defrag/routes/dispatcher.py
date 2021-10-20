from typing import Optional
from defrag.modules.dispatcher import Dispatcher
from defrag.modules.helpers import Query, QueryResponse

from fastapi import APIRouter
router = APIRouter()

""" Dispatcher """


@router.get("/dispatcher/poll_due/")
async def poll_due(sync: Optional[bool] = None) -> QueryResponse:
    query = Query(service="dispatcher")
    results = await Dispatcher.poll_due(True if sync is None else sync)
    return QueryResponse(query=query, results_count=len(results), results=results)
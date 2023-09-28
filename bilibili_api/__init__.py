"""
bilibili_api

哔哩哔哩的各种 API 调用便捷整合（视频、动态、直播等），另外附加一些常用的功能。
"""

import asyncio
import platform

from .utils.sync import sync
from .credential import Credential
from .utils.picture import Picture
from .utils.short import get_real_url
from .utils.parse_link import ResourceType, parse_link
from .utils.aid_bvid_transformer import aid2bvid, bvid2aid
from .utils.danmaku import DmMode, Danmaku, DmFontSize, SpecialDanmaku
from .utils.network import (
    HEADERS,
    Api,
    retry,
    enc_wbi,
    get_nav,
    check_valid,
    get_session,
    set_session,
    get_mixin_key,
    get_aiohttp_session,
    set_aiohttp_session
)
from .errors import (
    LoginError,
    ApiException,
    ArgsException,
    LiveException,
    NetworkException,
    ResponseException,
    VideoUploadException,
    ResponseCodeException,
    DanmakuClosedException,
    CredentialNoBuvid3Exception,
    CredentialNoBiliJctException,
    DynamicExceedImagesException,
    CredentialNoSessdataException,
    CredentialNoDedeUserIDException,
)
from . import (
    app,
    ass,
    hot,
    game,
    live,
    note,
    rank,
    show,
    user,
    vote,
    audio,
    emoji,
    login,
    manga,
    topic,
    video,
    cheese,
    client,
    search,
    article,
    bangumi,
    channel,
    comment,
    dynamic,
    session,
    homepage,
    settings,
    live_area,
    video_tag,
    black_room,
    login_func,
    video_zone,
    favorite_list,
    channel_series,
    video_uploader,
    creative_center,
    article_category,
    interactive_video,
)

BILIBILI_API_VERSION = "16.1.1b0"

# 如果系统为 Windows，则修改默认策略，以解决代理报错问题
if "windows" in platform.system().lower():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # type: ignore

__all__ = [
    "Api",
    "ApiException",
    "ArgsException",
    "BILIBILI_API_VERSION",
    "check_valid",
    "Credential",
    "CredentialNoBiliJctException",
    "CredentialNoBuvid3Exception",
    "CredentialNoDedeUserIDException",
    "CredentialNoSessdataException",
    "Danmaku",
    "DanmakuClosedException",
    "DmFontSize",
    "DmMode",
    "DynamicExceedImagesException",
    "enc_wbi",
    "HEADERS",
    "LiveException",
    "LoginError",
    "NetworkException",
    "Picture",
    "ResourceType",
    "ResponseCodeException",
    "ResponseException",
    "SpecialDanmaku",
    "VideoUploadException",
    "aid2bvid",
    "app",
    "article",
    "article_category",
    "ass",
    "asyncio",
    "audio",
    "bangumi",
    "black_room",
    "bvid2aid",
    "channel",
    "channel_series",
    "cheese",
    "client",
    "comment",
    "creative_center",
    "dynamic",
    "emoji",
    "favorite_list",
    "game",
    "get_aiohttp_session",
    "get_mixin_key",
    "get_nav",
    "get_real_url",
    "get_session",
    "homepage",
    "hot",
    "interactive_video",
    "live",
    "live_area",
    "login",
    "login_func",
    "manga",
    "note",
    "parse_link",
    "platform",
    "rank",
    "retry",
    "search",
    "session",
    "set_aiohttp_session",
    "set_session",
    "settings",
    "show",
    "sync",
    "topic",
    "user",
    "video",
    "video_tag",
    "video_uploader",
    "video_zone",
    "vote",
]

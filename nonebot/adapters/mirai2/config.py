from typing import List, Optional

from pydantic import Field, Extra, BaseModel


class Config(BaseModel):
    """
    mirai2 配置类

    :配置项:

      - ``verify_key`` / ``mirai_verify_key``: mirai-api-http 的 verify_key
      - ``mirai_url``: mirai-api-http 的地址, domain.com/path
      - ``mirai_ssl``: 是否启用ssl
      - ``mirai_qq``: mirai-api-http qq 列表
    """

    verify_key: str = Field(
        ..., alias="mirai_verify_key"
    )
    mirai_url: str
    mirai_ssl: bool = False
    mirai_qq: List[int]

    class Config:
        extra = Extra.ignore
        allow_population_by_field_name = True

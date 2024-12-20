import inspect

from vkbottle_types.codegen.responses.wall import *  # noqa: F403,F401

from .base_response import BaseResponse


class WallGetByIdExtendedResponseModel(WallGetByIdExtendedResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()


class WallGetByIdResponseModel(WallGetByIdResponseModel):  # type: ignore[no-redef]
    items: typing.Optional[typing.List["WallWallpostFull"]] = Field(
        default=None,
    )


class WallGetExtendedResponseModel(WallGetExtendedResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()


class WallGetResponseModel(WallGetResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()


class WallSearchExtendedResponseModel(WallSearchExtendedResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()


class WallSearchResponseModel(WallSearchResponseModel):  # type: ignore[no-redef]
    items: typing.List["WallWallpostFull"] = Field()


_locals = locals().copy()
_locals_values = _locals.values()
for item in _locals_values:
    if not (inspect.isclass(item) and issubclass(item, BaseResponse)):
        continue
    item.update_forward_refs(**_locals)
    for parent in item.__bases__:
        if parent.__name__ == item.__name__:
            parent.__fields__.update(item.__fields__)  # type: ignore
            parent.update_forward_refs(**_locals)  # type: ignore

# from attrs import asdict, define, field


# @define
# class UserResponse:
#     image = field(default=42)
#     has_errors = field(default=False)
#     error = field(default="")
#     success = field(default="")
#     alert = field(default="")
#     detected_stickers = field(factory=list)
#     reel = field(default=None)
#     reel_image = field(default=None)
#     item = field(default={})
#     sub = field(default=None)

#     @property
#     def json(self):
#         return asdict(self)

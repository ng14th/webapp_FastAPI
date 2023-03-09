from app.user.models.user import User

async def sync_password_expr(time_now : float):
    list_user_pw_expr = await User.collection.aggregate({'password_expr':{'$lte':str(time_now)}})
    async for user in list_user_pw_expr:
        print(user)
    return True
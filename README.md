# Arknights-kazimierz-major
明日方舟2.5周年签到活动脚本


### 使用方式：
1、打开[活动网页](https://ak.hypergryph.com/activity/kazimierz-major?source=bilibili)  
2、获取token  
如果是B服请直接登录，如果已登录请跳过此步。  
如果是官服，请暂时不要登录，如已经登陆，请先退出登录。  
按F12打开开发者工具——>找到Network选项卡——>登录账号——>找到**token_by_phone_password**——>点击**Response**——>复制```token:```中的内容到脚本的```x-session_token```中。  
3、获取uid  
可以直接在网页中账号信息中看到你自己的uid，并填入脚本中的```uid```。  
3、获取cookie  
在开发者工具中的Console里输入```document.cookie```并复制到脚本的```raw_cookies```中，不要复制单引号。  
![image](./images/gettoke.png)

运行后，将会在每天4：00自动签到。

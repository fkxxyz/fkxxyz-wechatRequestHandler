## 接受普通消息

### 文本消息

```
ToUserName      开发者微信号
FromUserName    发送方帐号（一个OpenID）
CreateTime      消息创建时间 （整型）
MsgType         消息类型，文本为text
Content         文本消息内容
MsgId           消息id，64位整型
```

### 图片消息

```
ToUserName      开发者微信号
FromUserName    发送方帐号（一个OpenID）
CreateTime      消息创建时间 （整型）
MsgType         消息类型，图片为image
PicUrl          图片链接（由系统生成）
MediaId         图片消息媒体id，可以调用获取临时素材接口拉取数据。
MsgId           消息id，64位整型
```

### 语音消息

```
ToUserName      开发者微信号
FromUserName    发送方帐号（一个OpenID）
CreateTime      消息创建时间 （整型）
MsgType         语音为voice
MediaId         语音消息媒体id，可以调用获取临时素材接口拉取数据。
Format          语音格式，如amr，speex等
Recognition     语音识别结果，UTF8编码（需要开通语音识别）
MsgID           消息id，64位整型
```

### 视频消息

```
ToUserName      开发者微信号
FromUserName    发送方帐号（一个OpenID）
CreateTime      消息创建时间 （整型）
MsgType         视频为video
MediaId         视频消息媒体id，可以调用获取临时素材接口拉取数据。
ThumbMediaId    视频消息缩略图的媒体id，可以调用多媒体文件下载接口拉取数据。
MsgId           消息id，64位整型
```

### 小视频消息

```
ToUserName      开发者微信号
FromUserName    发送方帐号（一个OpenID）
CreateTime      消息创建时间 （整型）
MsgType         小视频为shortvideo
MediaId         视频消息媒体id，可以调用获取临时素材接口拉取数据。
ThumbMediaId    视频消息缩略图的媒体id，可以调用获取临时素材接口拉取数据。
MsgId           消息id，64位整型
```

### 地理位置消息

```
ToUserName      开发者微信号
FromUserName    发送方帐号（一个OpenID）
CreateTime      消息创建时间 （整型）
MsgType         消息类型，地理位置为location
Location_X      地理位置维度
Location_Y      地理位置经度
Scale           地图缩放大小
Label           地理位置信息
MsgId           消息id，64位整型
```

### 链接消息

```
ToUserName      接收方微信号
FromUserName    发送方微信号，若为普通用户，则是一个OpenID
CreateTime      消息创建时间
MsgType         消息类型，链接为link
Title           消息标题
Description     消息描述
Url             消息链接
MsgId           消息id，64位整型
```

## 接收事件推送

### 关注/取消关注事件

```
ToUserName      开发者微信号
FromUserName    发送方帐号（一个OpenID）
CreateTime      消息创建时间 （整型）
MsgType         消息类型，event
Event           事件类型，subscribe(订阅)、unsubscribe(取消订阅)
```

### 扫描带参数二维码事件

```
ToUserName      开发者微信号
FromUserName    发送方帐号（一个OpenID）
CreateTime      消息创建时间 （整型）
MsgType         消息类型，event
Event           事件类型，subscribe
EventKey        事件KEY值，qrscene_为前缀，后面为二维码的参数值
Ticket          二维码的ticket，可用来换取二维码图片
```

### 用户已关注时的事件推送

```
ToUserName      开发者微信号
FromUserName    发送方帐号（一个OpenID）
CreateTime      消息创建时间 （整型）
MsgType         消息类型，event
Event           事件类型，SCAN
EventKey        事件KEY值，是一个32位无符号整数，即创建二维码时的二维码scene_id
Ticket          二维码的ticket，可用来换取二维码图片
```

### 上报地理位置事件

```
ToUserName      开发者微信号
FromUserName    发送方帐号（一个OpenID）
CreateTime      消息创建时间 （整型）
MsgType         消息类型，event
Event           事件类型，LOCATION
Latitude        地理位置纬度
Longitude       地理位置经度
Precision       地理位置精度
```

### 自定义菜单事件

```
ToUserName      开发者微信号
FromUserName    发送方帐号（一个OpenID）
CreateTime      消息创建时间 （整型）
MsgType         消息类型，event
Event           事件类型，CLICK
EventKey        事件KEY值，与自定义菜单接口中KEY值对应
```

## 被动回复用户消息

### 回复文本消息

```
ToUserName      是    接收方帐号（收到的OpenID）
FromUserName    是    开发者微信号
CreateTime      是    消息创建时间 （整型）
MsgType         是    消息类型，文本为text
Content         是    回复的消息内容（换行：在content中能够换行，微信客户端就支持换行显示）
```

### 回复图片消息

```
ToUserName      是    接收方帐号（收到的OpenID）
FromUserName    是    开发者微信号
CreateTime      是    消息创建时间 （整型）
MsgType         是    消息类型，图片为image
MediaId         是    通过素材管理中的接口上传多媒体文件，得到的id。
```

### 回复语音消息

```
ToUserName      是    接收方帐号（收到的OpenID）
FromUserName    是    开发者微信号
CreateTime      是    消息创建时间戳 （整型）
MsgType         是    消息类型，语音为voice
MediaId         是    通过素材管理中的接口上传多媒体文件，得到的id
```

### 回复视频消息

```
ToUserName      是    接收方帐号（收到的OpenID）
FromUserName    是    开发者微信号
CreateTime      是    消息创建时间 （整型）
MsgType         是    消息类型，视频为video
MediaId         是    通过素材管理中的接口上传多媒体文件，得到的id
Title           否    视频消息的标题
Description     否    视频消息的描述
```

### 回复音乐消息

```
ToUserName      是    接收方帐号（收到的OpenID）
FromUserName    是    开发者微信号
CreateTime      是    消息创建时间 （整型）
MsgType         是    消息类型，音乐为music
Title           否    音乐标题
Description     否    音乐描述
MusicURL        否    音乐链接
HQMusicUrl      否    高质量音乐链接，WIFI环境优先使用该链接播放音乐
ThumbMediaId    是    缩略图的媒体id，通过素材管理中的接口上传多媒体文件，得到的id
```

### 回复图文消息

```
ToUserName      是    接收方帐号（收到的OpenID）
FromUserName    是    开发者微信号
CreateTime      是    消息创建时间 （整型）
MsgType         是    消息类型，图文为news
ArticleCount    是    图文消息个数；当用户发送文本、图片、视频、图文、地理位置这五种消息时，开发者只能回复1条图文消息；其余场景最多可回复8条图文消息
Articles        是    图文消息信息，注意，如果图文数超过限制，则将只发限制内的条数
Title           是    图文消息标题
Description     是    图文消息描述
PicUrl          是    图片链接，支持JPG、PNG格式，较好的效果为大图360*200，小图200*200
Url             是    点击图文消息跳转链接
```


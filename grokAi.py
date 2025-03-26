from .tool import *
import time
from openai import OpenAI

# 文字
class YN_GrokAi_TX:

    def __init__(self):
        content = get_key()
        self.index = 0
        self.keys = [key.strip() for key in content.split('\n') if key.strip()]

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": (["grok-2-latest"],),
                "system":("STRING", {"multiline": True, "default": "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。"},),
                "prompt":("STRING", {"multiline": True, "default": ""},), 
            }
        }

    RETURN_TYPES = ("STRING",) 
    RETURN_NAMES = ("out",)
    FUNCTION = "gen"
    OUTPUT_NODE = False 
    CATEGORY = "CXH/gemini"

    def gen(self,model,system,prompt):
        if len(self.keys) ==0 :
            print("Grok key is empty, please register")

        #key
        if self.index >= len(self.keys):
            self.index = 0
        apikey = self.keys[self.index]
        client = OpenAI(
            api_key=apikey,
            base_url="https://api.x.ai/v1",
        )
        self.index = self.index + 1

        response = client.chat.completions.create(
            model=model,  # 填写需要调用的模型编码
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
        )

        print(response)
        # 将结果列表中的张量连接在一起
        return (response.choices[0].message.content,)

# 单个图片反推
class YN_GrokAi_Vision:
    def __init__(self):
        content = get_key()
        self.index = 0
        self.keys = [key.strip() for key in content.split('\n') if key.strip()]
        # self.client = ZhipuAI(api_key=self.api_key)

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "model": (["grok-2-vision-latest"],),
                "prompt":   ("STRING", {"multiline": True, "default": "请用英文详细描述这张图像，不要使用任何中文。英文输出。"},),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("out",)
    FUNCTION = "gen"
    OUTPUT_NODE = False
    CATEGORY = "CXH"

    def gen(self, image,model,prompt:str):

        pil_image = tensor2pil(image)
        
        image_base64 = pilTobase64(pil_image)

        if len(self.keys) ==0 :
            print("Grok key is empty, please register")

        #key
        if self.index >= len(self.keys):
            self.index = 0
        apikey = self.keys[self.index]
        client = OpenAI(
            api_key=apikey,
            base_url="https://api.x.ai/v1",
        )
        self.index = self.index + 1

        response = client.chat.completions.create(
            model=model,  # 填写需要调用的模型名称
            messages=[
                {"role": "user",
                 "content": [
                     {
                         "type": "text",
                         "text": prompt
                     },
                     {
                         "type": "image_url",
                         "image_url": {
                             "url": f"data:image/jpeg;base64,{image_base64}",
                             "detail": "high",
                         }
                     }
                 ]
                 },
            ],
        )
        content = response.choices[0].message.content
        return(content,)

# 文字
class YN_GrokAi_Image_Gen:

    def __init__(self):
        content = get_key()
        self.index = 0
        self.keys = [key.strip() for key in content.split('\n') if key.strip()]

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": (["grok-2-image"],),
                "prompt":("STRING", {"multiline": True, "default": ""},), 
            }
        }

    RETURN_TYPES = ("IMAGE","STRING","STRING",) 
    RETURN_NAMES = ("image","url","revised_prompt",)
    FUNCTION = "gen"
    OUTPUT_NODE = False 
    CATEGORY = "CXH/gemini"

    def gen(self,model,prompt):
        if len(self.keys) ==0 :
            print("Grok key is empty, please register")

        #key
        if self.index >= len(self.keys):
            self.index = 0
        apikey = self.keys[self.index]
        client = OpenAI(
            api_key=apikey,
            base_url="https://api.x.ai/v1",
        )
        self.index = self.index + 1

        response = client.images.generate(
            model=model,
            prompt=prompt
        )
        print(response.data[0].url)
        print(response.data[0])

        img = img_from_url(response.data[0].url)

        img = pil2tensor(img)

        print(response)
        # 将结果列表中的张量连接在一起
        return (img,response.data[0].url,response.data[0].revised_prompt)
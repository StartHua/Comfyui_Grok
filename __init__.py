
from .grokAi import YN_GrokAi_TX,YN_GrokAi_Vision,YN_GrokAi_Image_Gen

NODE_CLASS_MAPPINGS = {
    "YN_GrokAi_TX":YN_GrokAi_TX,
    "YN_GrokAi_Vision":YN_GrokAi_Vision,
    "YN_GrokAi_Image_Gen":YN_GrokAi_Image_Gen
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "YN_GrokAi_TX":"YN:Grok_TX",
    "YN_GrokAi_Vision":"YN:Grok_Vision",
    "YN_GrokAi_Image_Gen":"YN:Grok_Image_Gen"
}

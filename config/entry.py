"""
 * @author: zkyuan
 * @date: 2025/4/8 16:44
 * @description: 模型的配置
"""
import os

__all__ = [
    "MY_QWEN_VL_MODEL_NAME",
    "MY_QWEN_VL_API_KEY",
    "MY_QWEN_VL_URL",
    "MY_PROMPT_VL_USER",
    "my_prompt_vl_Customize",
]

"""模型的api-key和url"""
# 千问图像识别的的模型名
MY_QWEN_VL_MODEL_NAME = os.getenv("MY_QWEN_VL_MODEL_NAME")
# 千问图像识别的的模型api-key
MY_QWEN_VL_API_KEY = os.getenv("MY_QWEN_VL_API_KEY")
# 千问图像识别的的模型url
MY_QWEN_VL_URL = os.getenv("MY_QWEN_VL_URL")

"""提示词"""
MY_PROMPT_VL_USER = """
请根据图片中的内容，生成一份格式为Markdown格式的文档
"""


def my_prompt_vl_Customize(prompt: str) -> str:
    """输入需要识别的内容"""
    return f"""
    # 角色定义
    你是一名专业的图像识别助手，专门负责分析用户提供的图片，并依据用户的具体需求提取信息。
    
    ## 任务描述
    ### 图像内容识别
    - **目标**：识别并提取图片中的所有相关信息。
    - **内容包括但不限于**：
      - 文字（包括艺术字、印刷体和手写体）
      - 特定主题元素（如：{prompt}）
      - 表格、图形、流程图等（如果存在）
      
    - **优先级**：
      - 若图片中包含表格、图形或流程图，请特别指出并尽可能详细地描述这些元素的内容。
      - 如果没有上述复杂结构，专注于识别图片中的文本信息即可，无需进行额外的格式化处理。
    
    ### 识别标准
    - 确保提取的信息完整且精确，保持文本逻辑清晰，避免丢失任何关键细节。
    
    ## 输出指南
    ### 标题层级使用规则
    - 使用以下Markdown语法来创建标题层级：
      - `##` 一级标题
      - `###` 二级标题
      - `####` 三级标题
      - `#####` 四级标题
    
    ### 输出格式要求
    - 所有输出应遵循Markdown文档格式，示例如下：
    ```markdown
    识别的具体内容
    ```
    请按照以上指导原则进行操作，确保所提供的信息既全面又准确，以满足用户的特定需求。
    """

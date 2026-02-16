import json
import os
from datetime import datetime
from typing import List, Dict, Optional

GROUPS_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "groups.json")
CONTEXTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "contexts")

DEFAULT_BOTS = ["chatgpt", "claude", "grok", "gemini", "glm", "kimi", "minimax", "qwen", "deepseek", "seed"]

BOT_NAMES = {
    "chatgpt": "ChatGPT",
    "claude": "Claude",
    "grok": "Grok",
    "gemini": "Gemini",
    "glm": "GLM",
    "kimi": "Kimi",
    "minimax": "MiniMax",
    "qwen": "Qwen",
    "deepseek": "DeepSeek",
    "seed": "Seed",
}

if not os.path.exists(CONTEXTS_DIR):
    os.makedirs(CONTEXTS_DIR)


def load_groups() -> List[Dict]:
    """加载群组列表"""
    if not os.path.exists(GROUPS_FILE):
        default_groups = [
            {
                "id": "grp_all",
                "name": "全员群",
                "bots": DEFAULT_BOTS.copy(),
                "is_default": True,
                "created_at": datetime.now().isoformat()
            }
        ]
        save_groups(default_groups)
        return default_groups
    
    with open(GROUPS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_groups(groups: List[Dict]) -> bool:
    """保存群组列表"""
    try:
        with open(GROUPS_FILE, 'w', encoding='utf-8') as f:
            json.dump(groups, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"保存群组失败: {e}")
        return False


def get_group(group_id: str) -> Optional[Dict]:
    """获取指定群组"""
    groups = load_groups()
    for g in groups:
        if g["id"] == group_id:
            return g
    return None


def create_group(name: str, bots: List[str]) -> Optional[Dict]:
    """创建新群组"""
    groups = load_groups()
    
    if len(groups) >= 6:
        return None
    
    group_names = [g["name"] for g in groups]
    if name in group_names:
        return None
    
    new_group = {
        "id": f"grp_{int(datetime.now().timestamp() * 1000)}",
        "name": name,
        "bots": bots,
        "is_default": False,
        "created_at": datetime.now().isoformat()
    }
    
    groups.insert(0, new_group)
    
    if save_groups(groups):
        init_group_context(new_group["id"])
        return new_group
    return None


def update_group(group_id: str, name: str, bots: List[str]) -> Optional[Dict]:
    """更新群组"""
    groups = load_groups()
    
    for i, g in enumerate(groups):
        if g["id"] == group_id:
            if g.get("is_default"):
                return None
            
            old_bots = set(g["bots"])
            new_bots = set(bots)
            removed_bots = old_bots - new_bots
            added_bots = new_bots - old_bots
            
            g["name"] = name
            g["bots"] = bots
            
            if save_groups(groups):
                for bot in added_bots:
                    clear_bot_group_context(bot, group_id)
                
                return g
            return None
    
    return None


def delete_group(group_id: str) -> bool:
    """删除群组"""
    groups = load_groups()
    
    for i, g in enumerate(groups):
        if g["id"] == group_id:
            if g.get("is_default"):
                return False
            
            group_file = os.path.join(CONTEXTS_DIR, f"{group_id}.json")
            if os.path.exists(group_file):
                os.remove(group_file)
            
            groups.pop(i)
            return save_groups(groups)
    
    return False


def get_group_context(group_id: str) -> Dict[str, List[Dict]]:
    """获取群组的上下文"""
    context_file = os.path.join(CONTEXTS_DIR, f"{group_id}.json")
    if not os.path.exists(context_file):
        return {}
    
    with open(context_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def init_group_context(group_id: str) -> None:
    """初始化群组上下文文件"""
    context_file = os.path.join(CONTEXTS_DIR, f"{group_id}.json")
    if not os.path.exists(context_file):
        with open(context_file, 'w', encoding='utf-8') as f:
            json.dump({}, f)


def add_to_group_context(group_id: str, bot: str, role: str, content: str) -> None:
    """添加消息到群组上下文"""
    context_file = os.path.join(CONTEXTS_DIR, f"{group_id}.json")
    
    if not os.path.exists(context_file):
        init_group_context(group_id)
    
    with open(context_file, 'r', encoding='utf-8') as f:
        context = json.load(f)
    
    if bot not in context:
        context[bot] = []
    
    context[bot].append({"role": role, "content": content})
    
    with open(context_file, 'w', encoding='utf-8') as f:
        json.dump(context, f, ensure_ascii=False, indent=2)


def clear_bot_group_context(bot: str, group_id: str) -> bool:
    """清除特定群组中特定 bot 的上下文"""
    context_file = os.path.join(CONTEXTS_DIR, f"{group_id}.json")
    if not os.path.exists(context_file):
        return True
    
    with open(context_file, 'r', encoding='utf-8') as f:
        context = json.load(f)
    
    if bot in context:
        del context[bot]
    
    with open(context_file, 'w', encoding='utf-8') as f:
        json.dump(context, f, ensure_ascii=False, indent=2)
    
    return True


def clear_group_context(group_id: str) -> bool:
    """清除整个群组的上下文"""
    context_file = os.path.join(CONTEXTS_DIR, f"{group_id}.json")
    if os.path.exists(context_file):
        os.remove(context_file)
    init_group_context(group_id)
    return True


def get_all_groups_context(bots: List[str]) -> Dict[str, List[Dict]]:
    """获取多个群组的上下文聚合"""
    groups = load_groups()
    result = {}
    
    for bot in bots:
        result[bot] = []
    
    for group in groups:
        group_context = get_group_context(group["id"])
        for bot in bots:
            if bot in group_context:
                result[bot].extend(group_context[bot])
    
    return result

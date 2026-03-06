"""
生成书籍所需的示例截图
使用matplotlib生成流程图、界面示意图等
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建输出目录
output_dir = '/workspace/projects/silicon-team-guide/screenshots/generated'
os.makedirs(output_dir, exist_ok=True)

def create_workflow_diagram():
    """创建AI内容团队工作流程图"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # 标题
    ax.text(5, 9.5, 'AI内容团队协作流程', fontsize=20, ha='center', fontweight='bold')
    
    # 用户
    user_box = FancyBboxPatch((4, 8), 2, 0.8, boxstyle="round,pad=0.1", 
                               facecolor='#3B82F6', edgecolor='#1E40AF', linewidth=2)
    ax.add_patch(user_box)
    ax.text(5, 8.4, '👤 用户', fontsize=14, ha='center', color='white', fontweight='bold')
    
    # 三个Bot
    bots = [
        ('选题Bot', 1.5, 6, '#10B981'),
        ('写作Bot', 5, 6, '#8B5CF6'),
        ('排版Bot', 8.5, 6, '#F59E0B')
    ]
    
    for name, x, y, color in bots:
        box = FancyBboxPatch((x-0.8, y-0.4), 1.6, 0.8, boxstyle="round,pad=0.1",
                            facecolor=color, edgecolor='black', linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y, f'🤖 {name}', fontsize=11, ha='center', color='white', fontweight='bold')
    
    # 箭头
    arrow_style = dict(arrowstyle='->', color='#6B7280', lw=2)
    
    # 用户到Bot
    ax.annotate('', xy=(1.5, 6.8), xytext=(5, 8), arrowprops=arrow_style)
    ax.annotate('', xy=(5, 6.8), xytext=(5, 8), arrowprops=arrow_style)
    ax.annotate('', xy=(8.5, 6.8), xytext=(5, 8), arrowprops=arrow_style)
    
    # Bot之间
    ax.annotate('', xy=(5, 5.2), xytext=(1.5, 5.6), arrowprops=arrow_style)
    ax.annotate('', xy=(8.5, 5.2), xytext=(5, 5.6), arrowprops=arrow_style)
    
    # 输出
    output_box = FancyBboxPatch((3.5, 3), 3, 0.8, boxstyle="round,pad=0.1",
                               facecolor='#EF4444', edgecolor='#B91C1C', linewidth=2)
    ax.add_patch(output_box)
    ax.text(5, 3.4, '📄 完整文章', fontsize=12, ha='center', color='white', fontweight='bold')
    
    # 最终箭头
    ax.annotate('', xy=(5, 3.8), xytext=(5, 5.6), arrowprops=arrow_style)
    
    # 时间标注
    times = ['08:00', '08:10', '08:20', '08:35']
    for i, t in enumerate(times):
        ax.text(0.3, 8-i*1.5, t, fontsize=10, color='#6B7280')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/ch05-workflow-diagram.png', dpi=150, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()
    print(f'✅ 已生成: workflow-diagram.png')

def create_agent_config_screenshot():
    """创建Agent配置界面示意图"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # 模拟窗口
    window = FancyBboxPatch((0.5, 0.5), 9, 9, boxstyle="round,pad=0.1",
                           facecolor='#F3F4F6', edgecolor='#9CA3AF', linewidth=2)
    ax.add_patch(window)
    
    # 标题栏
    title_bar = FancyBboxPatch((0.5, 8.5), 9, 1, boxstyle="round,pad=0.05",
                              facecolor='#3B82F6', edgecolor='none')
    ax.add_patch(title_bar)
    ax.text(5, 9, '创建新 Agent', fontsize=16, ha='center', color='white', fontweight='bold')
    
    # 表单字段
    fields = [
        ('名称:', '写作Bot', 7.5),
        ('英文名:', 'WriterBot', 6.5),
        ('模型:', 'GPT-4', 5.5),
        ('工作区:', '/workspace/writer', 4.5),
    ]
    
    for label, value, y in fields:
        ax.text(1.5, y, label, fontsize=12, ha='left', fontweight='bold')
        input_box = FancyBboxPatch((3.5, y-0.3), 5, 0.5, boxstyle="round,pad=0.02",
                                  facecolor='white', edgecolor='#D1D5DB', linewidth=1)
        ax.add_patch(input_box)
        ax.text(3.7, y-0.05, value, fontsize=11, ha='left', color='#374151')
    
    # 角色描述文本框
    ax.text(1.5, 3.5, '角色描述:', fontsize=12, ha='left', fontweight='bold')
    desc_box = FancyBboxPatch((1.5, 1), 7, 2.2, boxstyle="round,pad=0.05",
                             facecolor='white', edgecolor='#D1D5DB', linewidth=1)
    ax.add_patch(desc_box)
    
    # 文本内容
    desc_text = """# 角色：写作Bot

你是一名资深科技自媒体写手...

## 写作风格
1. 开头要炸
2. 结构清晰  
3. 金句频出"""
    
    ax.text(1.7, 2.9, desc_text, fontsize=9, ha='left', va='top', 
           color='#374151', family='monospace')
    
    # 按钮
    save_btn = FancyBboxPatch((7, 0.2), 1.5, 0.5, boxstyle="round,pad=0.05",
                             facecolor='#10B981', edgecolor='#059669', linewidth=1)
    ax.add_patch(save_btn)
    ax.text(7.75, 0.45, '保存', fontsize=11, ha='center', color='white', fontweight='bold')
    
    cancel_btn = FancyBboxPatch((5, 0.2), 1.5, 0.5, boxstyle="round,pad=0.05",
                               facecolor='#E5E7EB', edgecolor='#9CA3AF', linewidth=1)
    ax.add_patch(cancel_btn)
    ax.text(5.75, 0.45, '取消', fontsize=11, ha='center', color='#374151')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/ch05-agent-config.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f'✅ 已生成: agent-config.png')

def create_cost_comparison_chart():
    """创建成本对比图"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    categories = ['人工助理', '外包公司', 'OpenClaw\nAI团队']
    costs = [8000, 4000, 400]
    colors = ['#EF4444', '#F59E0B', '#10B981']
    
    bars = ax.bar(categories, costs, color=colors, edgecolor='black', linewidth=1.5)
    
    # 添加数值标签
    for bar, cost in zip(bars, costs):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'¥{cost}',
                ha='center', va='bottom', fontsize=14, fontweight='bold')
    
    ax.set_ylabel('月度成本（元）', fontsize=12)
    ax.set_title('AI团队 vs 传统方案 - 成本对比', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylim(0, 9000)
    
    # 添加网格
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    
    # 添加节省标注
    ax.annotate('节省95%!', xy=(2, 400), xytext=(2.5, 2500),
                arrowprops=dict(arrowstyle='->', color='#10B981', lw=2),
                fontsize=12, color='#10B981', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/ch02-cost-comparison.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f'✅ 已生成: cost-comparison.png')

def create_efficiency_chart():
    """创建效率提升对比图"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    categories = ['内容创作', '客服回复', '数据分析', '报告撰写']
    before = [240, 30, 180, 480]  # 分钟
    after = [45, 3, 15, 120]  # 分钟
    
    x = np.arange(len(categories))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, before, width, label='传统方式', color='#EF4444', edgecolor='black')
    bars2 = ax.bar(x + width/2, after, width, label='AI团队', color='#10B981', edgecolor='black')
    
    ax.set_ylabel('时间（分钟）', fontsize=12)
    ax.set_title('AI团队效率提升对比', fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend(fontsize=11)
    
    # 添加数值标签
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom', fontsize=9)
    
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/ch01-efficiency-comparison.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f'✅ 已生成: efficiency-comparison.png')

def create_multi_agent_architecture():
    """创建多Agent架构图"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # 标题
    ax.text(5, 9.5, '5人AI助理团队架构', fontsize=20, ha='center', fontweight='bold')
    
    # 用户层
    user = FancyBboxPatch((4, 8), 2, 0.8, boxstyle="round,pad=0.1",
                         facecolor='#3B82F6', edgecolor='#1E40AF', linewidth=2)
    ax.add_patch(user)
    ax.text(5, 8.4, '👤 用户', fontsize=14, ha='center', color='white', fontweight='bold')
    
    # AIBoss（中心协调）
    boss = FancyBboxPatch((4, 6), 2, 0.8, boxstyle="round,pad=0.1",
                         facecolor='#EF4444', edgecolor='#B91C1C', linewidth=2)
    ax.add_patch(boss)
    ax.text(5, 6.4, '👔 AIBoss\n大总管', fontsize=12, ha='center', color='white', fontweight='bold')
    
    # 4个专业Agent
    agents = [
        ('📰 AINews', '资讯助理', 1.5, 4, '#10B981'),
        ('✍️ AIContent', '内容助理', 4, 4, '#8B5CF6'),
        ('💻 AICode', '代码助理', 6.5, 4, '#F59E0B'),
        ('📋 AITask', '任务助理', 9, 4, '#EC4899')
    ]
    
    for emoji_name, role, x, y, color in agents:
        box = FancyBboxPatch((x-0.9, y-0.5), 1.8, 1, boxstyle="round,pad=0.1",
                            facecolor=color, edgecolor='black', linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y+0.15, emoji_name, fontsize=10, ha='center', color='white', fontweight='bold')
        ax.text(x, y-0.25, role, fontsize=9, ha='center', color='white')
    
    # 箭头
    arrow_style = dict(arrowstyle='->', color='#6B7280', lw=2)
    
    # 用户到Boss
    ax.annotate('', xy=(5, 6.8), xytext=(5, 8), arrowprops=arrow_style)
    
    # Boss到各Agent
    for x in [1.5, 4, 6.5, 9]:
        ax.annotate('', xy=(x, 4.8), xytext=(5, 6), arrowprops=arrow_style)
    
    # 添加说明
    ax.text(5, 2.5, 'AIBoss统一接收用户需求，分发给各专业Agent', 
           fontsize=11, ha='center', style='italic', color='#6B7280')
    ax.text(5, 2, 'Agent间可互相协作，完成任务后汇总给AIBoss',
           fontsize=11, ha='center', style='italic', color='#6B7280')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/ch08-multi-agent-arch.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f'✅ 已生成: multi-agent-arch.png')

# 生成所有截图
if __name__ == '__main__':
    print('🎨 开始生成书籍截图...\n')
    create_workflow_diagram()
    create_agent_config_screenshot()
    create_cost_comparison_chart()
    create_efficiency_chart()
    create_multi_agent_architecture()
    print(f'\n✅ 所有截图已生成到: {output_dir}')
    print(f'📊 共生成 5 张示意图')

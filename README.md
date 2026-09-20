# Personal Skills

可持续维护的个人 AI 学习技能。方法与模板在这里迭代，教材、学习笔记和个人掌握记录保存在各自学习项目中。

## 技能目录

| Skill | 适用场景 | 版本 |
| --- | --- | --- |
| [personal-learning-skill](personal-learning-skill/SKILL.md) | 默认推荐：概念优先、四图建模、网状学习、跨学科适配、Obsidian 与华为笔记衔接 | 1.2.0 |
| [learning-method-skill](learning-method-skill/SKILL.md) | 轻量学习循环：目标、尝试、反馈、变式和复习 | 0.1.0 |

两个技能是可选方案，一次学习通常选一个。完整版是当前主要维护方向；轻量版保留独立用途，不自动把不同版本的规则混在一起。

## 在其他项目使用

在能够访问本仓库的助手中发送：

> 请读取本仓库 personal-learning-skill/SKILL.md，并按当前任务需要读取其中引用的文件。按这个流程带我学习本项目的课程。课程资料、状态和笔记留在本项目，不写回公共技能。

本机维护目录为 `E:/agent/skill`，保留 `<skill-name>/SKILL.md` 结构，因此已有绝对路径调用仍然有效。其他设备可以克隆到自己的目录；云端助手需取得实际技能文件，无法仅凭本机路径访问。完整技能应带上 references/ 与 templates/；本仓库本身不保证宿主自动安装或发现技能。

## 修改与更新

1. 先记录具体使用问题、预期行为及实际表现，可使用 Issues 中的改进模板。
2. 小步修改对应 Skill；参数改模板，流程改主文件，条件性细节改 references/。
3. 更新技能版本及其修改记录，并在 [CHANGELOG.md](CHANGELOG.md) 记录仓库级变化。
4. 安装检查依赖并检查文件：

   ```sh
   python -m pip install -r requirements-dev.txt
   python scripts/validate_skills.py
   python -m unittest discover -s tests
   ```

5. 对影响教学行为的修改，再实际跑相关场景。静态检查通过不代表教学效果已验证。
6. 检查差异后提交和推送。重要版本创建单独的技能标签，例如 `personal-learning-skill-v1.2.0`。后续标签不复用、不覆盖。

日常由本地编辑、Git 提交保存历史、GitHub 同步备份；其他电脑更新前先提交自己的改动，再执行 `git pull --ff-only`。出现冲突时按双方意图合并，不直接覆盖。

## 内容与分发

- 源文件是维护依据；旧 ZIP 和便携合并稿保留在本地，不加入 Git 历史，避免多个版本混淆。
- 不上传教材 PDF、个人学习记录、设备配置或凭据。忽略规则只是辅助，提交前仍应检查文件清单。
- 结构借鉴及原始来源见 [设计依据](personal-learning-skill/references/design-notes.md)。本项目并非上游作者的官方作品。
- 当前未选择开源许可证。公开可见不等于授予任意复制、修改或再分发授权；如果计划开放复用，后续明确许可证并保留必要的第三方声明。

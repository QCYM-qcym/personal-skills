# 学习状态文件模板

在课程状态目录内按以下文件边界创建；这是模板而非真实进度。说明文字应替换为用户实际信息，未知填“待确认”。不把本模板直接当作一个所有课程共享的数据库。

## MISSION.md

```yaml
project_id: "填写稳定课程标识"
course: "课程名称"
project_root: "课程根目录"
goal: "可检验目标"
scope: "本轮课程范围"
acceptance: "验收任务"
```

## CURRENT.md

```yaml
state_schema: 1
project_id: "与 MISSION 一致"
revision: 0
last_event_id: null
skill_name: "当前选用的技能名"
skill_version: "实际读取的版本"
updated_at: null
timezone: "待确认"
activity: "未开始"
resume_activity: null
node_id: null
last_hint_level: null
pending_task: null
next_action: "选择一个可检验学习节点"
```

pending_task 有任务时写完整题目或可访问文件及精确位置、要求用户做什么；next_action 始终只选一个立即动作。NODES 与 REVIEWS 的详细结果不要重复拷贝进 CURRENT。

有 HTML 课程时可加 lesson_id、lesson_path、diagnosis_ref、scaffold_plan，分别记录当前课、实际课件路径、诊断依据和支架策略。MISSION/RESOURCES 如指向课程根目录正文，在对应文件写明 project_id 和相对路径，按协议跟随读取，勿复制整份正文。

## NODES.md

| 节点 ID | 名称 | 必要前置 | 能力状态 | 最近证据/事件 | 是否待巩固及原因 |
| --- | --- | --- | --- | --- | --- |

## REVIEWS.md

| 任务 ID | 节点 ID | 闭卷任务与通过标准 | due 与时区/触发条件 | 状态 | 结果事件 |
| --- | --- | --- | --- | --- | --- |

## learning-records/事件ID.md

```yaml
event_id: "不会复用的唯一 ID"
project_id: "与 MISSION 一致"
occurred_at: "实际发生时间，含时区"
base_revision: 0
target_revision: 1
type: "讲解/尝试/反馈/提示/复查/暂停/恢复/迁移/偏好变化"
```

- 用户证据或来源：注明实际作答、自述、未作答；链接附件或摘录关键一步。
- 预期变更：逐项写明文件、节点/任务 ID、旧值与新值，供中断后检查并补全。
- 立即下一步：一个明确任务。

MISSION/个人设置/材料索引按课程需要补齐。无文件能力时，以这些字段组成可复制接续包并标“未落盘”，空表可省略。

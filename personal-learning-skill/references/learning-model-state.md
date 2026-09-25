# 学习模型可选扩展 v1

此契约补充 [状态协议](state-protocol.md)，不是新数据库或执行引擎。保留 state_schema: 1、四种节点能力状态、既有ID、revision、用户注释与未知字段；仅在当前课程按需增加字段，旧项目不用重建。其他Skill读取时保留扩展字段，不推断其含义。

## 唯一存放位置

| 信息 | 权威位置 |
| --- | --- |
| 主线、模块计划、overview覆盖、深挖队列 | 既有 MISSION 正文；展示页仅链接 |
| 来源角色/版本/实际已读/答案暴露 | 既有 RESOURCES 正文 |
| phase、step、当前任务、下一步 | CURRENT；phase与原activity分开 |
| 节点接触情况与能力维度证据 | NODES；已有math_facets维度原位复用 |
| 知识/误解/题型三逻辑视图 | 已有maps边表，正文引用glossary/solve-cards/事件 |
| 尝试、诊断、修复、模型变化 | learning-records原事件 |
| 复测安排/完成 | REVIEWS，继续使用旧任务ID和状态 |

## CURRENT与深挖队列

CURRENT 可加 learning_model_extension: 1、phase（生命周期表枚举）、step（PREDICT/ATTEMPT/VERIFY/FAIL或空）、phase_evidence_ref、orientation_scope、map_check（pending/passed/needs_repair/skipped）、hint_scheme、resume_phase。phase不是activity或能力状态：出题才activity=等待作答；首错提示为反馈修正；发新复测为待验证；纯讲授无题只存下一入口，不制造pending_task。这条有无任务的条件化解释优先于共享协议“AI讲完→等待作答”的简写。

只有同范围总览已交付且真实地图回答足够，才在MISSION记录 FAST_ORIENTATION_COMPLETE 和证据。跳过不记完成。新教材仅扩展新范围。已有pending_task先恢复，用户转任务时保存原任务引用和跳过/待回访原因，不覆盖丢失。暂停同时保存resume_activity/resume_phase，读预览不恢复。

MISSION深挖项：id、node_ref、issue、need_tags、blocking（判断及理由）、status（queued/in_progress/resolved/deferred）、priority_reason、evidence_ref、next_action。resolved仅表示已处理该问题，不等于掌握；迁移/延迟证据另记。队列按需排序，不以教材页序为永久顺序。一个CURRENT当前任务，队列只是候选。

## 暴露情况、能力画像与旧四状态

八标签是不同证据侧面，不是强制线性升级：

| 标签 | 可接受证据与边界 |
| --- | --- |
| SEEN | 实际材料/讲授暴露记录；不升级能力 |
| UNDERSTOOD / ORIENTED | 用户自述单独标self_report；若有解释任务，引用其实际结果 |
| REMEMBERED | 无资料提取关键内容；不自动证明会用 |
| GUIDED_APPLY | 有知识点/模型/步骤提示后应用，附提示与线索 |
| INDEPENDENT_RECOGNITION | 无显式及上下文模型线索的新题中识别结构/条件 |
| ROBUST | 在相关易混/干扰/边界任务中实际正确，限已测情境 |
| TRANSFERABLE | 新情境结构映射、选择、应用及边界通过；不能只换数字 |
| TEACHABLE | 脱稿教回并回答WHY/条件，限实际检验范围 |

NODES可选 learning_facets 按 node_id + dimension 索引：Recall、Conceptual Understanding、Explanation、Recognition、Condition Checking、Model Selection、Strategy Selection、Execution、Error Resistance、Transfer、Teach Back。数学已有同维度 math_facets 为唯一权威，仅新增缺少维度，通用视图引用它，不复制同一能力记录。

每项含 state（仍为旧四状态）、evidence_ref、task_ref、assessed_at、context、cue_level（labeled/contextual/none/unknown）、hint_scheme与hint_level、answer_seen、permitted_resources、retest_kind；未测维度省略或明确unknown，不伪造通过。NODES主行保留原任务范围的兼容摘要，不取维度平均/最小值。见过/自述只写exposure记录，不改主行能力证据。

不使用无范围MASTERED。若用户问是否稳定掌握，逐项报告Recall、Recognition、Condition Checking、Application、Variant、Transfer、Delayed Retest的实际证据和缺口；至少迁移与后续延迟未验证时不能宣称稳定可迁移。某一项通过不自动补其他项，TEACHABLE不等于实践通过。

旧L0表示旧体系的询问/请尝试，绝不是新H0无提示。旧记录保持L标识；新记录显式H-v1。无法判定旧提示/线索写unknown，绝不追溯升级独立性。

## 三种图：共享节点和证据

1. Knowledge Graph：既有概念、公式、定理、模型、方法及有依据的关系。
2. Misconception Graph：误解模式与 affected_node、关键区别、fails_when、修复策略/复测引用。通用模式标general；个人关联必须有实际attempt_ref，根因标hypothesis/confirmed/rejected及依据。更正追加事件而非删除历史。
3. Problem Pattern Graph：solve card正文负责 recognition_signals、hidden_structure、relevant_knowledge、model（适用时）、assumptions、preferred_strategy、alternatives、traps、common_errors、variants、transfer_contexts；maps仅引用卡及相关节点/误解模式。

统一边最小字段沿用 id/from/relation/to/conditions或context/source_ref，增加 basis（为何连）、scope（general/personal）、evidence_ref（个人边必需）。现有中文关系允许保留，用别名映射而非复制同一边。

| 关系 | 方向/语义 |
| --- | --- |
| prerequisite_of / prerequisite | A为B前置：A→B；depends_on是反向展示 |
| derived_from / derives_from | 结果→依据，二者为别名 |
| motivates | 问题/缺口→新概念；非逻辑蕴含 |
| implies | 前提/命题→结论，注明条件 |
| requires | 结论或用法→必要条件；充分条件不能误标必要 |
| used_by | 工具→使用者 |
| contrasts_with / commonly_confused_with | 对比/易混对象，注明维度 |
| generalizes_to / special_case_of | 特殊→一般，同事实一条边 |
| approximates | 近似模型→目标对象，注明极限/误差条件 |
| equivalent_under | 两者在条件下等价，可双向展示 |
| fails_without | 结论→被删条件，需具体反例；未知必要性不能使用 |
| incorrectly_generalized_to / false_equivalence | 错误推广/错误等同，明确为误解边，不当知识事实 |
| missing_condition / wrong_model_trigger | 误解模式→遗漏条件/错误触发线索 |
| fails_when / misinterpreted_as | 模式→失效情境 / 原概念→误读对象 |

## 事件、复盘、保存

原事件按需补 prediction、attempt_ref、observed_error、error_types、root_cause_hypothesis/certainty、misconception_ref、affected_nodes、minimal_repair、retest_ref；模型变化补 before_model、trigger_evidence、after_model、changed_relation、future_signal、remaining_uncertainty。用户未表达过的before_model只能标假设；新证据反驳时记录撤销。

共享提示/诊断与数学error_diagnosis引用同一事件正文，不再保存另一份结果。复测关联旧错误与新任务，REVIEWS保存排程；安排任务不算完成，过期不自动降级。扩展更新同样执行事件先写→NODES/图/队列/REVIEWS按需→CURRENT最后提交→读回，并将预期变更纳入恢复检查。无文件能力把相关扩展放未落盘接续包，不能声称已保存。

## 旧课程接续检查

- 原project_id、state_schema、节点ID、证据、用户注释及未知字段保留。
- 只恢复一个真实pending_task；阶段缺失根据活动暂定且注明推断，不造历史总览通过。
- 旧“即时独立通过”只覆盖原任务；无cue/transfer证据不推断识别或迁移。
- 分发共享协议文件不改，其他三技能能力不随本版升级；使用本扩展时遵循这里的条件化细则。

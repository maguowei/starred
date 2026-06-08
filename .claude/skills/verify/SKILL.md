---
name: verify
description: 验证对 starred 项目的改动 —— 运行 pycodestyle lint 与针对真实 GitHub API 的集成测试。在需要确认改动可用、提交前验证时使用。
---

# 验证 starred 改动

按顺序执行,任一步骤失败即停止并报告。

## 1. Lint 与格式检查

```bash
uv run ruff check starred
uv run ruff format --check starred
```

两条命令均无报错、退出码为 0 即通过。若有违规,先用 `uv run ruff check --fix starred` 和 `uv run ruff format starred` 修复再继续。

## 2. 集成测试

需要环境变量 `GITHUB_TOKEN`(GitHub personal access token)。若未设置,提示用户提供后再运行。

```bash
uv run starred --username maguowei --token ${GITHUB_TOKEN} --sort
```

确认命令成功退出且输出为合理的 Markdown(无报错、无乱码)。

## 报告

汇总两步结果:lint 是否通过、集成测试是否成功。如有失败,给出具体错误与定位。
